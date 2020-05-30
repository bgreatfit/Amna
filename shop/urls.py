
from django.urls import path

from shop import views

app_name = "shop"
#app_name = "ecommerce"
urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('search/', views.search, name="search"),
    path('<slug>/cart/', views.cart, name="cart"),
    path('mycart/', views.mycart, name="mycart"),
    path('checkout/', views.checkout, name="checkout"),
    path('<slug>/', views.detail, name="detail"),
    path('categories/<slug>/', views.categories, name="categories"),
    path('api/products/', views.api_products, name="api_products"),
    path('products/all',views.product_view,name="product_view"),
    path('account/user',views.account,name="account"),
    path('verify/<tx_id>',views.validate_transaction,name="validate"),
    path('contact',views.contact,name="contact_us")
    
]