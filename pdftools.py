#!/usr/bin/env python3
"""
pdftools - A small command-line toolbox for working with PDF files.

Currently supports:
  - merge : combine several PDF files into one
  - split : split a PDF into one file per page
"""

import argparse
import os
import sys

from pypdf import PdfReader, PdfWriter

parser = argparse.ArgumentParser(
    prog="pdftools",
    description="A small command-line toolbox for working with PDF files.",
)

subparsers = parser.add_subparsers(dest="command", required=True)

merge_parser = subparsers.add_parser("merge", help="Merge several PDF files into one")
merge_parser.add_argument("files", nargs="+", help="PDF files to merge, in order")
merge_parser.add_argument(
    "--output", type=str, default="output.pdf", help="Output file name (default: output.pdf)"
)

split_parser = subparsers.add_parser("split", help="Split a PDF into one file per page")
split_parser.add_argument("files", nargs="+", help="PDF file(s) to split")

args = parser.parse_args()

for file in args.files:
    if not os.path.exists(file):
        print(f"Error: file not found: {file}")
        sys.exit(1)

if args.command == "merge":
    writer = PdfWriter()
    for file in args.files:
        writer.append(file)
    writer.write(args.output)
    writer.close()
    print(f"Merged {len(args.files)} file(s) into {args.output}")

elif args.command == "split":
    for file in args.files:
        reader = PdfReader(file)
        for i, page in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(page)
            writer.write(f"page_{i + 1}.pdf")
            writer.close()
        print(f"Split {file} into {len(reader.pages)} file(s)")
