# Generated by Django 5.0.6 on 2024-06-19 01:31

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_rename_mysite_acco_account_7dc129_idx_mysite_acco_account_317046_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_id',
            field=models.UUIDField(default=uuid.UUID('770ac205-63a2-4bb0-a8de-7b2a44b534cc'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
