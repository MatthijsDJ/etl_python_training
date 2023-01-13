import unittest
from unittest.mock import Mock
import etl.genrator

def test_names():
    with unittest.patch(etl.genrator.generator) as mock_generator:
        mock_generator.return_value = ('Matthijs', 'de Jong')
        # Call the function
        etl.genrator