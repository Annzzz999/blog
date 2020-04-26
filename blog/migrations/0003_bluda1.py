# Generated by Django 3.0.3 on 2020-04-26 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20200426_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bluda1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Описание')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата начала')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
