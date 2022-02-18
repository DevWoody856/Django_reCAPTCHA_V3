from django.urls import path
from formapp import views


app_name = 'formapp'

urlpatterns = [
    path('contact1/', views.home, name='post_list'),
    path('contact2/', views.ContactFormView.as_view(), name='post_list2'),
]