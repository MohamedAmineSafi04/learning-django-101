from django.urls import path
from .views import HomePageView, PostDetailView, AddPostView, API, SendAPI


app_name = 'feed' #MUST MATCH NAMESPACE IN myapp/urls.py

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name="detail"),
    path('post/', AddPostView.as_view(), name='post'),

    
    path('api/', API.as_view(), name='api'),
    path('sendapi/', SendAPI.as_view(), name='sendapi'),
]