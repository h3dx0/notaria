# Generated by Django 2.2.7 on 2020-01-30 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200127_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosbasicos',
            name='fecha_creacion',
            field=models.DateField(auto_created=True, default="2000-01-01"),
            preserve_default=False,
        ),
    ]
