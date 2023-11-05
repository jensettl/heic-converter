# heic-converter

Convert HEIC Files from directory or individual files to JPEG locally on your machine.

## Requirements

- Python 3.6+
- Pillow
- pyheif

## Installation

```
pip install -r requirements.txt
```

## Usage

```
python heic_converter.py
```

Prompt asks for directory or file path. If `folder` is selected, all HEIC files in the directory will be converted to JPEG and copied to the same directory. If `files` is selected, the selected files will be converted to JPEG and copied to the same directory.
