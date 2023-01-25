from django.urls import path
from .views import SnackDetail, SnackListView

urlpatterns = [
    # snack list is homepage
    path('', SnackListView.as_view(), name='snack_list'),
    path('snack/<int:pk>/', SnackDetail.as_view(), name='snack_detail')
]