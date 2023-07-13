# Generated by Django 4.1.7 on 2023-06-29 15:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='First Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Last Updated')),
            ],
        ),
        migrations.AddIndex(
            model_name='restaurant',
            index=models.Index(fields=['name', 'public_id', 'created', 'updated'], name='core_restau_name_7cf6ed_idx'),
        ),
    ]
