from django.urls import path, re_path
from userManage.views import UserHomeView, delete_user


urlpatterns = [
    path(r"", UserHomeView.as_view(), name="index"),
    re_path(r"delete/(?P<user_id>[0-9]+)/$", delete_user, name="delete_user"),
]
