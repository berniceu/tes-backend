# Generated by Django 5.0.7 on 2024-07-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0007_remove_course_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='hours',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='beginner', max_length=20),
        ),
    ]
