"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from students import views      # https://djbook.ru/rel1.9/topics/http/urls.html
from django.conf import settings            #https://docs.djangoproject.com/en/1.11/howto/static-files/
from django.conf.urls.static import static  #https://docs.djangoproject.com/en/1.11/howto/static-files/
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    # Students urls
    url(r'^$', views.students_list, name='home'),
    url(r'^students/add/$', views.students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', views.students_edit, name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', views.students_delete, name='students_delete'),

    # Groups urls
    url(r'^groups$', views.groups_list, name='groups'),
    url(r'^groups/add/$', views.groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', views.groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', views.groups_delete, name='groups_delete'),

    # Journal urls
    #url(r'^journal$', views.students_list, name='journal'),
    url(r'^journal$', views.journal_list, name='journal'),
    url(r'^journal/(?P<jid>\d+)/student/$', views.journal_student, name='journal_student'),

    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #https://docs.djangoproject.com/en/1.11/howto/static-files/
