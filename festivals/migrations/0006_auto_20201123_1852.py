# Generated by Django 3.1.3 on 2020-11-23 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('festivals', '0005_t_festival_vytvoril'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r_rezervacia_na',
            name='id_uzivatela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='t_festival',
            name='vytvoril',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='t_rezervacia',
            name='majitel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='t_uzivatel',
        ),
    ]
