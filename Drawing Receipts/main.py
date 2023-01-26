import configparser
from PIL import Image, ImageDraw, ImageFont

class ReceiptView:
    def __init__(self):
        # Read the config file
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Get the image configuration
        self.image_width = int(config.getint('image', 'width'))
        self.image_height = int(config.getint('image', 'height'))
        self.image_color = tuple(map(int, config.get('image', 'color').split(',')))

        # Get the font configuration
        self.font_name = config.get('font', 'name')
        self.font_size = config.getint('font', 'size')

    def create_receipt(self, receipt_model):
        """
        Creates a receipt image and saves it as 'receipt.png'
        """
        # Create a blank image with the desired width and resolution
        img = Image.new("RGB", (self.image_width, self.image_height), color=self.image_color)
        # Create a drawing context
        font = ImageFont.truetype(self.font_name, self.font_size)
        draw = ImageDraw.Draw(img)
        # Add the time to the image
        draw.text((0.1 * img.width, 0.01 * img.height), receipt_model.time, font=font, fill=(10, 0, 0))
        # Add the location name to the image
        draw.text((0.1 * img.width, 0.03 * img.height), receipt_model.location_name, font=font, fill=(0, 0, 0))
        # Add the location address to the image
        draw.text((0.1 * img.width, 0.05 * img.height), receipt_model.location_address, font=font, fill=(0, 0, 0))
        # Add the items to the image
        y_offset = 0.07 * img.height
        for item in receipt_model.items:
            draw.text((0.1 * img.width, y_offset), item, font=font, fill=(0, 0, 0))
            y_offset += 0.02 * img.height
        # Save the image as a PNG file
        img.save("receipt.png")
    
class ReceiptModel:
    def __init__(self, time, location_name, location_address, items):
        self.time = time
        self.location_name = location_name
        self.location_address = location_address
        self.items = items

class ReceiptController:
    def __init__(self):
        self.receipt_model = None
        self.receipt_view = None

    def create_receipt(self, time, location_name, location_address, items):
        self.receipt_model = ReceiptModel(time, location_name, location_address, items)
        self.receipt_view = ReceiptView()
        self.receipt_view.create_receipt(self.receipt_model)

if __name__ == "__main__":
    time = "12:00 PM"
    location_name = "Store Name"
    location_address = "123 Main St"
    items = ["Item 1", "Item 2", "Item 3"]
    receipt_controller = ReceiptController()
    receipt_controller.create_receipt(time, location_name, location_address, items)
    print("Receipt created and saved as 'receipt.png'")