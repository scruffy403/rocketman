# Generated by Django 3.2.7 on 2021-09-10 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Testimonials',
            new_name='Testimonial',
        ),
        migrations.RenameField(
            model_name='testimonial',
            old_name='attributions',
            new_name='attribution',
        ),
    ]
