# multi-encoder
 Multi-encoder Python script supporting Base64, Base32, Base16, Base85, URL, HTML, Hex, and ROT13.
- URL Encoding  
- HTML Encoding  
- ASCII to Hex Encoding  
- Hex Encoding  
- Base85 Encoding  
- ROT13 Encoding  

## Features
- Encode any text into 6 different formats.
- CLI-based for simplicity.
- Easy to extend with more encodings.

## Requirements
- Python 3.7+
- Standard libraries only (`urllib`, `html`, `base64`, `codecs`, `binascii`).

##  Usage

Run the script:

```bash
python encoder.py
```
# Example
```bash
# Encode text using Base64
python encoder.py -e "hello world" --b64

# Output: aGVsbG8gd29ybGQ=

# Decode Base64
python encoder.py -d "aGVsbG8gd29ybGQ=" --b64

# Output: hello world

# Encode text using ROT13
python encoder.py -e "hello world" --rot13

# Output: uryyb jbeyq

# Encode text using Base85
python encoder.py -e "hello world" --b85

# Output: nm&qn=E,6C

# Encode text using URL encoding
python encoder.py -e "hello world" --url

# Output: hello%20world

# Encode text using HTML encoding
python encoder.py -e "<h1>Hello</h1>" --html

# Output: &lt;h1&gt;Hello&lt;/h1&gt;

# Encode text using Hex
python encoder.py -e "hello" --hex

# Output: 68656c6c6f
```

# License

This project is licensed under the MIT License – see the LICENSE

# Contributing

Pull requests are welcome! Please open an issue to discuss any new features or improvements.










