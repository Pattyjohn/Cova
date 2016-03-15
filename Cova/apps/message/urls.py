from django.conf.urls import url

from .views import Email


urlpatterns = [

    url(r'^email/$',Email.as_view(), name="email"),
    


]
