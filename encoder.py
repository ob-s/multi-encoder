### Author: OBBY
# TITLE: ENCODER
# DATE: 22 AUGUST 2025

import base64
import argparse
import textwrap
import html
import codecs
from urllib.parse import quote, unquote

# Parser setup
parser = argparse.ArgumentParser(
    prog='Encoder',
    description='SIMPLE PYTHON PROGRAM FOR ENCODING & DECODING USING DIFFERENT ENCODERS',
    epilog=textwrap.dedent('''Example:
      encoder.py -e -b64 "data"     # encode data with base64
      encoder.py -d -b64 "data"     # decode data with base64
      encoder.py -e -b85 "data"     # encode data with base85
      encoder.py -e -rot13 "data"   # encode data with ROT13
      encoder.py -e -html "data"    # html encode data
      encoder.py -e -url "data"     # url encode data
      encoder.py -e -hex "data"     # hex encode data
    ''')
)

parser.add_argument('-e', '--encode', help='Encode input text')
parser.add_argument('-d', '--decode', help='Decode input text')
parser.add_argument('-b64', '--base64', action='store_true', help='Use Base64')
parser.add_argument('-b32', '--base32', action='store_true', help='Use Base32')
parser.add_argument('-b16', '--base16', action='store_true', help='Use Base16')
parser.add_argument('-b85', '--base85', action='store_true', help='Use Base85')
parser.add_argument('-html', '--htmlencode', action='store_true', help='Use HTML')
parser.add_argument('-url', '--urlencode', action='store_true', help='Use URL')
parser.add_argument('-hex', '--hexencode', action='store_true', help='Use Hex')
parser.add_argument('-rot13', '--rot13encode', action='store_true', help='Use ROT13')

args = parser.parse_args()

# ---------- Encoding / Decoding Functions ----------

def base64_encode(data: str) -> str:
    return base64.b64encode(data.encode()).decode()

def base64_decode(data: str) -> str:
    return base64.b64decode(data.encode()).decode()

def base32_encode(data: str) -> str:
    return base64.b32encode(data.encode()).decode()

def base32_decode(data: str) -> str:
    return base64.b32decode(data.encode()).decode()

def base16_encode(data: str) -> str:
    return base64.b16encode(data.encode()).decode()

def base16_decode(data: str) -> str:
    return base64.b16decode(data.encode()).decode()

def base85_encode(data: str) -> str:
    return base64.b85encode(data.encode()).decode()

def base85_decode(data: str) -> str:
    return base64.b85decode(data.encode()).decode()

def html_encode(data: str) -> str:
    return html.escape(data)

def html_decode(data: str) -> str:
    return html.unescape(data)

def url_encode(data: str) -> str:
    return quote(data)

def url_decode(data: str) -> str:
    return unquote(data)

def hex_encode(data: str) -> str:
    return data.encode().hex()

def hex_decode(data: str) -> str:
    return bytes.fromhex(data).decode()

def rot13_encode(data: str) -> str:
    return codecs.encode(data, "rot_13")

def rot13_decode(data: str) -> str:
    return codecs.decode(data, "rot_13")

# ---------- Main Logic ----------
if args.encode:
    data = args.encode
    if args.base64:
        print(base64_encode(data))
    elif args.base32:
        print(base32_encode(data))
    elif args.base16:
        print(base16_encode(data))
    elif args.base85:
        print(base85_encode(data))
    elif args.htmlencode:
        print(html_encode(data))
    elif args.urlencode:
        print(url_encode(data))
    elif args.hexencode:
        print(hex_encode(data))
    elif args.rot13encode:
        print(rot13_encode(data))

elif args.decode:
    data = args.decode
    if args.base64:
        print(base64_decode(data))
    elif args.base32:
        print(base32_decode(data))
    elif args.base16:
        print(base16_decode(data))
    elif args.base85:
        print(base85_decode(data))
    elif args.htmlencode:
        print(html_decode(data))
    elif args.urlencode:
        print(url_decode(data))
    elif args.hexencode:
        print(hex_decode(data))
    elif args.rot13encode:
        print(rot13_decode(data))
