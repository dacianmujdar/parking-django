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

from parking_project.account.views import ProfileView
from parking_project.offer.views import OffersView, OfferDetail, AllOffersView
from parking_project.parking.views import ParkingList
from parking_project.parking_space.views import ParkingSpacesList, OwnParkingSpacesView
from parking_project.requests.views import RequestView, RequestDetail, AcceptRequestView, RejectRequestView, InboxView, \
    MarkAsViewedView

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', admin.site.urls),

    # account
    url(r'^profile/$', ProfileView.as_view()),

    # parking
    url(r'^parking/$', ParkingList.as_view()),

    # parking area
    url(r'^parking/(?P<parking_id>[0-9]+)/parking-spaces/$', ParkingSpacesList.as_view()),

    url(r'^subscriptions/$', OwnParkingSpacesView.as_view()),

    # requests
    url(r'^requests/(?P<pk>[0-9]+)/$', RequestDetail.as_view()),
    url(r'^requests/(?P<pk>[0-9]+)/accept/$', AcceptRequestView.as_view()),
    url(r'^requests/(?P<pk>[0-9]+)/reject/$', RejectRequestView.as_view()),
    url(r'^requests/(?P<pk>[0-9]+)/mark-as-viewed/$', MarkAsViewedView.as_view()),
    url(r'^requests/$', RequestView.as_view()),
    url(r'^inbox/$', InboxView.as_view()),

    # offers
    url(r'^offers/$', OffersView.as_view()),
    url(r'^all-offers/$', AllOffersView.as_view()),

    url(r'^offers/(?P<pk>[0-9]+)/$', OfferDetail.as_view()),

]

from parking_project.parking_space_detector.parking_detector import refresh_frames
refresh_frames.delay()
