# Generated by Django 4.1.7 on 2023-06-29 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_usermanagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phonenumber',
            field=models.CharField(db_index=True, default=1, max_length=15, unique=True),
            preserve_default=False,
        ),
    ]