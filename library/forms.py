from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import CATEGORY_CHOICES, PAYMENT_METHOD_CHOICES, Book, BorrowedBook, Member


class AddMemberForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Enter Member Name"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control form-control-lg", "placeholder": "Enter Member Email"})
    )

    class Meta:
        model = Member
        fields = ["name", "email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if Member.objects.filter(email=email).exists():
            raise ValidationError(_("A member with that email already exists."))

        return email


class UpdateMemberForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Enter Member Name"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control form-control-lg", "placeholder": "Enter Member Email"})
    )

    class Meta:
        model = Member
        fields = ["name", "email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if Member.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError(_("A member with that email already exists."))

        return email


class AddBookForm(forms.ModelForm):
    title = forms.CharField(
    label="Titulo",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Ingrese el título del libro"})
    ) 
    author = forms.CharField(
    label="Autor",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Ingrese autor del libro"})
    )

    category = forms.ChoiceField(
    label="Categoría",
        choices=CATEGORY_CHOICES, widget=forms.Select(attrs={"class": "form-control form-control-lg"})
    )

    quantity = forms.IntegerField(
        label="Cantidad",
        widget=forms.NumberInput(attrs={"class": "form-control form-control-lg", "placeholder": "Ingrese la cantidad"})
    )
    
    borrowing_fee = forms.DecimalField(
        label="Tarifa de préstamo:",
        widget=forms.NumberInput(attrs={"class": "form-control form-control-lg", "placeholder": "Ingrese la tarifa de préstamo"})
    )
    
    clasification_number = forms.CharField(
        label="Clasificación",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Ingrese la clasificación del libro"})
    )

    class Meta:
        model = Book
        fields = ["title", "author", "category", "quantity", "clasification_number", "borrowing_fee"]


class LendBookForm(forms.ModelForm):
    book = forms.ModelChoiceField(
        label="Libro / Libros",
        queryset=Book.objects.filter(quantity__gt=0),
        empty_label=None,
        widget=forms.Select(
            attrs={"class": "form-control form-control-lg js-example-basic-multiple w-100", "multiple": "multiple"}
        ),
    )

    member = forms.ModelChoiceField(
        label="Miembro",
        queryset=Member.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={"class": "form-control form-control-lg js-example-basic-single w-100"}),
    )

    return_date = forms.DateField(
        label="Fecha de regreso:",
        widget=forms.DateInput(attrs={"class": "form-control form-control-lg", "type": "date", "id": "return-date"})
    )
    
    condition_notes = forms.DateField(
        label="Detalles del libro",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Ingrese los detalles del libro"})
    )

    fine = forms.DecimalField(
        label="Sanción",
        widget=forms.NumberInput(attrs={"class": "form-control form-control-lg", "placeholder": "Ingrese sanción"})
    )

    class Meta:
        model = BorrowedBook
        fields = ["book", "member", "return_date", "condition_notes", "fine"]


class LendMemberBookForm(forms.ModelForm):
    book = forms.ModelChoiceField(
        queryset=Book.objects.filter(quantity__gt=0),
        empty_label=None,
        widget=forms.Select(
            attrs={"class": "form-control form-control-lg js-example-basic-multiple w-100", "multiple": "multiple"}
        ),
    )

    return_date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control form-control-lg", "type": "date", "id": "return-date"})
    )
    
    condition_notes = forms.DateField(
        label="Detalles del libro",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Ingrese los detalles del libro"})
    )


    fine = forms.DecimalField(
        widget=forms.NumberInput(attrs={"class": "form-control form-control-lg", "placeholder": "Enter Fine"})
    )

    class Meta:
        model = BorrowedBook
        fields = ["book", "return_date", "condition_notes", "fine"]


class UpdateBorrowedBookForm(forms.ModelForm):
    return_date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control form-control-lg", "type": "date", "id": "return-date"})
    )

    fine = forms.DecimalField(
        widget=forms.NumberInput(attrs={"class": "form-control form-control-lg", "placeholder": "Enter Fine"})
    )

    class Meta:
        model = BorrowedBook
        fields = ["return_date", "fine"]


class PaymentForm(forms.Form):
    payment_method = forms.ChoiceField(
        choices=PAYMENT_METHOD_CHOICES, widget=forms.Select(attrs={"class": "form-control form-control-lg"})
    )

    class Meta:
        fields = ["payment_method"]
