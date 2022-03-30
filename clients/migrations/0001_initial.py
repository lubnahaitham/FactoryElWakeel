# Generated by Django 4.0.2 on 2022-03-30 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, max_length=200, null=True)),
                ('client_personal_id', models.CharField(blank=True, max_length=30, null=True)),
                ('client_home_tel', models.CharField(blank=True, max_length=15, null=True)),
                ('client_office_tel', models.CharField(blank=True, max_length=15, null=True)),
                ('client_mobile', models.CharField(blank=True, max_length=25, null=True)),
                ('client_address', models.CharField(blank=True, max_length=500, null=True)),
                ('client_province', models.CharField(blank=True, max_length=200, null=True)),
                ('client_nghood', models.CharField(blank=True, max_length=300, null=True)),
                ('client_pobox', models.CharField(blank=True, max_length=300, null=True)),
                ('contact_name', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_id', models.CharField(blank=True, max_length=30, null=True)),
                ('contact_mobile', models.CharField(blank=True, max_length=25, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='create_client', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='update_client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
