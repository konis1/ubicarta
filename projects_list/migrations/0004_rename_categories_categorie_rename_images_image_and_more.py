# Generated by Django 5.0.1 on 2024-02-13 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects_list', '0003_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Categorie',
        ),
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
        migrations.RenameModel(
            old_name='ProjectLinks',
            new_name='ProjectLink',
        ),
    ]
