# Generated by Django 4.0.1 on 2022-02-06 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninja_namer', '0005_rename_ninja_word_ninjaword_ninja_word_option'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NinjaWordOptions',
            new_name='NinjaWordOption',
        ),
    ]
