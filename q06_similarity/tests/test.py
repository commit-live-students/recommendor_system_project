import unittest
from inspect import getfullargspec
from build import q06_similarity
import dill
import pandas as pd
from pandas.util.testing import assert_frame_equal


class Testing(unittest.TestCase):
    def setUp(self):
        print('setup')
        with open('user_sol.pkl', 'wb') as f:
            dill.dump(q06_similarity, f)

        with open('test_sol.pkl', 'wb') as f:
            dill.dump(q06_similarity, f)
        with open('user_sol.pkl', 'rb') as f:
            self.student_func = dill.load(f)
        with open('test_sol.pkl', 'rb') as f:
            self.solution_func = dill.load(f)
        self.data = 'data/reddit_data.csv'
        self.student_return = self.student_func(self.data)
        self.original_return = self.solution_func(self.data)

    #  Check the arguements of the function
    def test_args(self):

        self.args_student = getfullargspec(self.student_func).args
        self.args_original = getfullargspec(self.solution_func).args
        self.assertEqual(len(self.args_student), len(self.args_original),
                         "Expected argument(s) %d, Given %d" % (len(self.args_original), len(self.args_student)))

        # check the defaults of the function

    def test_defaults(self):
        self.defaults_student = getfullargspec(self.student_func).defaults
        self.defaults_solution = getfullargspec(self.solution_func).defaults
        self.assertEqual(self.defaults_student, self.defaults_solution,
                         "Expected default values do not match given default values")

    def test_return_dataframe(self):
        assert_frame_equal(self.student_return[0], self.original_return[0],
                           obj="The return values do not match expected values")

    def test_return_dataframe(self):
        assert_frame_equal(self.student_return[1], self.original_return[1],obj="The return values do not match expected values")


