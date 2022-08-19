from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from . import views
from .models import Standard, Subject, Lesson, Comment
import base

app_name = 'curriculum'


class StandardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Standard
        fields = "__all__"


class StandardViewSet(viewsets.ModelViewSet):
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer


router = routers.DefaultRouter()
router.register(r'users', StandardViewSet)


urlpatterns = [
    path('', views.StandardListView.as_view(), name='standard_list'),
    path('<slug:slug>/', views.SubjectListView.as_view(), name='subject_list'),
    path('<str:standard>/<slug:slug>/',
         views.LessonListView.as_view(), name='lesson_list'),
    path('<str:standard>/<str:slug>/create/',
         views.LessonCreateView.as_view(), name='lesson_create'),
    path('<str:standard>/<str:subject>/<slug:slug>/',
         views.LessonDetailView.as_view(), name='lesson_detail'),
    path('<str:standard>/<str:subject>/<slug:slug>/update/',
         views.LessonUpdateView.as_view(), name='lesson_update'),
    path('<str:standard>/<str:subject>/<slug:slug>/delete/',
         views.LessonDeleteView.as_view(), name='lesson_delete'),
#     path('assignments/<int:id>/', views.viewAssignment, name='view_assignments'),

    # path('video/', include('base.urls'), name='video'),



    # api urls
    # path('standardApi/', include(router.urls)),
]
