# Generated by Django 4.0.4 on 2023-12-01 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_seating_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seating',
            name='employee_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.employee'),
        ),
    ]