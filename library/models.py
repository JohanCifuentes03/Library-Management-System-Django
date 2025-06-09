from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from users.models import AbstractBaseModel

STATUS_CHOICES = (
    ("available", "Available"),
    ("not-available", "Not-Available"),
)

CATEGORY_CHOICES = (
    ("ficción", "Ficción"),
    ("no ficción", "No ficción"),
    ("biografía", "Biografía"),
    ("historia", "Historia"),
    ("ciencia", "Ciencia"),
    ("poesía", "Poesía"),
    ("drama", "Drama"),
    ("religión", "Religión"),
    ("infantil", "Infantil"),
    ("otro", "Otro"),
    )

PAYMENT_METHOD_CHOICES = (
    ("cash", "Cash"),
    ("mpesa", "Mpesa"),
    ("card", "Card"),
)


class Member(AbstractBaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
        
    # NUEVOS CAMPOS PARA VALIDACIÓN Y ACUDIENTE
    fecha_nacimiento = models.DateField(null=True, blank=True)
    acudiente_nombre = models.CharField(max_length=100, blank=True)
    acudiente_telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.name}"

    def calculate_amount_due(self):
        borrowed_books = self.borrowed_books.all()
        amount = 0
        for book in borrowed_books:
            if book.return_date < timezone.now().date() and not book.returned:
                amount += book.fine
        return amount

    def es_menor_de_edad(self):
        if self.fecha_nacimiento:
            today = timezone.now().date()
            edad = today.year - self.fecha_nacimiento.year - (
                (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
            )
            return edad < 18
        return False


class Book(AbstractBaseModel):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    quantity = models.PositiveIntegerField(default=0)
    clasification_number = models.CharField(max_length=20, default="N/A")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="available")
    
    def __str__(self):
        return f"{self.title} por {self.author}"


class BorrowedBook(AbstractBaseModel):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="borrowed_books")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrowed_books")
    return_date = models.DateField()
    returned = models.BooleanField(default=False)
    fine = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0.00)])
    condition_notes = models.TextField(
        verbose_name="Descripción del estado del libro",
        null=True,
        blank=True,
        help_text="Ej: Pasta rayada, hoja 73 rota, portada despegada..."
    )
    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title} on {self.created_at}"


