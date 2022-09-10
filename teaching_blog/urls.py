"""teaching_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import app_users
import curriculum


from rest_framework.urlpatterns import format_suffix_patterns
from curriculum.api import views
import curriculum.views as vs

import base.views as videovs
# import base
  


admin.site.site_header = 'kachhya Dashboard'                   
admin.site.index_title = 'Welcome to kachhya Dashboard'  
admin.site.site_title = 'kachhya Dashboard' 

urlpatterns = [
    path('', include('app_users.urls')),
    path('curriculum/',include('curriculum.urls')),
    path('admin/', admin.site.urls),

    #video call app imported
    path('video/<str:id>/', videovs.lobby, name='video'),
    path('room/', videovs.room),
    path('get_token/', videovs.getToken),

    path('create_member/', videovs.createMember),
    path('get_member/', videovs.getMember),
    path('delete_member/', videovs.deleteMember),
    # path('video/', include('base.urls'), name="video"),

    # path('search/',vs.search, name='search'),
    path('standard/', views.StandardList.as_view()),
    path('standard/<int:pk>/', views.StandardDetail.as_view()),
    path('subject/', views.SubjectList.as_view()),
    path('subject/<int:pk>/', views.SubjectDetail.as_view()),
    path('lesson/', views.LessonList.as_view()),
    path('lesson/<int:pk>/', views.LessonDetail.as_view()),
    path('comment/', views.CommentList.as_view()),
    path('comment/<int:pk>/', views.CommentDetail.as_view()),
    path('userprofileinfo/', views.UserProfileInfoList.as_view()),
    path('userprofileinfo/<int:pk>/', views.UserProfileInfoDetail.as_view()),
    path('contacts/', views.ContactList.as_view()),
    path('contacts/<int:pk>/', views.ContactDetail.as_view()),
    path('assignment/', vs.viewAssignment, name='viewAssignment'),
    # path('search/', views.SearchSerializer.as_view()),
    path('assignment/<str:id>/', vs.viewAssignmentById, name="viewAssignmentById"),
    path('create-assignment/<str:id>', vs.createAssignment, name="createAssignment"),
    path('submit-assignment/<str:id>',vs.submitAssignment, name='answerSubmission'),
    path('viewSubmission/<str:id>', vs.viewSubmission, name="viewSubmission"),
    path('popular/<str:id>', vs.viewPopular, name="viewPopular"),



]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
