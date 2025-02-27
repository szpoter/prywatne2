from django.urls import path
from . import views
from .views import articles_view, argument_view, add_to_cart, cart_view, remove_from_cart, search_results

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('homepage/', views.homepage, name='homepage'),
    path('cart/', cart_view, name='cart'),
    path('contact_info/', views.contact_view, name='contact'),
    path('about/', views.about_view, name='about'),
    path('search-article/', search_results, name='search_results'),
    path('articles/<int:id>/add-to-cart/', add_to_cart, name='add_to_cart'),
    path('articles/<int:id>/like/', views.like_article, name='like_article'),
    path('articles/<int:id>/dislike/', views.dislike_article, name='dislike_article'),
    path('cart/remove/<int:id>/', remove_from_cart, name='remove_from_cart'), 
    path('articles/', articles_view, name='articles'),
    path('articles/<int:article_id>/', argument_view, name='argument'),
    path('index/', views.index_view, name='index'),
]