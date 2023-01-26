class Receipt:
    def __init__(self, time, location_name, location_address, items, width=70*80, height=180*180, color=(255,255,255)):
        '''
            Initialize the class with the following parameters:
        - time: the time to be displayed on the receipt
        - location_name: the name of the location
        - location_address: the address of the location
        - items: a list of items to be displayed on the receipt
        - width: the width of the image (default: 70*180)
        - height: the height of the image (default: 180*180)
        - color: the background color of the image (default: white)
        '''
        self.time = time
        self.location_name = location_name
        self.location_address = location_address
        self.items = items
        self.width = width
        self.height = height
        self.color = color

    def create_receipt(self):
        """
        Creates a receipt image and saves it as 'receipt.png'
        """
        from PIL import Image, ImageDraw, ImageFont

        # Create a blank image with the desired width and resolution
        img = Image.new("RGB", (self.width, self.height), color=self.color)
        # Create a drawing context
        draw = ImageDraw.Draw(img)
        # Define font and its size
        font = ImageFont.truetype("arial.ttf", 500)
        # Add the time to the image
        draw.text((50, 100), self.time, font=font, fill=(10, 0, 0))
        # Add the location name to the image
        draw.text((50, 5000), self.location_name, font=font, fill=(0, 0, 0))
        # Add the location address to the image
        draw.text((50, 20000), self.location_address, font=font, fill=(0, 0, 0))
        # Add the items to the image
        y_offset = 25000
        for item in self.items:
            draw.text((0, y_offset), item, font=font, fill=(0, 0, 0))
            y_offset += 5000
        # Save the image as a PNG file
        img.save("receipt.png")

time = "12:00 PM"
location_name = "Storde Name"
location_address = "123 Main St"
items = ["Item 1", "Item 2", "Item 3"]

# Create an instance of the receipt class
receipt = Receipt(time, location_name, location_address, items)
# Call the create_receipt method to generate the image
receipt.create_receipt()