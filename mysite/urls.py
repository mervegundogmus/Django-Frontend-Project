from django.urls import path
from .views import AnasayfaView
from .views import ProfileView
from .views import LoginView
from .views import SignupView
from .views import FollowersView
from .views import FollowingView
from .views import EditView
from .views import PostsView


urlpatterns = [
    path('', AnasayfaView.as_view(),name='anasayfa'),
    path('profile/', ProfileView.as_view(),name='profil'),
    path('login/', LoginView.as_view(),name='giris'),
    path('signup/', SignupView.as_view(),name='kayitol'),
    path('edit/', EditView.as_view(),name='duzenle'),
    path('followers/', FollowersView.as_view(),name='takipciler'),
    path('following/', FollowingView.as_view(),name='takipedilen'),
    path('posts/', PostsView.as_view(),name='gonderiler'),
]
