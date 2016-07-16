from django.conf.urls import url
from django.contrib import admin

from lists import views as lists_views


urlpatterns = [
        url(r'^$', lists_views.home_page, name='home'),
        url(r'^admin/', admin.site.urls),
]
