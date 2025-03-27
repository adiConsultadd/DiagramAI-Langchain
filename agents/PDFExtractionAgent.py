import pdfplumber

class PDFExtractionAgent():        
    def extract_text(self, file_path):
        try:
            content = ""
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        # Normalize common bullet styles
                        cleaned_text = (
                            text.replace("•", "-")
                                .replace("◦", "-")
                                .replace("●", "-")
                                .replace("○", "-")
                                .replace("▪", "-")
                        )
                        content += cleaned_text + "\n\n"
            return content.strip() if content.strip() else "No text extracted."
        except Exception as e:
            return f"Failed to extract text: {str(e)}"

    def parse_pdf(self, pdf_path):
        pdf_content = self.extract_text(pdf_path)
        return pdf_content
