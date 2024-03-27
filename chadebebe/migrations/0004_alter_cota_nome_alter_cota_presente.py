# Generated by Django 4.1 on 2024-03-27 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chadebebe', '0003_presente_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cota',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome e Sobrenome'),
        ),
        migrations.AlterField(
            model_name='cota',
            name='presente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cotas', to='chadebebe.presente'),
        ),
    ]
