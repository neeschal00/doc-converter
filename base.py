from pdf2docx import Converter
from docx2pdf import convert
import os

def pdf_to_docx(pdf_path, docx_path):
    cv = Converter(pdf_path)
    cv.convert(docx_path)
    cv.close()



def docx_to_pdf(docx_path, pdf_path):
    convert(docx_path, pdf_path)


if __name__ == "__main__":
    list_dir = os.listdir("files")
    prefix = "files\\"
    for files in list_dir:
        filename = files.replace(".pdf",".docx")
        if files.endswith(".pdf"):
            pdf_to_docx(prefix+files,prefix+filename)
