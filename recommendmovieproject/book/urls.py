from django.urls import path
from  . import views
app_name='book'

urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail, name='prodCatdetail'),
    # path('add_review', views.add_review, name='add_review'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('book/item/<int:item_id>/add_review/', views.add_review, name='add_review'),

    # path('item/<int:item_id>/add_review/', views.add_review, name='add_review'),

]
