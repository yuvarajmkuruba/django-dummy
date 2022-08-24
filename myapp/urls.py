from unicodedata import name
from django.urls import path
from . import views
urlpatterns =[
    path('',views.index,name='index'),
    # path('counter',views.counter,name='counter'),
    # path('counter1',views.counter1,name='counter1'),
    path('counter2',views.counter2,name='counter2'),
    # path('',views.port,name='port')
]