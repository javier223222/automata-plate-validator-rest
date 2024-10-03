import pandas as pd 
from docx import Document
from bs4 import BeautifulSoup


def read_file(file_path):
    try:
        if file_path.filename.endswith('.xlsx') or file_path.filename.endswith('.csv'):
            
            return pd.read_excel(file_path.file,header=None) if file_path.filename.endswith('.xlsx') else pd.read_csv(file_path.file,header=None)
        elif file_path.filename.endswith('.docx'):
        
            return read_docx(file_path.file)
        elif file_path.filename.endswith('.html'):
            return read_html(file_path.file)
        else:
            raise ValueError('Unsupported file format')
    except Exception as e:
        raise ValueError(str(e))
    

def read_docx(file_path):
    try: 
        
        doc = Document(file_path)
        return [p.text for p in doc.paragraphs if p.text]
    
    except Exception as e:
        raise ValueError(str(e))
   

def read_html(file_path):
    try:
        content = file_path.read().decode('utf-8')
        lines = content.splitlines()  
        return lines

    except Exception as e:
        raise ValueError(str(e))