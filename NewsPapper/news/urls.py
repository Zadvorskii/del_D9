from django.urls import path
from .views import * # импортируем наше представление

urlpatterns = [
                path('', PostView.as_view()),
                path('create/', PostCreateView.as_view(), name='post_create'),
                path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
                path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
                path('search/', PostSearch.as_view()),
                path('<int:pk>', PostDetailView.as_view(), name='post_detail')

]