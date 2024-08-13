# VCF to CSV Converter

## The Story Behind This Project

I encountered an issue with my phone display glitching, and I couldn't find a convenient way to back up my contacts. When I tried the export option, it gave me a contact.vcf file. I wasn't sure how to extract the information from the file. Online converters didn't work, and when I opened the contact.vcf in VSCode, it wasn't readable. However, I realized there was a way to make it work, and that's how this project came to be.

This project provides a web-based tool to convert VCF (vCard File) files into CSV format. It's built using Python with Streamlit for the web interface and includes custom logic for parsing and converting vCard data.

## Features

- Upload VCF files through a user-friendly web interface
- Convert VCF files to CSV format
- Download the converted CSV file
- Preview the converted data directly in the browser

## Usage

You have two options to use this VCF to CSV Converter:

### Option 1: Use the Hosted Version

You can access the hosted version of this tool directly through Streamlit by visiting:

[https://vcf-converter.streamlit.app](https://vcf-converter.streamlit.app)
![VCF to CSV Converter demo](./img/Screenshot%20(48).png)



This option requires no installation and can be used immediately in your web browser.

### Option 2: Run Locally

To run the application on your local machine, follow the installation instructions below.

## Installation (for local use)

To run this project locally, you need Python 3.6 or later. Follow these steps to set up the project:

1. Clone this repository:
   ```
   git clone https://github.com/sanotogii/VCF-converter.git
   cd VCF-converter
   ```

2. Install the required dependencies:
   ```
   pip install streamlit pandas
   ```

3. Start the application:
   ```
   streamlit run main.py
   ```

4. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

## How to Use

For both the hosted version and local installation:

1. Click on the "File uploader" button to select your VCF file.
2. Once the file is uploaded, the application will automatically convert it to CSV format.
3. Click the "Download the converted file" button to download the CSV file.
4. A preview of the converted data will be displayed on the page.

## Project Structure

- `main.py`: Contains the Streamlit web application code.
- `converter.py`: Includes the core logic for parsing VCF files and converting them to CSV format.

## Dependencies

- streamlit
- pandas

## Contributing

Contributions to improve the project are welcome. Please feel free to submit a Pull Request.

## Contact

Khalid LAZRAG

Email: khalidlazrag.contact@gmail.com