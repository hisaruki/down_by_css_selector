# Web Image Downloader

A command-line tool to download images from web pages using CSS selectors.

## Features

- Download images from any web page using CSS selectors
- Automatically detect image selectors if not specified
- Customize output filenames and directory structure
- Support for both relative and absolute image URLs

## Installation

```bash
git clone https://github.com/hisaruki/down_by_css_selector.git
cd down_by_css_selector
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python web_image_downloader.py URL [CSS_SELECTOR]
```

Options:
- `URL`: Target web page URL (required)
- `CSS_SELECTOR`: CSS selector to find images (optional)
- `--digit N`: Number of digits for sequential filenames (default: 5)
- `--orig`: Keep original filenames instead of sequential numbers
- `--title TITLE`: Specify custom directory name for downloaded images

Example:
```bash
# Download images using automatic selector detection
python web_image_downloader.py https://example.com

# Download images with specific CSS selector
python web_image_downloader.py https://example.com "div.content img[src]"

# Keep original filenames
python web_image_downloader.py https://example.com --orig

# Save in custom directory
python web_image_downloader.py https://example.com --title "my_images"
```

## Requirements

- Python 3.6+
- beautifulsoup4
- requests
- lxml

## License

MIT License - see [LICENSE](LICENSE) file for details

---

# ウェブ画像ダウンローダー

CSSセレクターを使用してウェブページから画像をダウンロードするコマンドラインツールです。

## 特徴

- CSSセレクターを使用して任意のウェブページから画像をダウンロード
- セレクターを指定しない場合は自動検出
- 出力ファイル名とディレクトリ構造のカスタマイズが可能
- 相対URLと絶対URLの両方に対応

## インストール

```bash
git clone https://github.com/hisaruki/down_by_css_selector.git
cd down_by_css_selector
pip install -r requirements.txt
```

## 使い方

基本的な使用方法:
```bash
python web_image_downloader.py URL [CSSセレクター]
```

オプション:
- `URL`: 対象のウェブページURL（必須）
- `CSS_SELECTOR`: 画像を検索するCSSセレクター（省略可）
- `--digit N`: 連番ファイル名の桁数（デフォルト: 5）
- `--orig`: 連番ではなく元のファイル名を保持
- `--title TITLE`: ダウンロードした画像を保存するディレクトリ名を指定

使用例:
```bash
# 自動セレクター検出を使用して画像をダウンロード
python web_image_downloader.py https://example.com

# 特定のCSSセレクターで画像をダウンロード
python web_image_downloader.py https://example.com "div.content img[src]"

# 元のファイル名を保持
python web_image_downloader.py https://example.com --orig

# カスタムディレクトリに保存
python web_image_downloader.py https://example.com --title "my_images"
```

## 必要要件

- Python 3.6以上
- beautifulsoup4
- requests
- lxml

## ライセンス

MITライセンス - 詳細は[LICENSE](LICENSE)ファイルを参照してください 