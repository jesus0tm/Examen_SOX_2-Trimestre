# Generated by Django 5.0.2 on 2024-02-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registro_jug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField()),
                ('num_socio', models.IntegerField()),
                ('contraseña', models.CharField(max_length=100)),
            ],
        ),
    ]