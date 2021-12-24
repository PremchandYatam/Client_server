"""This is a testcase file to perform unit testing"""
import unittest
from function_file import *

class TestFunc(unittest.TestCase):
    """TestFunc class handles all the unit tests.
    Methods:
    -----------------------
    test_login(self):
    test_write_file(self):

    """
    def test_login(self):
        """
        This performs testing for the existing users.
        TestCase1: incorrect credentials - incorrect password
        TestCase2: correct credentials
        TestCase3: correct credentials - handle multiple user test case
        TestCase4: incorrect credentials, incorrect username
        """
        given_values = [[["login", "prem", "143"], ('127.0.0.1', 62295)],
                        [["login", "prem", "1234"], ('127.0.0.1', 62296)],
                        [["login", "abcde", "123"], ('127.0.0.1', 62297)]]
        output_values = ['Login Unsuccessful-->Wrong Password', 'User Login successful',
                            'Username does not exist']
        res_list = []
        i= 0
        while i<len(given_values):
            res_list.append(sf_obj.login_func(given_values[i][0], given_values[i][1]))
            i=i+1
        self.assertListEqual(res_list, output_values)

    def test_write_file(self):
        """This performs testing during writing of the file.
        """
        given_values = [[["write_file", "tex.txt"]],
                        [["write_file", "tex.txt", "Prem is a good boy"]]]
        output_values = [' File created successfully', ' Successfully completed file writing ']
        res_list = []
        i= 0
        while i<len(given_values):
            res_list.append(sf_obj.write_file_func(given_values[i][0]))
            i=i+1
        self.assertListEqual(res_list, output_values)

if __name__ == '__main__':
    sf_obj = ServerFunction()
    unittest.main()
