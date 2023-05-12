import imp
from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index1,name='index.html'),
    path('about/',views.about,name='about.html'),
    path('blog-single',views.blogsingle,name='blog-single.html'),
    path('product-single',views.productsingle,name='product-single.html'),
    path('blog',views.blog,name='blog.html'),
    path('mcart',views.cart,name='cart.html'),
    path('checkout',views.checkout,name='checkout.html'),
    path('contact',views.contact,name='contact.html'),
    path('<id>/detail',views.detail_view,name='detail_view'),
    path('shop',views.shop,name='shop.html'),
    path('wishlist',views.wishlist,name='wishlist.html'),
    path('add',views.create_view,name='create_view'),
     path('<id>/update',views.update_view,name='update_view'),
      path('<id>/delete',views.delete_view,name='delete_view'),
      path('index',views.index1,name='index.html'),

]

