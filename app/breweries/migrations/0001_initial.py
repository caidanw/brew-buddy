# Generated by Django 3.0 on 2019-12-15 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brewery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('brewery_type', models.CharField(max_length=20, null=True)),
                ('street', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('postal_code', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('longitude', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]
