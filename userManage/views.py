from django.views import generic
from userManage.models import User


# Create your views here.


class UserHomeView(generic.ListView):
    template_name = "base.html"
    context_object_name = "users"
    queryset = User.objects.all()
    model = User
