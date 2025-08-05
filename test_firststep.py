# test_firststep.py
"""
Tests for FirstStep module.
"""

import unittest
from firststep import FirstStep

class TestFirstStep(unittest.TestCase):
    """Test cases for FirstStep class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FirstStep()
        self.assertIsInstance(instance, FirstStep)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FirstStep()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
