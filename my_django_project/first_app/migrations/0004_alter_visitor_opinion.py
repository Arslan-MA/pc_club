# Generated by Django 4.2.1 on 2023-06-16 16:49

from django.db import migrations, models
import first_app.validator


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_alter_visitor_visiting_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='opinion',
            field=models.TextField(validators=[first_app.validator.validator_opinion]),
        ),
    ]
