# Generated by Django 3.1.3 on 2020-11-29 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivals', '0021_r_vystupuje_na_id_interpret'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_festival',
            name='koniec',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='t_festival',
            name='zaciatok',
            field=models.DateTimeField(),
        ),
    ]
