# Generated by Django 2.2.5 on 2019-11-03 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.DecimalField(decimal_places=2, max_digits=4)),
                ('snore', models.DecimalField(decimal_places=2, max_digits=4)),
                ('body_position', models.DecimalField(decimal_places=0, max_digits=2)),
                ('testdate', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BodyStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waistline', models.DecimalField(decimal_places=2, max_digits=4)),
                ('body_fat_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('alcoholism', models.DecimalField(decimal_places=0, max_digits=1)),
                ('day_sleepy', models.DecimalField(decimal_places=0, max_digits=1)),
                ('Irritability', models.DecimalField(decimal_places=0, max_digits=1)),
                ('age', models.DecimalField(decimal_places=1, max_digits=4)),
                ('inputdate', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]