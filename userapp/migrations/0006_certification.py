# Generated by Django 5.0.6 on 2024-06-27 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_qualifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificatename', models.CharField(max_length=255)),
                ('certificateimage', models.ImageField(upload_to='certificate_images/')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.userprofile')),
            ],
        ),
    ]