# Generated by Django 3.0.3 on 2020-04-26 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_bluda1'),
    ]

    operations = [
        migrations.AddField(
            model_name='bluda1',
            name='kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Kategori', verbose_name='Категория'),
        ),
    ]
