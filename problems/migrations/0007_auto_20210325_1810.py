# Generated by Django 2.2.10 on 2021-03-25 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0006_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='c_body',
        ),
    ]
