#!/usr/bin/python3
"""Unittest for BASE
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Class TestBase"""
    def setup(self):
        """init nb"""
        Base._Base__nb_objects = 0

    def test_exist(self):
        """Function to test if class exist"""
        self.assertEqual(str(type(Base())), "<class 'models.base.Base'>")

    def test_createBase(self):
        """Function to test asign ID"""
        b1 = Base(39)
        b2 = Base()
        b3 = Base(None)
        b4 = Base(13)
        b5 = Base()
        self.assertEqual(b1.id, 39)
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 13)
        self.assertEqual(b5.id, 3)

    def test_toomucharg(self):
        """Function to test too much arguments"""
        with self.assertRaises(TypeError):
            b1 = Base(12, 12)

    def test_onlyemptybase(self):
        """Function to test only empty base"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 5)
        self.assertEqual(b2.id, 6)
        self.assertEqual(b3.id, 7)

    def test_onlyasignid(self):
        """Function to test asign id"""
        b1 = Base(39)
        b2 = Base(12)
        b3 = Base(10)
        self.assertEqual(b1.id, 39)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 10)

    def test_savefileerror(self):
        """Test for savefileerror"""
        with self.assertRaises(TypeError):
            Base.save_to_file({1, 2})

    def test_jsonstringerror(self):
        """Test for from_json_method with int."""
        with self.assertRaises(TypeError):
            Base.from_json_string(39)

    def test_jsonstringemptydict(self):
        """Test json with empty dict"""
        list_input = [{}]
        json_list_input = Base.to_json_string(list_input)
        listob = Base.from_json_string(json_list_input)
        self.assertEqual(listob, [{}])

    def test_empty_json(self):
        """tests if list is empty"""
        lis = Base.to_json_string([])
        self.assertEqual(lis, "[]")

    def test_emptydict_json(self):
        """tests for empty dict"""
        dic = Base.to_json_string([{}])
        self.assertEqual(dic, "[{}]")

    def test_nonefile(self):
        """tests for none file"""
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_from_string_set(self):
        """tests func from_json with set"""
        with self.assertRaises(TypeError) as e:
            Base.from_json_string({1, 2})

if __name__ == '__main__':
    unittest.main()
