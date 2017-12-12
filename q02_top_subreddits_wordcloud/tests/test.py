import unittest
from inspect import getargspec
from ..build import q02_top_subreddits_wordcloud as student
from greyatomlib.recommendor_system_project.q02_top_subreddits_wordcloud.build import q02_top_subreddits_wordcloud as original
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

