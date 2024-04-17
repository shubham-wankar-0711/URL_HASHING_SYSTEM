from django.test import TestCase
from rest_framework.exceptions import ValidationError
from url_hashing_app.models import Link
from url_hashing_app.serializers import LinkSerializer
from django.test import Client
from utils.get_random_string import get_random_string


class LinkSerializerTestCase(TestCase):
    def test_validate_full_address_valid(self):
        # Create a serializer instance
        serializer = LinkSerializer()
        # Valid URL
        valid_url = 'https://portal2.passportindia.gov.in/AppOnlineProject/statusTracker/trackStatusInpNew'
        # Assert that validation passes for a valid URL
        self.assertEqual(
            serializer.validate_full_address(valid_url), valid_url)

    def test_validate_full_address_invalid(self):
        # Create a serializer instance
        serializer = LinkSerializer()
        # Invalid URL
        invalid_url = 'example.com'
        # Assert that validation raises a ValidationError for an invalid URL
        with self.assertRaises(ValidationError):
            serializer.validate_full_address(invalid_url)
