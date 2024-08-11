#!/usr/bin/python3
import streamlit as st
from converter import vcf_to_csv

st.title('VCF to CSV Converter')
vcf_file = st.file_uploader('File uploader', type=['vcf'])
if vcf_file is not None:
    data = vcf_to_csv(vcf_file)
    st.download_button('Download the converted file', data, file_name='converted.csv')
