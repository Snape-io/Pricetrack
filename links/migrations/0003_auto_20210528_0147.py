# Generated by Django 3.2.3 on 2021-05-27 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_auto_20210528_0141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ('price_diff', '-created')},
        ),
        migrations.RenameField(
            model_name='link',
            old_name='price_difference',
            new_name='price_diff',
        ),
        migrations.RenameField(
            model_name='link',
            old_name='name',
            new_name='productname',
        ),
    ]