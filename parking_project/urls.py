"""parking_project URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

from parking_project.parking.views import ParkingList, RequestDetail, RequestView

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', admin.site.urls),
    url(r'^parking/$', ParkingList.as_view()),
    url(r'^requests/(?P<pk>[0-9]+)/$', RequestDetail.as_view()),
    url(r'^requests/$', RequestView.as_view()),

]
