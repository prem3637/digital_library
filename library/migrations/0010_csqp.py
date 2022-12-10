# Generated by Django 3.2.4 on 2022-05-08 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_eenote_manote_mpnote'),
    ]

    operations = [
        migrations.CreateModel(
            name='csqp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150)),
                ('ppic', models.ImageField(default='', upload_to='static/csnotes')),
                ('branch', models.CharField(max_length=150)),
                ('year', models.IntegerField()),
                ('pfile', models.FileField(default='', upload_to='static/csnotes')),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.category')),
            ],
        ),
    ]