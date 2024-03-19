"""Integration testing for logger.py and the get_icon function in views.py"""
from django.test import TestCase  # A subclass of unittest.TestCase
from litereview.views import Icon


class TestMediaIcon(TestCase):
    """Tests for the get_icon function in view.py"""
    def setUp(self):
        self.icon = Icon()

    def test_icon(self):
        """Test if the correct string/link is returned"""
        self.assertIn(self.icon.get_media_icon("MOV"), "../static/icons/MOV.png")
        self.assertIn(self.icon.get_media_icon("BOK"), "../static/icons/BOK.png")
        self.assertIn(self.icon.get_media_icon("MGA"), "../static/icons/MGA.png")
        self.assertIn(self.icon.get_media_icon("TVS"), "../static/icons/TVS.png")
        self.assertIn(self.icon.get_media_icon("MUS"), "../static/icons/MUS.png")
        self.assertIn(self.icon.get_media_icon("COM"), "../static/icons/COM.png")

    def test_return_type(self):
        """Test that the function returns a string"""
        self.assertIsInstance(self.icon.get_media_icon("MOV"), str)

    def test_input_type_error(self):
        """
        Test that the function raises a TypeError
        when the input parameter is not a string
        """
        with self.assertRaises(TypeError):
            self.icon.get_media_icon(1)

    def test_input_key_error(self):
        """
        Test that the function raises a KeyError
        when the input parameter is not a valid media type
        """
        with self.assertRaises(KeyError):
            self.icon.get_media_icon("ANI")

    def test_logging(self):
        """Test that the logger works correctly"""
        self.icon.get_media_icon("MOV")
        log = self.icon.logger.get_last_log()
        self.assertIn("Retrieved link to icon for media type MOV = ../static/icons/MOV.png", log)
