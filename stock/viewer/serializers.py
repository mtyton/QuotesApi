import sys
import os

module_parent_dir_path = os.path.abspath(os.path.join(__file__,"../"))  # Make all local  parallel to stock apps
sys.path.insert(1, module_parent_dir_path)    # Do not replace sys.path[0], insert just after it

from rest_framework import serializers, fields
from viewer.models import StockQuotes


class StockQuotesSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(StockQuotesSerializer, self).__init__(*args, **kwargs)
        self.fields['date'].format="%Y-%m-%d - %H:%M:%S"  # simply setting better way of date display

    class Meta:
        model = StockQuotes
        fields = ['name', 'code', 'price', 'date']
