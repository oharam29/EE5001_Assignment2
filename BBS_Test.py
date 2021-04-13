import unittest

from BBS import *

class BBS_Test(unittest.TestCase):
    def compare_runs(x1, x2):
        print("Same number of 1s?:", x1[1] == x2[1])