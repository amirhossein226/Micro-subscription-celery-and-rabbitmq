from django.urls import path
# from .views import AddressList, AddressDetail
from .views import address_list, address_detail

v = 'v1'
urlpatterns = [
    # path(f'api/{v}/addresses/', AddressList.as_view()),
    # path(f"api/{v}/addresses/<int:pk>/", AddressDetail.as_view())
    path(f'api/{v}/addresses/', address_list),
    path(f'api/{v}/addresses/<int:pk>/', address_detail)
]
