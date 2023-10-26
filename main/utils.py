# from django.core.paginator import Paginator

class DataMixin:
    paginate_by = 6

    def get_user_context(self, **kwargs):
        return kwargs