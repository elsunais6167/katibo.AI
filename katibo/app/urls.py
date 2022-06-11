from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('sale', views.sale, name='sale'),
    path('category', views.category, name='category'),
    path('product', views.product, name='product'),
    path('add_qty', views.add, name='add'),
    path('customer', views.customer, name='customer'),
    path('report', views.report, name='report'),
    path('sell', views.sell_pred, name='sell'),
    path('prof', views.prof_pred, name='prof'),
    path('types', views.types, name='types'),
    path('change', views.change, name='change'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('add_customer', views.create_customer, name='add_customer'),
    path('add_product', views.create_product, name='add_product'),
    path('add_category', views.create_category, name='add_category'),
    path('add_qty/<str:pk>', views.add_qty, name='add_qty'),
    path('sale_item', views.sale_item, name='sale_item'),
    path('analyser/', views.anal, name="analyser"),
    path('analyserp/', views.analp, name="analyserp")
]