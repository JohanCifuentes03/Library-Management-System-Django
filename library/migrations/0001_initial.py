import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        # Modelo para los libros
        migrations.CreateModel(
            name='Book',  # Libro
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),  # Fecha de creación
                ('updated_at', models.DateTimeField(auto_now=True)),  # Fecha de actualización
                ('title', models.CharField(max_length=100)),  # Título
                ('author', models.CharField(max_length=100)),  # Autor
                ('category', models.CharField(
                    choices=[
                        ('fiction', 'Ficción'),
                        ('non-fiction', 'No ficción'),
                        ('biography', 'Biografía'),
                        ('history', 'Historia'),
                        ('science', 'Ciencia'),
                        ('poetry', 'Poesía'),
                        ('drama', 'Drama'),
                        ('religion', 'Religión'),
                        ('children', 'Infantil'),
                        ('other', 'Otro')
                    ],
                    max_length=20
                )),  # Categoría
                ('quantity', models.PositiveIntegerField(default=0)),  # Cantidad disponible
                ('borrowing_fee', models.DecimalField(
                    decimal_places=2,
                    default=0.0,
                    max_digits=10,
                    validators=[django.core.validators.MinValueValidator(0.0)]
                )),  # Tarifa de préstamo
                ('status', models.CharField(
                    choices=[('available', 'Disponible'), ('borrowed', 'Prestado')],
                    default='available',
                    max_length=20
                )),  # Estado del libro
            ],
            options={
                'abstract': False,
            },
        ),

        # Modelo para los miembros
        migrations.CreateModel(
            name='Member',  # Miembro
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),  # Fecha de creación
                ('updated_at', models.DateTimeField(auto_now=True)),  # Fecha de actualización
                ('name', models.CharField(max_length=100)),  # Nombre
                ('email', models.EmailField(max_length=254)),  # Correo electrónico
                ('amount_due', models.DecimalField(
                    decimal_places=2,
                    default=0.0,
                    max_digits=10,
                    validators=[django.core.validators.MinValueValidator(0.0)]
                )),  # Monto adeudado
            ],
            options={
                'abstract': False,
            },
        ),

        # Modelo para los libros prestados
        migrations.CreateModel(
            name='BorrowedBook',  # Libro Prestado
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),  # Fecha de préstamo
                ('updated_at', models.DateTimeField(auto_now=True)),  # Fecha de actualización
                ('return_date', models.DateField()),  # Fecha de devolución
                ('returned', models.BooleanField(default=False)),  # ¿Fue devuelto?
                ('fine', models.DecimalField(
                    decimal_places=2,
                    default=0.0,
                    max_digits=10,
                    validators=[django.core.validators.MinValueValidator(0.0)]
                )),  # Multa
                ('book', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='borrowed_books',
                    to='library.book'
                )),  # Libro relacionado
                ('member', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='borrowed_books',
                    to='library.member'
                )),  # Miembro que tomó el préstamo
            ],
            options={
                'abstract': False,
            },
        ),

        # Modelo para las transacciones
        migrations.CreateModel(
            name='Transaction',  # Transacción
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),  # Fecha de creación
                ('updated_at', models.DateTimeField(auto_now=True)),  # Fecha de actualización
                ('amount', models.DecimalField(
                    decimal_places=2,
                    default=0.0,
                    max_digits=10,
                    validators=[django.core.validators.MinValueValidator(0.0)]
                )),  # Monto de la transacción
                ('payment_method', models.CharField(
                    choices=[('cash', 'Efectivo'), ('mpesa', 'Mpesa'), ('card', 'Tarjeta')],
                    max_length=20
                )),  # Método de pago
                ('member', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='transactions',
                    to='library.member'
                )),  # Miembro que hizo la transacción
            ],
            options={
                'abstract': False,
            },
        ),
    ]
    
