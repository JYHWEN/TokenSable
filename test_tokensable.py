# test_tokensable.py
"""
Tests for TokenSable module.
"""

import unittest
from tokensable import TokenSable

class TestTokenSable(unittest.TestCase):
    """Test cases for TokenSable class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = TokenSable()
        self.assertIsInstance(instance, TokenSable)

    def test_run_method(self):
        """Test the run method."""
        instance = TokenSable()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
