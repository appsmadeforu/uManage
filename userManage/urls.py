from django.urls import path, re_path
from userManage.views import (
    AddUserView,
    EditUserView,
    UserHomeView,
    deleteUser,
    index,
)


urlpatterns = [
    path(r"", index, name="index"),
    path(r"users/", UserHomeView.as_view(), name="view_user"),
    path(r"add_user/", AddUserView.as_view(), name="add_user"),
    re_path(r"users/edit_user/(?P<pk>\d+)/$", EditUserView.as_view(), name="edit_user"),  # noqa
    re_path(r"delete/(?P<user_id>[0-9]+)/$", deleteUser, name="delete_user"),  # noqa
]
