import unittest

from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
	    self.assertEqual(english_to_french(""),"") # Test for the translation of the word Hello and Bonjour

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
	    self.assertEqual(french_to_english(""),"") # Test for the translation of the word Hello and Bonjour

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
	    self.assertEqual(english_to_french("Hello"),"Bonjour") # Test for the translation of the word Hello and Bonjour

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self):
	    self.assertEqual(french_to_english("Bonjour"),"Hello") # Test for the translation of the word Bonjour and Hello

unittest.main()