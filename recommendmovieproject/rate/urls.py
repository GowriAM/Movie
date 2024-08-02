from  django.urls import path
from  . import views
app_name='cartapp'


urlpatterns=[
    path('add/<int:product_id>/',views.add_rate,name='add_rate'),
    path('',views.rate_detail,name='rate_detail'),
    path('remove/<int:product_id>/',views.rate_remove,name='rate_remove'),
    # path('full_remove/<int:product_id>/',views.full_remove,name='full_remove'),
    # path('make_payment/<int:product_id>/',views.make_payment,name='make_payment'),

]