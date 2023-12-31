from rest_framework import routers
from django.urls import path
from learn.apps import LearnConfig
from learn.views import LessonList, LessonDetail, LessonCreate, LessonUpdate, LessonDelete, PaymentsList, \
    CourseSubscriptionCreate, CourseSubscriptionDelete, CourseViewSet, PaymentsCreate, PaymentCheckStatus, PaymentDetail

app_name = LearnConfig.name

urlpatterns = [
    path('lesson/', LessonList.as_view(), name='list'),
    path('lesson/<int:pk>/', LessonDetail.as_view(), name='detail'),
    path('lesson/create/', LessonCreate.as_view(), name='create'),
    path('lesson/<int:pk>/update/', LessonUpdate.as_view(), name='update'),
    path('lesson/<int:pk>/delete/', LessonDelete.as_view(), name='delete'),
    path('payments/', PaymentsList.as_view(), name='payments_list'),
    path('payments/create/', PaymentsCreate.as_view(), name='payments_create'),
    path('payments/<int:pk>/check/', PaymentCheckStatus.as_view(), name='payments_check'),
    path('payments/<int:pk>/', PaymentDetail.as_view(), name='payments_detail'),
    path('subscribe/', CourseSubscriptionCreate.as_view(), name='sub_create'),
    path('subscribe/<int:pk>/delete/', CourseSubscriptionDelete.as_view(), name='sub_delete'),

]

router = routers. SimpleRouter()
router.register('course', CourseViewSet)
urlpatterns += router.urls

