# from django.core.paginator import Paginator

from .models import Article

class DataMixin:
    paginate_by = 6