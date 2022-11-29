from django.urls import path
from .views import *

urlpatterns = [
    path('', main_func, name='home'),
    path('category/<int:category_id>/', get_category, name='categoryAAA'),
    path('news/<int:news_id>/', news_read, name='news_read'),
    path('news/add_news/', add_news, name='add_news'),

]

