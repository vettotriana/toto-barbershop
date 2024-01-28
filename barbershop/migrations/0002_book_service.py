# Generated by Django 3.0.3 on 2024-01-27 12:31

from django.db import migrations, models

class Migration(migrations.Migration):
    # Especifica que esta migración depende de la migración inicial '0001_initial' de la app 'barbershop'.
    dependencies = [
        ('barbershop', '0001_initial'),
    ]

    # Define las operaciones que se realizarán en la base de datos.
    operations = [
        # Añade un nuevo campo 'service' al modelo 'Book'.
        migrations.AddField(
            model_name='book',
            name='service',
            field=models.CharField(
                # Define las opciones disponibles para el campo 'service'.
                choices=[
                    ('Mañana Temprano (6:00 - 8:00)', 'Mañana Temprano (6:00 - 8:00)'),
                    ('Mediodía (12:00 - 14:00)', 'Mediodía (12:00 - 14:00)'),
                    ('Tarde Noche (18:00 - 21:00)', 'Tarde Noche (18:00 - 21:00)'),
                    ('Noche (21:00 - 23:00)', 'Noche (21:00 - 23:00)')
                ],
                max_length=200,
                # Permite que el campo sea opcional.
                null=True,
            ),
        ),
    ]