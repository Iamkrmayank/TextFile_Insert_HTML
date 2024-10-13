import streamlit as st

def insert_multiple_files_in_html(html_content, head_txt_contents, body_txt_contents):
    # Split the HTML content into lines
    html_lines = html_content.splitlines(keepends=True)

    # Insert head content
    head_index = None
    body_index = None
    for i, line in enumerate(html_lines):
        if '</head>' in line:
            head_index = i
        if '<body>' in line:
            body_index = i

    if head_index is not None:
        for head_meta_pixel_code in head_txt_contents:
            html_lines.insert(head_index, head_meta_pixel_code + "\n")
    else:
        st.error("No </head> tag found in the HTML file.")

    if body_index is not None:
        body_insert_index = body_index + 1
        for body_meta_pixel_code in body_txt_contents:
            html_lines.insert(body_insert_index, body_meta_pixel_code + "\n")
            body_insert_index += 1
    else:
        st.error("No <body> tag found in the HTML file.")

    modified_html_content = ''.join(html_lines)
    return modified_html_content

# Streamlit UI
st.title("HTML Modifier")

html_file = st.file_uploader("Upload an HTML file", type="html")
head_txt_files = st.file_uploader("Upload .txt files for <head>", type="txt", accept_multiple_files=True)
body_txt_files = st.file_uploader("Upload .txt files for <body>", type="txt", accept_multiple_files=True)

if st.button("Generate Modified HTML"):
    if html_file is not None:
        # Read the HTML file content
        html_content = html_file.getvalue().decode("utf-8")
        
        # Read the content of each .txt file
        head_txt_contents = [txt_file.getvalue().decode("utf-8") for txt_file in head_txt_files] if head_txt_files else []
        body_txt_contents = [txt_file.getvalue().decode("utf-8") for txt_file in body_txt_files] if body_txt_files else []
        
        # Call the function to modify the HTML content
        modified_html_content = insert_multiple_files_in_html(html_content, head_txt_contents, body_txt_contents)

        # Offer the modified content for download
        st.download_button("Download Modified HTML", modified_html_content, "modified_file.html")
    else:
        st.error("Please upload an HTML file.")
