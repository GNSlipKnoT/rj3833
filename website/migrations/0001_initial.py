# Generated by Django 2.2.7 on 2019-11-21 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
