# Streamlit HTML Modifier

A simple Streamlit application that allows users to upload an HTML file and multiple `.txt` files to insert meta tags in the `<head>` and `<body>` sections of the HTML. The modified HTML file can then be downloaded for use.

## Features

- Upload an HTML file.
- Upload multiple `.txt` files for the `<head>` section.
- Upload multiple `.txt` files for the `<body>` section.
- Generate a modified HTML file with the inserted meta tags.
- Download the modified HTML file.

## Technologies Used

- [Streamlit](https://streamlit.io/) - A Python library for creating web applications.
- Python - The programming language used for developing the application.

## Installation

To run this application locally, you will need to have Python installed. Follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Iamkrmayank/TextFile_Insert_HTML.git
   cd TextFile_Insert_HTML
   
2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
  
3. **Install the required package**
    ```bash
    pip install -r requirements.txt

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py

# Usage
  Upload your HTML file using the file uploader.
  Upload one or more .txt files for the <head> section.
  Upload one or more .txt files for the <body> section.
  Click the Generate Modified HTML button.
  Download the modified HTML file by clicking the download button.
  Contributing
  If you would like to contribute to this project, please fork the repository and create a pull request with your changes.

# License
  This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
  Thanks to the Streamlit community for their support and inspiration.


