from PIL import Image


class ImageProcessor:
    @staticmethod
    def load(path):
        return Image.open(path)