import unittest
import os
from seminar_test.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()
        print("現在のpath:"+path)
        self.printer = CSVPrinter("sample2.csv")
        self.lines = self.printer.read()

    def test_read1(self):
        print(self.lines)
        self.assertEqual(3, len(self.lines))

    def test_read2(self):
        all_list = [value for line_value in self.lines for value in line_value]
        print(all_list)
        for line in self.lines:
            self.assertEqual(3, len(line))
        for value in all_list:
            self.assertTrue(value)

    def test_read3(self):
        try:
            printer = CSVPrinter("not_exist.csv")
            printer.read()
            unittest.TestCase.fail("This line should not be invoked")
        except FileNotFoundError as e:
            print("Detail:", e)
