# Generated by Django 4.2.7 on 2023-12-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_student_delete_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
