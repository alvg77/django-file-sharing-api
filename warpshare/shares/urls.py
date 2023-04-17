from django.urls import path
from . import views

urlpatterns = [
    path("upload/<str:filename>/", views.FileShareView.as_view(), name="share file"),
    path("list/", views.ListSharesView.as_view(), name="list_shares"),
    path("history/", views.ListSharesHistoryView.as_view(), name="list_shares_history"),
]