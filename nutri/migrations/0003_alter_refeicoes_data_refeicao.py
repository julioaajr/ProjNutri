# Generated by Django 4.1 on 2022-08-11 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutri', '0002_refeicoes_periodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refeicoes',
            name='data_refeicao',
            field=models.DateTimeField(verbose_name='Data da Refeição'),
        ),
    ]
