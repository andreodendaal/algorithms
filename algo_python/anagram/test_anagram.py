import anagram
import unittest


class TestAnagramCheckingOff(unittest.TestCase):
    def test_EqualLength(self):
        self.assertEqual(anagram.checking_off('Hello', 'Helloo'), False)

    def test_Anagram(self):
        self.assertEqual(anagram.checking_off('Heart', 'Earth'), True)

    def test_Not_Anagram(self):
        self.assertEqual(anagram.checking_off('Heart', 'aaaaa'), False)


class TestAnagramSorting(unittest.TestCase):
    def test_EqualLength(self):
        self.assertEqual(anagram.sorting('Hello', 'Helloo'), False)

    def test_Anagram(self):
        self.assertEqual(anagram.sorting('Heart', 'Earth'), True)

    def test_Not_Anagram(self):
        self.assertEqual(anagram.sorting('Heart', 'aaaaa'), False)

    def test_Length(self):
        self.assertEqual(anagram.sorting('aa', 'aaa'), False)


class TestAnagramGivenSolution1(unittest.TestCase):
    def test_EqualLength(self):
        self.assertEqual(anagram.anagramSolution1('Hello', 'Helloo'), False)

    def test_Anagram(self):
        self.assertEqual(anagram.anagramSolution1('Heart', 'Earth'), True)

    def test_Not_Anagram(self):
        self.assertEqual(anagram.anagramSolution1('Heart', 'aaaaa'), False)

    def test_Length(self):
        self.assertEqual(anagram.anagramSolution1('aa', 'aaa'), False)


if __name__ == '__main__':
    unittest.main()
