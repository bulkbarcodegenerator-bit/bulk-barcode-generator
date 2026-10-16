#!/usr/bin/env python3
"""
barcode_batch.py — generate PNG barcodes from a CSV file.

Usage:
    pip install python-barcode pillow
    python barcode_batch.py codes.csv

The CSV should have one product code per line (a header row is skipped
automatically if it is not numeric). Each code is saved as PNG in ./output/.
Symbology is picked automatically: 13 digits -> EAN-13, 12 digits -> UPC-A,
anything else -> Code 128.

Part of the Bulk Barcode Generator project: https://bulkbarcodegeneratorr.com/
"""

import csv
import os
import sys

from barcode import Code128, Ean13, Upca
from barcode.writer import ImageWriter


def pick_symbology(code):
    if len(code) == 13 and code.isdigit():
        return Ean13
    if len(code) == 12 and code.isdigit():
        return Upca
    return Code128


def main(csv_path):
    os.makedirs("output", exist_ok=True)
    made = 0
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        for row in csv.reader(f):
            if not row:
                continue
            code = row[0].strip()
            if not code or (made == 0 and not code[0].isdigit() and len(code) != 13):
                # skip a header row like "code" / "sku"
                if not any(ch.isdigit() for ch in code):
                    continue
            symbology = pick_symbology(code)
            barcode = symbology(code, writer=ImageWriter())
            barcode.save(os.path.join("output", code))
            made += 1
            print("saved output/{}.png ({})".format(code, symbology.__name__))
    print("Done: {} barcodes written to ./output/".format(made))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python barcode_batch.py codes.csv")
        sys.exit(1)
    main(sys.argv[1])
