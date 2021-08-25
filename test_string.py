#!/usr/bin/env python

import unittest
from stringcheck import quote_check,number_check,misplaced_period_check,period_check,caps_check

class TestString(unittest.TestCase):

    def test_captials(self):            #UNIT TEST FOR CAPTIAL CHECK FUNCTION
        valid_sentence = caps_check(r'''The quick brown fox said “hello Mr lazy dog”.''')
        self.assertEqual(valid_sentence, "Test Passed")
        invalid_sentence = caps_check(r'''the quick brown fox said “hello Mr lazy dog".''')
        self.assertEqual(invalid_sentence, "Test Failed")

    def test_period(self):          #UNIT TEST FOR PERIOD AT END OF STRING CHECK FUNCTION
        valid_sentence = period_check(r'''The quick brown fox said hello Mr lazy dog.''')
        self.assertEqual(valid_sentence, "Test Passed")
        invalid_sentence  = period_check(r'''The quick brown fox said "hello Mr. lazy dog"''')
        self.assertEqual(invalid_sentence, "Test Failed")

    def test_mis_period(self):          #UNIT TEST FOR MISPLACED PERIOD IN STRING FUNCTION
        valid_sentence = misplaced_period_check(r'''One lazy dog is too few, 13 is too many.''')
        self.assertEqual(valid_sentence, "Test Passed")
        invalid_sentence = misplaced_period_check(r'''The quick brown fox said "hello Mr. lazy dog".''')
        self.assertEqual(invalid_sentence, "Test Failed")

    def test_number(self):              # UNIT TEST FOR < 13 NUMBER CHECK FUNCTION
        valid_sentence = number_check(r'''One lazy dog is too few, thirteen is too many.''')
        self.assertEqual(valid_sentence, "Test Passed")
        invalid_sentence = number_check(r'''One lazy dog is too few, 12 is too many.''')
        self.assertEqual(invalid_sentence, "Test Failed")

    def test_quote(self):           #UNIT TEST FOR EVEN AMOUNT OF QUOTES USED IN STRING FUNCTION
        valid_sentence = quote_check(r'''The quick brown fox said hello "Mr lazy dog".''')
        self.assertEqual(valid_sentence, "Test Passed")
        invalid_sentence = quote_check(r'''The quick" brown fox said "hello Mr lazy dog."''')
        self.assertEqual(invalid_sentence, "Test Failed")

if __name__ == '__main__':
    unittest.main()
