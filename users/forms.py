from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Librarian


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"class": "form-control form-control-lg", "placeholder": "Correo electrónico"}),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg", "placeholder": "Contraseña"}),
    )

    class Meta:
        fields = ("email", "password")

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not Librarian.objects.filter(email=email).exists():
            raise ValidationError(_("Usuario con ese correo no existe"))

        return email


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Nombre"}),
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Apellido"}),
    )

    email = forms.CharField(
        widget=forms.EmailInput(attrs={"class": "form-control form-control-lg", "placeholder": "Correo electrónico"}),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg", "placeholder": "Contraseña"}),
    )

    repeat_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg", "placeholder": "Repetir contraseña"}),
    )

    class Meta:
        model = Librarian
        fields = ["first_name", "last_name", "email", "password", "repeat_password"]

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if Librarian.objects.filter(email=email).exists():
            raise ValidationError(_("El correo ya existe"))

        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")

        try:
            validate_password(password)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)

        return password

    def clean_repeat_password(self):
        password = self.cleaned_data.get("password")
        repeat_password = self.cleaned_data.get("repeat_password")

        if password != repeat_password:
            raise ValidationError(_("Las contraseñas no coinciden"))

        return repeat_password