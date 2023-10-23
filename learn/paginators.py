from rest_framework.pagination import PageNumberPagination


class LessonPaginator(PageNumberPagination):
    page_size = 5
    page_query_param = "page_size"
    max_page_size = 10


class CoursePaginator(PageNumberPagination):
    page_size = 2
    page_query_param = "page_size"
    max_page_size = 5
