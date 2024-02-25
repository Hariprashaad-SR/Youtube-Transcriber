import requests
from fpdf import FPDF
from logger import logging


# Function representing the properties of the 'report.pdf'
class PDFReport(FPDF):
    def __init__(self, channel_name, title, summary, image_url):
        self.channel_name = channel_name
        self.title = title
        self.summary = summary
        self.image_url = image_url
        super().__init__()

    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Generated by Youtube Transcriber by Hariprashaad-SR', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def chapter_image(self, image_path):
        self.image(image_path, x=10, y=None, w=160, h=90)
        self.ln()


# Function to download an image from a URL and store it locally
def download_image(url, file_name = "Assets/image.jpg"):
    logging.info('Downloading image')
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print("Image downloaded successfully.")
    else:
        print("Failed to download image. Please check the URL and try again.")


# Function to Generate 'report.pdf' 
def generate_report(channel_name, title, image_url, summary):
    logging.info('Generating report')
    
    # Adding Page
    pdf = PDFReport(channel_name, title, summary, image_url)
    pdf.add_page() 

    # Importing image
    download_image(image_url)
    
    # Adding title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, channel_name, 0, 1, 'C')
    pdf.ln(10)
   
    # Adding chapter title
    pdf.chapter_title(title)

    # Adding resized image
    pdf.chapter_image('Assets/image.jpg')

    # Adding summary
    pdf.chapter_title('Summary:')
    pdf.chapter_body(summary)

    # Generating PDF file
    pdf_output = 'Assets/report.pdf'
    logging.info('Generation Successful')
    pdf.output(pdf_output)



style =  """
            <style>
            .footer {
                position: fixed;
                bottom: 0;
                width: 100%;
                text-align: center;
                padding: 5px;
                background-color: #0E1117
                color: FAFAFA
            }
            </style>
                
        """

