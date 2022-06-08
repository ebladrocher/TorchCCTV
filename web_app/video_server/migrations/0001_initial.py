# Generated by Django 4.0.4 on 2022-06-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(max_length=50, verbose_name='IP адрес')),
                ('is_active', models.BooleanField(db_index=True, default=False, verbose_name='Активная/неактивная камера')),
                ('last_activities', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
