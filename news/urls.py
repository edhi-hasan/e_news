from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('latest_news/',views.latest_news,name = 'latest'),
    path('bangladesh/',views.bangladesh_news,name = 'bd'),
    path('politics/',views.politics_news,name = 'pn'),
    path('world/',views.World_news,name = 'world'),
    path('sports/',views.sports_news,name = 'sports'),
    path('trade/',views.trade_news,name = 'trade'),
    path('technology/',views.technology_news,name = 'technology'),
    path('entertainment/',views.entertainment_news,name = 'entertainment'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('details/',views.details_news,name='detial'),

]
