from django.urls import path
from . import views

urlpatterns = [
    path("upload/<str:filename>/", views.FileShareView.as_view(), name="share file"),
    # path("create/", views.CreateShareView.as_view(), name="create_share"),
    path("list/", views.ListSharesView.as_view(), name="list_shares"),
    path("history/", views.ListSharesHistoryView.as_view(), name="list_shares_history"),
    # path("url/", views.getPreSignedURL, name="upload_url")
]