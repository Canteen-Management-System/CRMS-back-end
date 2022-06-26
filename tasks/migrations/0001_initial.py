# Generated by Django 4.0.5 on 2022-06-25 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immediate_resolution', models.BooleanField()),
                ('action_taken', models.TextField()),
                ('details', models.TextField()),
                ('expectation', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.category')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.department')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.priority')),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.servicetype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
