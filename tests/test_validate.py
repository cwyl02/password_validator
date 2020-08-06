from unittest import TestCase
# from password_validator import validate
from password_validator.validate import *
import os


class TestValidate(TestCase):

    def test_validate_length_pw_short(self):
        pw_short = '0ab'
        self.assertEqual((False, 3), validate_length(pw_short))

    def test_validate_length_pw_long(self):
        pw_long = '0'*666
        self.assertEqual((False, 666), validate_length(pw_long))

    def test_validate_length_pw_ok(self):
        pw_len_ok = 'abcnd@S123s'
        self.assertEqual((True, None), validate_length(pw_len_ok))

    def test_validate_charset_pw_nonascii(self):
        pw_nonascii = '1Sf5😄7fSD密@@码'
        self.assertEqual((False, '1Sf5*7fSD*@@*'), validate_charset(pw_nonascii))

    def test_validate_charset_pw_validascii(self):
        pw_nonascii = '1Sf57fSD@@'
        self.assertEqual((True, None), validate_charset(pw_nonascii))

    def test_validate_common_pw_1(self):
        pw_ez = '1234567'
        # validate_common_pw returns False when the pw shows up in the common password list
        self.assertFalse(validate_common_pw(set(['1234567', 'pointer', 'hello', 'paul']), pw_ez))
