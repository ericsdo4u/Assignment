import unittest

import Class_work


class MyTestCase(unittest.TestCase):
    def test_Add_Number_To_List(self):
        first = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.assertEqual(10, Class_work.get_Length_Of_List(first))

    def test_Sum_Of_Element(self):
        first = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.assertEqual(70, Class_work.sum_All_Elemet_Of_Even(first))

    def test_Sum_Of_Element(self):
        first = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.assertEqual(75, Class_work.sum_Odd_Element(first))

    def test_multiply_Element_In_Third_Position(self):
        first = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.assertEqual(39, Class_work.multiply_Element_In_Third_Position(first))

    def test_average_Element_in_list(self):
        first = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.assertEqual(7.632, Class_work.average_Element_in_list(first))

    def test_largest_Element(self):
        first = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.assertEqual(19, Class_work.largest_Element(first))

    def test_smallest_Element(self):
        first = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.assertEqual(10, Class_work.smallest_Element(first))

    def test_Word_Count_In_A_List_Of_Word(self):
        text = ('The palace is minuts away from he village'
                ' this is sample text with several words '
                'this is more sample text with some different words ')
        self.assertEqual(17, Class_work.count_word(text))

    def test_sum_of_even_and_odd_number(self):
        sample_input = 10
        expected_output = 20, 25
        self.assertEqual(expected_output, Class_work.sum_even_and_odd_numbers(sample_input))

