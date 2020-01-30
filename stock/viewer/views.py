import sys
import os

module_parent_dir_path = os.path.abspath(os.path.join(__file__,"../"))  # Make all local  parallel to stock apps
sys.path.insert(1, module_parent_dir_path)    # Do not replace sys.path[0], insert just after it


from rest_framework import viewsets
from rest_framework import filters
from viewer.models import StockQuotes
from viewer.serializers import StockQuotesSerializer


# Create your views here.
class DataView(viewsets.ReadOnlyModelViewSet):
    queryset = StockQuotes.objects.all()
    serializer_class = StockQuotesSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'code']
