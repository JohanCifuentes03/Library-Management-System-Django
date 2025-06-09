from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date
from .models import CATEGORY_CHOICES, PAYMENT_METHOD_CHOICES, Book, BorrowedBook, Member


class AddMemberForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Ingrese el nombre del miembro"})
    )
    email = forms.EmailField(
        label="Correo",
        widget=forms.EmailInput(attrs={"class": "form-control form-control-lg", "placeholder": "Ingrese el correo del miembro"})
    )
    fecha_nacimiento = forms.DateField(
        label="Fecha de nacimiento",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control form-control-lg"})
    )
    acudiente_nombre = forms.CharField(
        label="Nombre del acudiente",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"})
    )
    acudiente_telefono = forms.CharField(
        label="Teléfono del acudiente",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"})
    )

    class Meta:
        model = Member
        fields = ["name", "email", "fecha_nacimiento", "acudiente_nombre", "acudiente_telefono"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Member.objects.filter(email=email).exists():
            raise ValidationError(_("Ya fue agregado un miembro con este correo."))
        return email

    def clean(self):
        cleaned_data = super().clean()
        fecha_nacimiento = cleaned_data.get("fecha_nacimiento")
        acudiente_nombre = cleaned_data.get("acudiente_nombre")
        acudiente_telefono = cleaned_data.get("acudiente_telefono")

        if fecha_nacimiento:
            hoy = date.today()
            edad = hoy.year - fecha_nacimiento.year - (
                (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day)
            )
            if edad < 18:
                if not acudiente_nombre or not acudiente_telefono:
                    raise ValidationError(_("Para miembros menores de edad, se requieren los datos del acudiente."))


class UpdateMemberForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Ingrese el nombre del miembro"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control form-control-lg", "placeholder": "Ingrese el correo del miembro"})
    )

    class Meta:
        model = Member
        fields = ["name", "email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if Member.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError(_("Ya fue agregado un miembro con este correo."))

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
    
    clasification_number = forms.CharField(
        label="Clasificación",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Ingrese la clasificación del libro"})
    )

    class Meta:
        model = Book
        fields = ["title", "author", "category", "quantity", "clasification_number"]


class LendBookForm(forms.ModelForm):
    book = forms.ModelChoiceField(
        label="Libro / Libros",
        queryset=Book.objects.filter(quantity__gt=0),
        empty_label=None,
        widget=forms.Select(
            attrs={
                "class": "form-control form-control-lg js-example-basic-multiple w-100",
                "multiple": "multiple"
            }
        ),
    )

    member = forms.ModelChoiceField(
        label="Miembro",
        queryset=Member.objects.all(),
        empty_label=None,
        widget=forms.Select(
            attrs={
                "class": "form-control form-control-lg js-example-basic-single w-100"
            }
        )
    )

    return_date = forms.DateField(
        label="Fecha de regreso:",
        widget=forms.DateInput(
            attrs={
                "class": "form-control form-control-lg",
                "type": "date",
                "id": "return-date"
            }
        )
    )

    condition_notes = forms.CharField(
        label="Detalles del libro",
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Ingrese los detalles del libro",
                "rows": 3
            }
        )
    )


    class Meta:
        model = BorrowedBook
        fields = ["book", "member", "return_date", "condition_notes"]

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields['member'].label_from_instance = lambda obj: f"{obj.name} ({obj.email})"


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
    
    condition_notes = forms.CharField(
        label="Detalles del libro",
        required=False,
        widget=forms.Textarea(attrs={
            "class": "form-control form-control-lg",
            "placeholder": "Ingrese los detalles del libro",
            "rows": 3
        })
    )


    fine = forms.DecimalField(
        widget=forms.NumberInput(attrs={"class": "form-control form-control-lg", "placeholder": "Enter Fine"})
    )

    class Meta:
        model = BorrowedBook
        fields = ["book", "return_date", "condition_notes", "fine"]


class UpdateBorrowedBookForm(forms.ModelForm):
    return_date = forms.DateField(
                label="Fecha de devolución",
        widget=forms.DateInput(attrs={"class": "form-control form-control-lg", "type": "date", "id": "return-date"})
    )



    class Meta:
        model = BorrowedBook
        fields = ["return_date"]
