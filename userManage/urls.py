from django.urls import path
from userManage.views import UserHomeView


urlpatterns = [
    path(r"", UserHomeView.as_view(), name="index"),
]
