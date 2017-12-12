import unittest
from inspect import getargspec
from ..build import q01_Unique_users_subreddit as student
from greyatomlib.recommendor_system_project.q01_Unique_users_subreddit.build import q01_Unique_users_subreddit as original
import dill
import pandas as pd
from pandas.util.testing import assert_frame_equal


class Testing(unittest.TestCase):

    #  Check the arguements of the function
    def test_recommendor_args(self):
        # Input parameters tests
        args = getargspec(student)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args)))


    def test_recommendor_default(self):
        args = getargspec(student)
        self.assertEqual(args[3], (None), "Expected default values do not match given default values")

    def test_dataframe(self):
        self.student_func = student
        self.data = 'data/subreddit-interactions-for-25000-users.zip'
        self.student_return = self.student_func(self.data)
        self.assertEqual(self.student_return[0].shape, (700000, 3), "The return values is not a DataFrame")



    def test_return(self):
        self.student_func = student
        self.data = 'data/subreddit-interactions-for-25000-users.zip'
        self.student_return = self.student_func(self.data)
        self.assertEqual(self.student_return[1], 21376, "The return values do not match expected values")


    def test_return_2(self):
        self.student_func = student
        self.data = 'data/subreddit-interactions-for-25000-users.csv.zip'
        self.student_return = self.student_func(self.data)
        self.original_return = self.solution_func(self.data)
        self.assertEqual(self.student_return[2], 14111, "The return values do not match expected values")

