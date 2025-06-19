# Huffman Compression Program

A simple Python program to perform **Huffman Encoding** for text compression. This tool reads input from the user or a file, compresses the text using Huffman coding, and shows the savings in file size. It also saves the compressed data in a file and performs decompression to verify correctness.

---

## 📌 Features

- Compress text using **Huffman Encoding**
- Supports input via:
  - Terminal/command line
  - Text files
- Displays:
  - Huffman tree structure
  - Binary codes for each character
  - Original and compressed file sizes
  - Bit savings
- Saves compressed output to a file (`compressed.txt`)
- Automatically **decodes the compressed text** to verify correctness

---

## 🧪 Example Usage

```bash
$ python huffman.py
Huffman Compression Program
=================================================================
Enter 1 if you want to enter in command window, 2 if you are using some file: 1
Enter the string you want to compress: hello
