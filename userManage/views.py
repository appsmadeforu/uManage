from django.contrib.auth.models import User as AuthUser
from django.db import IntegrityError
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.template.defaulttags import register
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from userManage.forms import NewUserForm
from userManage.models import Role, User, Userrole


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
                authUser.first_name = form.cleaned_data["first_name"]
                authUser.last_name = form.cleaned_data["last_name"]
                user.username = form.cleaned_data["user_name"]
                user.description = form.cleaned_data["description"]
                selectedRoles = Role.objects.filter(id__in=self.request.POST.getlist("role_list"))  # noqa
                authUser.save()
                user.save()
                if selectedRoles:
                    for role in selectedRoles:
                        Userrole.objects.create(user=user, role=role)
                else:
                    Userrole.objects.create(user=user)
            except IntegrityError:
                return redirect(reverse("view_user"))
            except BaseException:
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

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

    def get_userroles(self):
        users = User.objects.all()
        user_role = {}
        for user in users:
            roles = Userrole.objects.filter(user_id=user.id)
            joined_string = ", ".join([role.role.role_name for role in roles])
            user_role.update({user.id: joined_string})
        return user_role

    def get_context_data(self, **kwargs):
        context = super(UserHomeView, self).get_context_data(**kwargs)
        context["userrole"] = self.get_userroles()
        return context


def deleteUser(request, user_id):
    """
    Method to delete a user
    :param request:
    :param user_id: User Id
    :return: redirects to home page.
    """
    if request.method == "POST":
        user = User.objects.filter(user_id=user_id)
        user_role = Userrole.objects.filter(user__in=user)
        if user or user_role:
            user.delete()
            user_role.delete()
            if request.POST.get("is_req_from_edit"):
                return render(request, "view_user.html")
    return redirect("/")


class EditUserView(generic.DetailView):
    model = User
    template_name = "edit_user.html"
    context_object_name = "user"

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            return redirect(reverse("view_user"))
        context = self.get_context_data(user=self.object)
        context["roles"] = Role.objects.all()
        userrole = Userrole.objects.filter(user_id=self.object.id)
        context["user_roles"] = [role.role.id for role in userrole]
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs.get("pk"))
