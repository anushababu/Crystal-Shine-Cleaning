# Generated by Django 4.1.5 on 2023-02-28 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app10', '0004_contact_tb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_tb',
            old_name='namr',
            new_name='name',
        ),
    ]