#!/usr/bin/python3
import streamlit as st
import pandas as pd
import io
from converter import vcf_to_csv


st.title('VCF to CSV Converter')
vcf_file = st.file_uploader('File uploader', type=['vcf'])
if vcf_file is not None:
    # Convert VCF to CSV
    csv_data = vcf_to_csv(vcf_file)

    # Ensure csv_data is a string or file-like object
    if isinstance(csv_data, str):
        csv_data = io.StringIO(csv_data)

    # Provide download button
    st.download_button('Download the converted file', csv_data.getvalue(),
                       file_name='converted.csv')

    # Reset the StringIO object for reading
    csv_data.seek(0)

    # Preview the data
    st.write('### Data preview:')
    preview = pd.read_csv(csv_data)
    st.write(preview)
