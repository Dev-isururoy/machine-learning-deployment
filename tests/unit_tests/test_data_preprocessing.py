import unittest
from your_module import data_preprocessing

class TestDataPreprocessing(unittest.TestCase):
    def test_clean_text(self):
        text = "This is a test sentence."
        cleaned_text = data_preprocessing.clean_text(text)
        self.assertEqual(cleaned_text, "this is a test sentence")

    def test_tokenize_text(self):
        text = "This is a test sentence."
        tokens = data_preprocessing.tokenize_text(text)
        self.assertEqual(tokens, ["this", "is", "a", "test", "sentence"])

    # Add more test methods 

if __name__ == "__main__":
    unittest.main()
