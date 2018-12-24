import anagram
import unittest


class TestAnagram(unittest.TestCase):
    def test_EqualLength(self):
        self.assertEqual(anagram.checking_off('Hello', 'Helloo'), False)

    def test_Anagram(self):
        self.assertEqual(anagram.checking_off('Heart', 'Earth'), True)

    def test_Not_Anagram(self):
        self.assertEqual(anagram.checking_off('Heart', 'aaaaa'), False)

if __name__ == '__main__':
    unittest.main()
