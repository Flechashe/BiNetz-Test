# Generated by Django 4.0.5 on 2022-06-18 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('fecha_de_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('cobertura_medica', models.CharField(max_length=50, verbose_name='cobertura médica')),
            ],
        ),
    ]