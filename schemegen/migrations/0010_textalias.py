# Generated by Django 3.0.7 on 2020-07-18 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemegen', '0009_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html_id', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
        ),
    ]