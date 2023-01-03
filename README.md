# html-to-image
Simple and easy HTML to Image CLI converter made in Python

# Usage
To use this tool, you will need to have WeasyPrint and Ghostscript installed. You can install these libraries using pip:

`
pip install weasyprint
`
`
pip install ghostscript
`

Once you have these libraries installed, you can run the tool by passing in the path to the HTML file and the desired image file path as command line arguments:

`python html_to_image.py html_file_path image_file_path
`

For example, if your HTML file is located at "C:/Users/User/Documents/example.html" and you want to save the image as "C:/Users/User/Documents/example.jpg", you would run the following command:

`python html_to_image.py "C:/Users/User/Documents/example.html" "C:/Users/User/Documents/example.jpg"
`

