# Generated by Django 3.0.4 on 2020-05-14 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_prodw'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('message', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
