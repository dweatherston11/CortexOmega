# test_cortexomega.py
"""
Tests for CortexOmega module.
"""

import unittest
from cortexomega import CortexOmega

class TestCortexOmega(unittest.TestCase):
    """Test cases for CortexOmega class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CortexOmega()
        self.assertIsInstance(instance, CortexOmega)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CortexOmega()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
