from django.urls import path

from .views import VueHomeView

app_name = 'common'
urlpatterns = [
    path('', VueHomeView.as_view(), name='home'),
]
