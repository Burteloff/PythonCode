from PIL import Image, ImageDraw, ImageFont
#Код для отрисовки чеков
# Define the input variables
time = "12:00 PM"
location_name = "Storde Name"
location_address = "123 Main St"
items = ["Item 1", "Item 2", "Item 3"]

# Create a blank image with the desired width and resolution
img = Image.new("RGB", (70*180, 180*180), color=(255,255,255))

# Create a drawing context
draw = ImageDraw.Draw(img)

# Define font and its size
font = ImageFont.truetype("arial.ttf", 500)

# Add the time to the image
draw.text((50, 100), time, font=font, fill=(10, 0, 0))

# Add the location name to the image
draw.text((50, 5000), location_name, font=font, fill=(0, 0, 0))

# Add the location address to the image
draw.text((50, 20000), location_address, font=font, fill=(0, 0, 0))

# Add the items to the image
y_offset = 25000
for item in items:
    draw.text((0, y_offset), item, font=font, fill=(0, 0, 0))
    y_offset += 5000

# Save the image as a PNG file
img.save("receipt.png")