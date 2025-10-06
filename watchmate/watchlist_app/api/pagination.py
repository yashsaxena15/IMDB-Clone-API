from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination,CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'p' # this will change the page to p
    page_size_query_param = 'size' # using this user can get the n number of pages himself by passing ?size=page no
    max_page_size = 2 # user can't load more than 2 pages at once using this 
    last_page_strings = 'end'

class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'

class WatchListCPagination(CursorPagination):
    page_size = 5
    ordering = 'created'