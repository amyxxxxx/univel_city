# Generated by Django 3.0 on 2021-10-28 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.PositiveIntegerField()),
                ('course', models.CharField(max_length=25)),
                ('date_of_birth', models.DateField()),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('no_of_pages', models.IntegerField(default=10)),
                ('author', models.CharField(max_length=300)),
                ('body', models.TextField()),
                ('isbn', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='attendance.Student')),
            ],
        ),
    ]
