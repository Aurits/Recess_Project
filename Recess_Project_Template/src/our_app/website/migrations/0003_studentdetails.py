# Generated by Django 4.2.3 on 2023-08-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_facilityfeedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('studentId', models.CharField(max_length=20)),
                ('emailAddress', models.EmailField(max_length=254)),
                ('year_of_study', models.CharField(max_length=10)),
            ],
        ),
    ]