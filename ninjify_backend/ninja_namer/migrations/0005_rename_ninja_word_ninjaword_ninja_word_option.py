# Generated by Django 4.0.1 on 2022-02-06 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninja_namer', '0004_remove_ninjaword_ninja_word_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ninjaword',
            old_name='ninja_word',
            new_name='ninja_word_option',
        ),
    ]
