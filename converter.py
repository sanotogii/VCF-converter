#!/usr/bin/python3
import csv
import re
import io
import quopri

def decode_quoted_printable(string):
    try:
        return quopri.decodestring(string.encode('utf-8')).decode('utf-8')
    except UnicodeDecodeError:
        try:
            return quopri.decodestring(string.encode('utf-8')).decode('iso-8859-1')
        except:
            return string

def parse_vcard(vcard):
    name = 'Unknown'
    phone = ''
    for line in vcard.splitlines():
        if line.startswith('FN'):
            encoded_name = line.split(':', 1)[1].strip()
            name = decode_quoted_printable(encoded_name)
        elif line.startswith('TEL'):
            phone = line.split(':', 1)[1].strip()
    return name, phone

def vcf_to_csv(vcf_file):
    if isinstance(vcf_file, io.BytesIO):
        content = vcf_file.getvalue().decode('utf-8', errors='ignore')
    else:
        with open(vcf_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

    vcards = re.split('BEGIN:VCARD', content)[1:]

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Name', 'Phone Number'])

    for vcard in vcards:
        name, phone = parse_vcard(vcard)
        if phone:
            writer.writerow([name, phone])

    return output.getvalue()
