class OcrFactory:

    def __init__(self, type):
        self.type = type.strip().lower()

    def get_ocr_object(self):

        if len(self.type == 0):
            raise "Type of OCR is not specified"

        if self.type == "google":
            return "google"
        elif self.type == "tesseract":
            return "tesseract"
        else:
            raise "Unsupported OCR specified"