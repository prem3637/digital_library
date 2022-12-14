# Generated by Django 3.2.4 on 2022-05-04 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_category_computerscience'),
    ]

    operations = [
        migrations.CreateModel(
            name='mechanicalautomobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('ppic', models.ImageField(default='', upload_to='static/mechanicalautomobile')),
                ('branch', models.CharField(max_length=150)),
                ('lan', models.CharField(max_length=50)),
                ('pdate', models.DateField()),
                ('pfile', models.FileField(default='', upload_to='static/mechanicalautomobile')),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.category')),
            ],
        ),
    ]
