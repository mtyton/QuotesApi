import sys
import os

module_parent_dir_path = os.path.abspath(os.path.join(__file__,"../"))  # Make all local  parallel to stock apps
sys.path.insert(1, module_parent_dir_path)    # Do not replace sys.path[0], insert just after it

from rest_framework import serializers
from viewer.models import StockQuotes


class StockQuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockQuotes
        fields = '__all__'
