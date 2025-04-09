from django.urls import path
from .views import class_list, class_detail, create_class, attendance_list, mark_attendance

urlpatterns = [
    path('', class_list, name='class_list'),
    path('<int:session_id>/', class_detail, name='class_detail'),
    path('create/', create_class, name='create_class'),
    path('<int:session_id>/attendance/', attendance_list, name='attendance_list'),
    path('<int:session_id>/attendance/mark/', mark_attendance, name='mark_attendance'),
]
