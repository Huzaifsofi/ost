import docx
import PyPDF2
import re

def extract_text_from_docx(docx_file):
    text = ""
    doc = docx.Document(docx_file)
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, "rb") as f:
        reader = PyPDF2.PdfFileReader(f)
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

def extract_information_from_cv(cv_text):
    # Regular expressions for email and phone number patterns
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_regex = r'\b(?:\+\d{1,2}\s)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'

    # Extracting email addresses
    emails = re.findall(email_regex, cv_text)

    # Extracting phone numbers
    phone_numbers = re.findall(phone_regex, cv_text)

    # Removing email addresses and phone numbers from the text
    #text_without_contact_info = re.sub(email_regex, '', cv_text)
    #text_without_contact_info = re.sub(phone_regex, '', text_without_contact_info)

    return emails, phone_numbers


# Example usage
docx_file = "Sample2/AnamRehman.docx"
#pdf_file = "example.pdf"

docx_text = extract_text_from_docx(docx_file)
#pdf_text = extract_text_from_pdf(pdf_file)


emails, phone_numbers = extract_information_from_cv(docx_text)
print(emails)
print(phone_numbers)

