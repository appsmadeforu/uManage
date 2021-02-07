from django.shortcuts import get_object_or_404, redirect
from django.utils import log
from django.views import generic
from userManage.models import User


# Create your views here.


class UserHomeView(generic.ListView):
    template_name = "base.html"
    context_object_name = "users"
    queryset = User.objects.all()
    model = User


def delete_user(request, user_id):
    if request.method == "POST":
        user = get_object_or_404(User, id=user_id)
        user.delete()
        log.info("User is deleted successfully")
    return redirect("/")
