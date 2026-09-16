# pdftools

A small command-line toolbox for working with PDF files, built with
[pypdf](https://pypdf.readthedocs.io/). Structured as subcommands
(`merge`, `split`, ...) so new operations can be added over time.

Built as a learning project while studying cybersecurity (EPITA).

## Features

- `merge` — combine several PDF files into one, in order
- `split` — split a PDF into one file per page

More subcommands (rotate, watermark, page extraction...) may be added
later.

## Requirements

- Python 3.9+
- [pypdf](https://pypi.org/project/pypdf/)

## Installation

```bash
git clone https://github.com/AEG1X/pdftools.git
cd pdftools
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Merge PDFs into `output.pdf`:

```bash
python3 pdftools.py merge file1.pdf file2.pdf file3.pdf
```

Merge PDFs into a custom output file:

```bash
python3 pdftools.py merge file1.pdf file2.pdf --output combined.pdf
```

Split a PDF into one file per page (`page_1.pdf`, `page_2.pdf`, ...):

```bash
python3 pdftools.py split file.pdf
```

## Author & credits

Code written by Aegis. This README was drafted with the help of Claude
(Anthropic).

## License

MIT — see [LICENSE](LICENSE).
