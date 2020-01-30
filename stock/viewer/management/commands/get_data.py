import sys
import os

module_parent_dir_path = os.path.abspath(os.path.join(__file__,"../../../"))  # Make all local  parallel to stock apps
sys.path.insert(1, module_parent_dir_path)    # Do not replace sys.path[0], insert just after it


from django.core.management.base import BaseCommand
from viewer.loader import run


class Command(BaseCommand):
    help = "runs data downloading"

    def handle(self, *args, **options):
        run()
