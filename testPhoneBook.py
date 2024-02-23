import unittest

import PhoneBook


class MyTestCase(unittest.TestCase):
    def test_add_contact(self):
        PhoneBook.contacts("Donald", "09015267354")

        self.assertEqual(PhoneBook.contacts(1))
