import unittest
from inspect import getargspec
from build import q01_Unique_users_subreddit as student
from greyatomlib.recommendor_system_project.q01_Unique_users_subreddit.build import q01_Unique_users_subreddit as original
import dill
import pandas as pd
from pandas.util.testing import assert_frame_equal


class Testing(unittest.TestCase):
    def setUp(self):
        print('setup')
        with open('q01_Unique_users_subreddit/tests/user_sol.pkl', 'wb') as f:
            dill.dump(student, f)

        with open('q01_Unique_users_subreddit/tests/test_sol.pkl', 'wb') as f:
            dill.dump(original, f)
        with open('q01_Unique_users_subreddit/tests/user_sol.pkl', 'rb') as f:
            self.student_func = dill.load(f)
        with open('q01_Unique_users_subreddit/tests/test_sol.pkl', 'rb') as f:
            self.solution_func = dill.load(f)
        self.data = 'data/subreddit-interactions-for-25000-users.zip'
        self.student_return = self.student_func(self.data)
        self.original_return = self.solution_func(self.data)

    #  Check the arguements of the function
    def test_polynomial(self):
        # Input parameters tests
        args = getargspec(student)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args)))
        self.assertEqual(args[3], (None), "Expected default values do not match given default values")

    
    def test_return_dataframe(self):
        assert_frame_equal(self.student_return[0], self.original_return[0],
                           obj="The return values do not match expected values")

    def test_return(self):
        print('not a tuple')
        self.assertEqual(self.student_return[1], self.original_return[1], "The return values do not match expected values")
    
    def test_return_2(self):
        print('not a tuple')
        self.assertEqual(self.student_return[2], self.original_return[2], "The return values do not match expected values")
  

