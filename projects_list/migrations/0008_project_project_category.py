# Generated by Django 5.0.1 on 2024-02-23 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_list', '0007_alter_project_description_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_category',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.PROTECT, to='projects_list.categorie'),
        ),
    ]