# Generated by Django 4.1 on 2022-08-11 20:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nutri', '0003_alter_refeicoes_data_refeicao'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='refeicoes',
            new_name='Refeicoess',
        ),
    ]
