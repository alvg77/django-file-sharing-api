from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.CreateShareView.as_view(), name="create_share"),
    path("list/<int:id>/", views.ListSharesView.as_view(), name="list_shares"),
]