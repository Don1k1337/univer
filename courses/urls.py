from django.urls import path
from . import views


urlpatterns = [
    path('', views.CourseListView.as_view(),
         name='course-list'),
    path('create', views.CourseCreateView.as_view(),
         name='course-create'),
          path('courses/<int:pk>', views.CourseDetailView.as_view(),
         name='course-detail'),
]


