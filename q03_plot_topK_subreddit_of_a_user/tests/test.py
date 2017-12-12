import unittest
from inspect import getargspec
from ..build import q03_plot_topK_subreddit_of_a_user as student
from greyatomlib.recommendor_system_project.q03_plot_topK_subreddit_of_a_user.build import q03_plot_topK_subreddit_of_a_user as original
import dill
import pandas as pd
from pandas.util.testing import assert_frame_equal


class Testing(unittest.TestCase):

    #  Check the arguements of the function
    def test_recommendor_args(self):
        # Input parameters tests
        args = getargspec(student)
        self.assertEqual(len(args[0]), 3, "Expected argument(s) %d, Given %d" % (3, len(args)))

    def test_recommendor_defaults(self):
        args = getargspec(student)
        self.assertEqual(args[3], ('kabanossi',14), "Expected default values do not match given default values")

   
