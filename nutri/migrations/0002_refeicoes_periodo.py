# Generated by Django 4.1 on 2022-08-11 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutri', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='refeicoes',
            name='periodo',
            field=models.CharField(choices=[('0', 'Manhã'), ('1', 'Tarde'), ('2', 'Noite'), ('3', 'Madrugada')], default=0, max_length=1, verbose_name='Periodo'),
        ),
    ]