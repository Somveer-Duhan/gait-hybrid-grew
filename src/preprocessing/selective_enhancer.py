from PIL import Image, ImageOps, ImageFilter

class SelectiveEnhancer:
    def __init__(self):
        pass

    def enhance(self, image: Image.Image):
        # convert to grayscale
        img = image.convert('L')
        # apply lightweight contrast enhancement
        img = ImageOps.autocontrast(img)
        # sharpen slightly
        img = img.filter(ImageFilter.SHARPEN)
        return img
