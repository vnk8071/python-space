import pdf2printer


# Function to read data from a file
def read_from_file(document_path):
    with open(document_path, "rb") as file:
        document_data = file.read()
    return document_data


# Function to print a PDF document
def print_document(document_path):
    document = read_from_file(document_path)
    printer = pdf2printer.PdfFilePrinter()

    try:
        printer.print_document(document)
    except Exception as e:
        print(f"Error printing document: {e}")


# Example usage
pdf_document_path = "path/to/your/document.pdf"

try:
    print_document(pdf_document_path)
except Exception as e:
    print(f"Error printing PDF document: {e}")


# Function to read data from a text file
def read_from_file(document_path):
    with open(document_path, "r") as file:
        document_data = file.read()
    return document_data


# Function to print a text document
def print_document(document_path):
    document = read_from_file(document_path)
    print_file(document)


# Function to print a text document
def print_file(document):
    print(document)


# Example usage
text_document_path = "path/to/your/document.txt"

try:
    print_document(text_document_path)
except Exception as e:
    print(f"Error printing text document: {e}")
