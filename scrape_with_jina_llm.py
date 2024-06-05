from docx import Document
import requests

def jinaai_readerapi_web_scraper(url):
    response = requests.get('https://r.jina.ai/'+url)
    return response.text

def save_to_doc(content, filename):
    doc = Document()
    doc.add_paragraph(content)
    doc.save(filename)
    
url = 'https://databankfiles.worldbank.org/public/ddpext_download/GDP.pdf'

data = jinaai_readerapi_web_scraper(url)

save_to_doc(data,'output.docx')
print('Data saved to output.docx')