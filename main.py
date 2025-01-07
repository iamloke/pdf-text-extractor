import pdfplumber

def extract_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        
        for page in pdf.pages:
            text += page.extract_text()
            
    return text

if __name__ == "__main__":
    text = extract_text("input/example.pdf")
    with open("output/extracted_text.txt", "w") as f:
        f.write(text)
