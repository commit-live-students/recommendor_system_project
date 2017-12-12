import unittest
from inspect import getargspec
from ..build import q06_similarity as student
from greyatomlib.recommendor_system_project.q06_similarity.build import q06_similarity as original
import dill
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from pandas.util.testing import assert_frame_equal


class Testing(unittest.TestCase):
    def setUp(self):
        print('setup')
        with open('q06_similarity/tests/user_sol.pkl', 'wb') as f:
            dill.dump(student, f)

        with open('q06_similarity/tests/test_sol.pkl', 'wb') as f:
            dill.dump(original, f)
        with open('q06_similarity/tests/user_sol.pkl', 'rb') as f:
            self.student_func = dill.load(f)
        with open('q06_similarity/tests/test_sol.pkl', 'rb') as f:
            self.solution_func = dill.load(f)
        self.data = 'data/subreddit-interactions-for-25000-users.zip'
        self.student_return = self.student_func(self.data)
        self.original_return = self.solution_func(self.data)

    #  Check the arguements of the function
    def test_recommendor_args(self):
        # Input parameters tests
        args = getargspec(student)
        self.assertEqual(len(args[0]), 3, "Expected argument(s) %d, Given %d" % (3, len(args)))

    def test_recommendor_defaults(self):
        args = getargspec(student)
        self.assertEqual(args[3], ('subreddit',cosine_similarity), "Expected default values do not match given default values")


    def test_return_dataframe(self):
        self.student_func = student
        self.data = 'data/subreddit-interactions-for-25000-users.zip'
        self.student_return = self.student_func(self.data)
        self.assertEqual(self.student_return[0].shape, (79,79),
                           "The return values do not match expected values")

    def test_return_dataframe(self):
        self.student_func = student
        self.data = 'data/subreddit-interactions-for-25000-users.zip'
        self.student_return = self.student_func(self.data)
        self.assertEqual(self.student_return[1].shape, (13,79),
                           "The return values do not match expected values")
