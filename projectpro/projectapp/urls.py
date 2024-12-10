from django.urls import path
from projectapp import views
urlpatterns=[
    # path('hello/',views.apple),
    path('home/',views.msg,name='home'),
    # path('page',views.msg,name='page'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('msg/', views.msg, name='msg'),
    path('add-to-cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('',views.color,name='home1'),
    # path('payment/',views.payment,name='payment')
    path('payment/<int:product_id>/', views.payment_page, name='payment_page'),
    path('process_payment/<int:product_id>/', views.process_payment, name='process_payment'),


]