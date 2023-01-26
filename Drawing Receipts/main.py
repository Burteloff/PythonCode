class ReceiptView:
    def __init__(self, width=70*80, height=180*180, color=(255,255,255)):
        self.width = width
        self.height = height
        self.color = color

    def create_receipt(self, receipt_model):
        """
        Creates a receipt image and saves it as 'receipt.png'
        """
        from PIL import Image, ImageDraw, ImageFont

        # Create a blank image with the desired width and resolution
        img = Image.new("RGB", (self.width, self.height), color=self.color)
        # Create a drawing context
        font = ImageFont.truetype("arial.ttf", 500)
        draw = ImageDraw.Draw(img)
        # Add the time to the image
        draw.text((50, 100), receipt_model.time, font=font, fill=(10, 0, 0))
        # Add the location name to the image
        draw.text((50, 5000), receipt_model.location_name, font=font, fill=(0, 0, 0))
        # Add the location address to the image
        draw.text((50, 20000), receipt_model.location_address, font=font, fill=(0, 0, 0))
        # Add the items to the image
        y_offset = 25000
        for item in receipt_model.items:
            draw.text((0, y_offset), item, font=font, fill=(0, 0, 0))
            y_offset += 5000
        # Save the image as a PNG file
        img.save("receipt.png")


class ReceiptModel:
    def __init__(self, time, location_name, location_address, items):
        self.time = time
        self.location_name = location_name
        self.location_address = location_address
        self.items = items


class ReceiptController:
    def init(self):
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