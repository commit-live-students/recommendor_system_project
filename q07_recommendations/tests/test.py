import unittest
from inspect import getargspec
from ..build import q07_recommendations as student
from greyatomlib.recommendor_system_project.q07_recommendations.build import q07_recommendations as original
from sklearn.metrics.pairwise import cosine_similarity
import dill
import pandas as pd
from pandas.util.testing import assert_frame_equal


class Testing(unittest.TestCase):
    def setUp(self):
        print('setup')
        self.data = 'data/subreddit-interactions-for-25000-users.zip'
        self.student_return = student(self.data)
        self.original_return = original(self.data)

    #  Check the arguements of the function
    def test_recommendor_args(self):
        # Input parameters tests
        args_student = getargspec(student)
        args_original = getargspec(original)
        self.assertEqual(len(args_student[0]), len(args_original[0]), "Expected argument(s) %d, Given %d" % (len(args_student[0]), len(args_original[0])))

    def test_recommendor_defaults(self):
        args_student_default = getargspec(student)
        args_original_default = getargspec(original)
        self.assertEqual(args_student_default[3], args_original_default[3], "Expected default values do not match given default values")




    def test_return(self):
        print('not a tuple')
        self.assertEqual(self.student_return, self.original_return, "The return values do not match expected values")
