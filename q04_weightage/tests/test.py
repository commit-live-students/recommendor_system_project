import unittest
from inspect import getargspec
from ..build import q04_weightage as student
from greyatomlib.recommendor_system_project.q04_weightage.build import q04_weightage as original
import dill
import pandas as pd
from pandas.util.testing import assert_frame_equal


class Testing(unittest.TestCase):
    #  Check the arguements of the function
    def test_recommendor_args(self):
        # Input parameters tests
        args = getargspec(student).args
        self.assertEqual(len(args), 1, "Expected argument(s) %d, Given %d" % (1, len(args)))


    def test_return_dataframe(self):
        self.student_func = student
        self.data = 'data/subreddit-interactions-for-25000-users.zip'
        self.student_return = self.student_func(self.data)
        self.assertEqual(self.student_return.shape, (700000, 4),
                           "The return values do not match expected values")
