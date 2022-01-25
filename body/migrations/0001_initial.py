# Generated by Django 4.0.1 on 2022-01-25 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('positions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('fatherland', models.CharField(max_length=60)),
                ('position_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='positions.position')),
            ],
        ),
    ]
