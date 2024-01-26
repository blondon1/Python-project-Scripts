from pathlib import Path
from PyPDF2 import PdfReader


def convert_pdf_to_txt(pdf_path: Path) -> None:
    # Check if provided PDF file exists
    if not pdf_path.is_file():
        print('Error! File Not Found!')
        return None
    print('PDF Found! Attempting Conversion...')
    
    # Exception Handling during Data Extraction from PDF File
    try:
        # Define .txt file which will contain the extracted data 
        # Extracting Data from PDF file page-by-page and storing in TXT file
        pdf_reader = PdfReader(str(pdf_path))
        with out_filename.open('w', encoding='utf-8') as extracted_data:
            for page in pdf_reader.pages:
                text = page.extract_text() or ''  # Fallback to empty string if None
                extracted_data.write(text)
        
    # If any Error is encountered, Print the Error on Screen
    except Exception as e:
        print(f'Error Converting PDF to Text or Saving Converted Text into .txt file: {e}')
        return None


def main():
    filename = input("Enter the path to the PDF file: ")
    pdf_path = Path(filename)
    convert_pdf_to_txt(pdf_path)

if __name__ == "__main__":
    main()
