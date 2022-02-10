# Generated by Django 4.0.2 on 2022-02-10 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=20)),
                ('patient_age', models.IntegerField()),
                ('patient_number', models.IntegerField()),
                ('patient_address', models.CharField(max_length=20)),
                ('patient_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='BackendData',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]