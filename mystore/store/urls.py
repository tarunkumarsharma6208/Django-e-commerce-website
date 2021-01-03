from django.urls import path
from store import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>', views.home, name='product_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.productDetail, name='product_detail'),

    path('cart/add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/delete/<int:product_id>/', views.remove_cart_product, name='remove_cart_product'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('thanks/<int:order_id>', views.thanks_page, name='thanks'),

    path('account/create/', views.signup_view, name='signup'),
    path('account/login/', views.signin_view, name='login'),
    path('account/logout/', views.signout_view, name='logout'),
    path('order_history/', views.order_history, name='order_history'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),

    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
]