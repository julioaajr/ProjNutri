# Generated by Django 4.1 on 2024-03-27 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomme', models.TextField()),
                ('qtd', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('qtd', models.IntegerField()),
                ('presente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chadebebe.presente')),
            ],
        ),
    ]
