import streamlit as st

def insert_multiple_files_in_html(html_file, head_txt_files, body_txt_files):
    # Read the HTML file contents
    html_lines = html_file.readlines()
    html_file.seek(0)
    
    # Read the content of each uploaded file for insertion in the <head> section
    head_meta_pixel_codes = [file.read().decode() for file in head_txt_files]
    
    # Read the content of each uploaded file for insertion in the <body> section
    body_meta_pixel_codes = [file.read().decode() for file in body_txt_files]

    # Find the index of the closing </head> and the opening <body> tags
    head_index = None
    body_index = None
    for i, line in enumerate(html_lines):
        if '</head>' in line:
            head_index = i
        if '<body>' in line:
            body_index = i

    # Insert the contents of each file right before the </head> tag
    if head_index is not None:
        for head_meta_pixel_code in head_meta_pixel_codes:
            html_lines.insert(head_index, head_meta_pixel_code + "\n")
    else:
        st.error("No </head> tag found in the HTML file.")

    # Insert the contents of each file right after the <body> tag
    if body_index is not None:
        body_insert_index = body_index + 1  # To insert after <body>
        for body_meta_pixel_code in body_meta_pixel_codes:
            html_lines.insert(body_insert_index, body_meta_pixel_code + "\n")
            body_insert_index += 1  # Move index to keep inserting the files sequentially
    else:
        st.error("No <body> tag found in the HTML file.")

    return ''.join(html_lines)

# Streamlit UI
st.title("HTML Modifier with Meta Tags")

# Step 1: Upload HTML file
html_file = st.file_uploader("Upload your HTML file", type=['html'])

# Step 2: Upload .txt files for the <head> section
head_txt_files = st.file_uploader("Upload .txt files for the <head> section", type=['txt'], accept_multiple_files=True)

# Step 3: Upload .txt files for the <body> section
body_txt_files = st.file_uploader("Upload .txt files for the <body> section", type=['txt'], accept_multiple_files=True)

# Step 4: Button to insert files and generate the modified HTML
if st.button("Generate Modified HTML"):

    if html_file and (head_txt_files or body_txt_files):
        # Process the uploaded files and modify the HTML content
        modified_html_content = insert_multiple_files_in_html(html_file, head_txt_files, body_txt_files)

        # Step 5: Provide a download link for the modified HTML
        st.download_button("Download Modified HTML", modified_html_content, "modified_file.html", "text/html")
    else:
        st.error("Please upload the HTML file and at least one .txt file.")
