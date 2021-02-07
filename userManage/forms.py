from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Row
from django import forms
from userManage.models import User


class NewUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First Name"}))  # noqa
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Last Name"}))  # noqa
    user_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))  # noqa
    description = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Description"}), required=False)  # noqa

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Row(Div("first_name"), css_class="form-new-user"),
                Row(Div("last_name"), css_class="form-new-user"),
                Row(Div("user_name"), css_class="form-new-user"),
                Row(Div("description"), css_class="form-new-user"),
            )
        )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "user_name", "description"]
