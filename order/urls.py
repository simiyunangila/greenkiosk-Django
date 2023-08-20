from django.urls import path
from .views import order_upload_view
from .views import order_list
from .views import order_detail
from .views import order_update_view
from .views import order_delete



urlpatterns = [
    path("orders/upload/", order_upload_view,name = "order_upload_view"),
    path("orders/list/", order_list,name = "order_list_view"),
    path("orders/<int:id>/", order_detail,name = "order_detail_view"),
    path("orders/edit/<int:id>/", order_update_view,name = "order_update_view"),
    path("product_delete/<int:id>/", order_delete,name = "order_delete"),
]