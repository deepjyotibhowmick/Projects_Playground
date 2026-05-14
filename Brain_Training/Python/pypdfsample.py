import os
from os import getcwd

from pypdf import PdfReader
from PyPDF2 import PdfMerger

fpath="E:\python\code_2023\pic"
os.chdir(fpath)
reader = PdfReader("File19.pdf")
print(f"total number of pages in the pdf file : {len(reader.pages)}")
page =reader.pages[0]
text = page.extract_text()

# print(page)
print(text)

pdfmerge = PdfMerger()

# pdf_files = ["File10.pdf","File11.pdf","File19.pdf"]
pdf_files = [pdf for pdf in os.listdir() if pdf.endswith(".pdf")]
print(pdf_files)
print("merging started..")
for pdf in pdf_files:
    pdfmerge.append(pdf)

pdfmerge.write("MergedFile.pdf")
pdfmerge.close()

print("Merge completed")