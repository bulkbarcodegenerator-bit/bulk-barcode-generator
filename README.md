# Bulk Barcode Generator

Free browser-based tool that generates up to **500 barcodes at once** — Code 128, EAN-13, UPC-A, QR codes and more. No signup, no watermark, no data uploaded.

🌐 **Live tool:** https://bulkbarcodegeneratorr.com/

## Features

- Generate up to 500 barcodes in a single batch
- Symbologies: Code 128, Code 39, EAN-13, EAN-8, UPC-A, UPC-E, ITF-14, QR Code, Data Matrix, ISBN
- Import from Excel / CSV, or paste a list of codes
- Export as PNG, JPG, SVG, PDF, or download everything as ZIP
- 100% browser-local — your spreadsheet data never leaves your device

## Try the demos in this repo

- `demo/index.html` — open it in any browser. Generates sample EAN-13, Code 128 and UPC barcodes instantly with [JsBarcode](https://github.com/lindell/JsBarcode).
- `python/barcode_batch.py` — reads product codes from a CSV file and saves each barcode as a PNG:

```bash
pip install python-barcode pillow
python python/barcode_batch.py codes.csv
```

## Links

- Live tool: https://bulkbarcodegeneratorr.com/
- Generate barcodes from Excel/CSV: https://bulkbarcodegeneratorr.com/generate-barcodes-from-excel-csv-bulk/
- EAN-13 explained: https://bulkbarcodegeneratorr.com/ean-13-barcode-explained/

## License

MIT — see [LICENSE](LICENSE).
