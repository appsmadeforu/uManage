from django.urls import path, re_path
from userManage.views import AddUserView, DeleteUserView, UserHomeView, index


urlpatterns = [
    path(r"", index, name="index"),
    path(r"users/", UserHomeView.as_view(), name="view_user"),
    path(r"add_user/", AddUserView.as_view(), name="add_user"),
    re_path(r"delete/(?P<user_id>[0-9]+)/$", DeleteUserView, name="delete_user"),  # noqa
]
