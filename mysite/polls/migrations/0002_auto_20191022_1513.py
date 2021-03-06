# Generated by Django 2.2.6 on 2019-10-22 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('channel', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=5)),
                ('os', models.CharField(max_length=10)),
                ('impressions', models.IntegerField()),
                ('clicks', models.IntegerField()),
                ('installs', models.IntegerField()),
                ('spend', models.IntegerField()),
                ('revenue', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]
