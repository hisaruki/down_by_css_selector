#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import requests
import argparse
from urllib import parse
from bs4 import BeautifulSoup
from pathlib import Path
from collections import Counter
from urllib.parse import urljoin
import sys

parser = argparse.ArgumentParser(description="Download images using CSS selectors")
parser.add_argument('url', type=str)
parser.add_argument('selectors', type=str, nargs='?')
parser.add_argument('--digit', type=int, default=5)
parser.add_argument('--orig', action='store_true')
parser.add_argument('--title', type=str)
args = parser.parse_args()

sys.stderr.write(args.url + "\n")
response = requests.get(args.url)
webpage = BeautifulSoup(response.text, "lxml")

def download_image(image_url, output_filename=None):
    url_path = Path(parse.urlparse(image_url).path)
    file_suffix = url_path.suffix
    if not output_filename:
        output_filename = url_path.stem
    local_path = Path(output_filename + file_suffix)
    if image_url.find("http") < 0:
        image_url = urljoin(args.url, image_url)
    print(image_url + "\t" + str(local_path))

def extract_image_urls(base_url, css_selector, current_depth, webpage):
    attribute_name = css_selector.split(" ")[-1]
    attribute_name = re.search(r'\[([a-zA-Z0-9]*).*\]', attribute_name).groups()[0]
    for image_element in webpage.select(css_selector):
        yield urljoin(base_url, image_element.get(attribute_name)), current_depth + 1, webpage.title.text.strip()

def detect_image_selectors(webpage):
    image_classes = []
    for img in webpage.select('img[src*=".jpg"]'):
        css_class = img.get("class")
        if css_class:
            image_classes.append(" ".join(css_class))
    for main_class, count in Counter(image_classes).most_common():
        break
    if not main_class:
        sys.exit()
    class_parts = main_class.split(" ")
    image_selector = "img." + ".".join(class_parts)
    image_selector += '[src]'
    image_selector = '.entry-content img[src*=".jpg"]'
    return image_selector

if args.selectors:
    css_selectors = args.selectors
else:
    css_selectors = detect_image_selectors(webpage)

css_selectors = css_selectors.split("|")
css_selectors = map(lambda x:x.lstrip().rstrip(), css_selectors)
css_selectors = list(css_selectors)
image_counter = 0

def process_images(current_url, current_selector, current_depth):
    global image_counter
    for image_url, depth, page_title in extract_image_urls(current_url, current_selector, current_depth, webpage):
        if depth == len(css_selectors):
            output_filename = image_url.split("/")[-1]
            output_filename = re.sub(r'\?.*', '', output_filename)
            if not args.orig:
                output_filename = str(image_counter).zfill(args.digit)
            if len(page_title) > 32:
                page_title = page_title[0:32]
            if args.title:
                page_title = args.title
            if page_title:
                output_filename = page_title + "/" + output_filename
            download_image(image_url, output_filename)
            image_counter += 1
        else:
            process_images(image_url, css_selectors[depth], depth)

process_images(args.url, css_selectors[0], 0)
