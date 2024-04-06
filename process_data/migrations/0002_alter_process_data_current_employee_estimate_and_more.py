# Generated by Django 5.0.3 on 2024-04-03 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process_data',
            name='current_employee_estimate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='process_data',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='process_data',
            name='size_range',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='process_data',
            name='total_employee_estimate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='process_data',
            name='year_founded',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
