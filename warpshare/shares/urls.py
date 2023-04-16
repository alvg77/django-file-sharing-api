from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.CreateShareView.as_view(), name="create_share"),
    path("list/", views.ListSharesView.as_view(), name="list_shares"),
    path("history/", views.ListSharesHistoryView.as_view(), name="list_shares_history"),
]