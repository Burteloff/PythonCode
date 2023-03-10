import unittest
from PIL import Image
import configparser
import os
from main import ReceiptController,ReceiptModel,ReceiptView

class TestReceiptController(unittest.TestCase):
    def setUp(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.time = "12:00 PM"
        self.location_name = "Store Name"
        self.location_address = "123 Main St"

        self.width=int(self.config['image']['width'])
        self.height=int(self.config['image']['height'])
        self.color=tuple(map(int,self.config['image']['color'].split(',')))
       

        self.items = ["Item 1", "Item 2", "Item 3"]
        self.receipt_controller = ReceiptController()

    def test_create_receipt(self):
        self.receipt_controller.create_receipt(self.time, self.location_name, self.location_address, self.items)
        self.assertIsInstance(self.receipt_controller.receipt_model, ReceiptModel)
        self.assertEqual(self.receipt_controller.receipt_model.time, self.time)
        self.assertEqual(self.receipt_controller.receipt_model.location_name, self.location_name)
        self.assertEqual(self.receipt_controller.receipt_model.location_address, self.location_address)
        self.assertEqual(self.receipt_controller.receipt_model.items, self.items)
        self.assertTrue(os.path.isfile("receipt.png"))
        Image.MAX_IMAGE_PIXELS = 100000000
        img = Image.open("receipt.png")
   
        self.assertEqual(img.size, ((self.width),self.height))
        self.assertEqual(img.getpixel((0, 0)), (self.color))

class TestReceiptModel(unittest.TestCase):
    def setUp(self):
        self.time = "12:00 PM"
        self.location_name = "Store Name"
        self.location_address = "123 Main St"
        self.items = ["Item 1", "Item 2", "Item 3"]
        self.receipt_model = ReceiptModel(self.time, self.location_name, self.location_address, self.items)

    def test_receipt_model(self):
        self.assertEqual(self.receipt_model.time, self.time)
        self.assertEqual(self.receipt_model.location_name, self.location_name)
        self.assertEqual(self.receipt_model.location_address, self.location_address)
        self.assertEqual(self.receipt_model.items, self.items)
class TestReceiptView(unittest.TestCase):
    def setUp(self):
        self.receipt_model = ReceiptModel("12:00 PM", "Store Name", "123 Main St", ["Item 1", "Item 2", "Item 3"])
        self.receipt_view = ReceiptView()
        self.width=int(self.config['image']['width'])
        self.height=int(self.config['image']['height'])
        self.color=tuple(map(int,self.config['image']['color'].split(',')))

    def test_create_receipt(self):
        self.receipt_view.create_receipt(self.receipt_model)
        self.assertTrue(os.path.isfile("receipt.png"))
        Image.MAX_IMAGE_PIXELS = 100000000
        img = Image.open("receipt.png")
        
        self.assertEqual(img.size, ((self.width),self.height))
        self.assertEqual(img.getpixel((0, 0)), (self.color))