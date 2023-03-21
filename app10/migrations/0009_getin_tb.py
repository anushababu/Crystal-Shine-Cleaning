# Generated by Django 4.1.5 on 2023-03-09 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app10', '0008_category_tb_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='getin_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('serid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app10.service_tb')),
            ],
        ),
    ]
