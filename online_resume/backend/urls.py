from django.conf import settings
from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name='main'),
    path('save/',views.save_file,name='save'),
    path('download/<str:name>',views.download_pdf,name='download'),
    path('open/<str:name>',views.open_pdf,name='open')
]

