class GoogleOcr:
    """
    This uses google vision api to pull the texts found in the image.
    """

    def __init__(self, image):
        self.image = image