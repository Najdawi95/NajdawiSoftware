from django.conf.urls import url
from my_app import views

# TEMPLATE TAGGING
app_name = 'my_app'

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^base/$', views.base, name='base'),

]
