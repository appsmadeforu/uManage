from django.contrib.auth.models import User as AuthUser
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import log
from django.views import generic
from django.views.generic import CreateView
from userManage.forms import NewUserForm
from userManage.models import Role, User


# Create your views here.


def index(request):
    """
    index method to render base template
    """
    return render(request, "base.html")


class AddUserView(CreateView, generic.ListView):
    """
    View to Add new user data
    """

    template_name = "add_user.html"
    form_class = NewUserForm
    model = User
    success_url = reverse_lazy("view_user")

    def get_context_data(self, **kwargs):
        context = super(AddUserView, self).get_context_data(**kwargs)
        context["roles"] = Role.objects.all()
        return context

    def form_valid(self, form):
        if form.is_valid():
            try:
                authUser = AuthUser.objects.get(username=form.cleaned_data["user_name"])  # noqa
                user = User()
                user.user_id = authUser.id
                user.first_name = form.cleaned_data["first_name"]
                user.last_name = form.cleaned_data["last_name"]
                user.username = form.cleaned_data["user_name"]
                user.description = form.cleaned_data["description"]
                user.save()
            except IntegrityError:
                return redirect(reverse("view_user"))
        return redirect(reverse("view_user"))

    def get_success_url(self):
        return redirect(reverse("view_user"))


class UserHomeView(generic.ListView):
    """
    UserHomeView - View user details
    """

    template_name = "view_user.html"
    context_object_name = "users"
    queryset = User.objects.all()
    model = User


def DeleteUserView(request, user_id):
    """
    Method to delete a user
    :param request:
    :param user_id: User Id
    :return: redirects to home page.
    """
    if request.method == "POST":
        user = get_object_or_404(User, id=user_id)
        user.delete()
        log.request_logger("User is deleted successfully")
    return redirect("/")
