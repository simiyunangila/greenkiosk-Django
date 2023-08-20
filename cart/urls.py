from django.urls import path
from .views import cart_upload_view
from .views import cart_list
from .views import cart_detail
from .views import cart_update_view


urlpatterns = [
    path("cart/upload/",cart_upload_view,name = "cart_upload_view"),
    path("cart/list/",cart_list,name = "cart_list_view"),
    path("cart/<int:id>/",cart_detail,name = "cart_detail_view"),
    path("cart/edit/<int:id>/",cart_update_view,name = "cart_update_view")
]