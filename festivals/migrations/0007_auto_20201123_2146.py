# Generated by Django 3.1.3 on 2020-11-23 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festivals', '0006_auto_20201123_1852'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='t_festival',
            options={'permissions': [('edit', 'Can create, edit and delete festivals')]},
        ),
        migrations.AlterModelOptions(
            name='t_interpret',
            options={'permissions': [('edit', 'Can create, edit and delete inteprets')]},
        ),
        migrations.AlterModelOptions(
            name='t_stage',
            options={'permissions': [('edit', 'Can create, edit and delete stages')]},
        ),
    ]
