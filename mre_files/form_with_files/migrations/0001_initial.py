# Generated by Django 4.0.7 on 2022-10-03 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelWithFileField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_image_title', models.CharField(max_length=100)),
                ('file_field', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('second_file_field', models.FileField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
    ]
