from django.conf.urls import url, include
from django.urls import path, re_path
from rest_auth.views import PasswordResetConfirmView, PasswordResetView
from tutorials import views
from django.conf import settings
from tutorials.views import Belts, StudentBelts, BeltsDetail, StudentLesson, PhotoStudent, ServiceDojoDetail

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    #url(r'^api/tutorials$', views.tutorial_list),
    #url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    #url(r'^api/tutorials/published$', views.tutorial_list_published),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/', include('django.contrib.auth.urls')),
    #url(r'^rest-auth/password/', include('rest_auth.password.urls')),
    url(r'^rest-auth/accounts/', include('allauth.urls')),
    
    url(r'^api_v1/users/(?P<pk>[0-9]+)$', views.user_detail),
    url(r'^api_v1/users/([a-z0-9_-]{3,15})$', views.user_detail_by_username),
    
    url(r'^api_v1/belt/(?P<pk>[0-9]+)$', BeltsDetail.as_view()),
    url(r'^api_v1/belts$', Belts.as_view()),
    
    url(r'^api_v1/studentbelts$', StudentBelts.as_view()),
    #url(r'^api_v1/studentLesson$', StudentLesson.as_view()),
    url(r'^api_v1/studentLesson/(?P<student>.+)/(?P<service>.+)/(?P<date>.+)$', StudentLesson.as_view()),
    url(r'^api_v1/studentLesson/', StudentLesson.as_view()),
    url(r'^api_v1/PhotoStudent/', PhotoStudent.as_view()),
   #  url(r'^api_v1/PhotoStudent/', PhotoStudent.as_view()),
    url(r'^api_v1/serviceDojo/(?P<pk>[0-9]+)$', ServiceDojoDetail.as_view()),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

