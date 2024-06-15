# Generated by Django 5.0.6 on 2024-06-15 04:42

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='imagen',
            new_name='foto',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='fecha_ncto',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='telefono',
        ),
        migrations.AddField(
            model_name='persona',
            name='fnacto',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='persona',
            name='sexo',
            field=models.CharField(choices=[('F', 'FEMENINO'), ('M', 'MASCULINO'), ('O', 'OTRO')], default=datetime.datetime(2024, 6, 15, 4, 42, 46, 846278, tzinfo=datetime.timezone.utc), max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='correo',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.CreateModel(
            name='Mancuerna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('10', '10 kilos'), ('20', '20 kilos')], max_length=2)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gymapp.persona')),
            ],
        ),
    ]
