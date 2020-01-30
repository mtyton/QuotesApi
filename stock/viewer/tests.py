import sys
import os

module_parent_dir_path = os.path.abspath(os.path.join(__file__,"../"))  # Make all local  parallel to stock apps
sys.path.insert(1, module_parent_dir_path)    # Do not replace sys.path[0], insert just after it


from django.test import TestCase
from viewer.loader import Loader


# Create your tests here.
class TestLoader(TestCase):
    def setUp(self):
        self.loader = Loader()

    def test_get_courses(self):
        self.loader.get_courses()
