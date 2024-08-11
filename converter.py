#!/usr/bin/python3
import csv
import re
import io
import quopri
"""
This module provides functions to decode quoted-printable strings,
parse vCard data, and convert VCF (vCard File) files to CSV format.
"""


def decode_quoted_printable(string):
    """
    Decodes a quoted-printable encoded string.

    Args:
        string: The quoted-printable encoded string.

    Returns:
        The decoded string.
    """
    try:
        # Attempt to decode using UTF-8
        return quopri.decodestring(string.encode('utf-8')).decode('utf-8')
    except UnicodeDecodeError:
        try:
            # Fallback to ISO-8859-1 if UTF-8 decoding fails
            return quopri.decodestring(string.encode('utf-8')).decode('iso-8859-1')
        except:
            # Return the original string if decoding fails
            return string


def parse_vcard(vcard):
    """
    Parses a vCard string to extract the name and phone number.

    Args:
        vcard: The vCard string.

    Returns:
        A tuple containing the name and phone number.
    """
    name = 'Unknown'
    phone = ''
    for line in vcard.splitlines():
        if line.startswith('FN'):
            # Extract and decode the full name
            encoded_name = line.split(':', 1)[1].strip()
            name = decode_quoted_printable(encoded_name)
        elif line.startswith('TEL'):
            # Extract the phone number
            phone = line.split(':', 1)[1].strip()
    return name, phone


def vcf_to_csv(vcf_file):
    """
    Converts a VCF file to CSV format.

    Args:
        vcf_file: A file-like object or file path containing VCF data.

    Returns:
        A string containing the CSV formatted data.
    """
    # Read the content of the VCF file
    if isinstance(vcf_file, io.BytesIO):
        content = vcf_file.getvalue().decode('utf-8', errors='ignore')
    else:
        with open(vcf_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

    # Split the content into individual vCards
    vcards = re.split('BEGIN:VCARD', content)[1:]

    # Initialize a StringIO object to hold CSV data
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Name', 'Phone Number'])

    # Parse each vCard and write the extracted data to the CSV
    for vcard in vcards:
        name, phone = parse_vcard(vcard)
        if phone:
            writer.writerow([name, phone])

    return output.getvalue()
