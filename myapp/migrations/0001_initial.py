# Generated by Django 3.0.8 on 2020-07-03 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(default='404', max_length=9, primary_key=True, serialize=False)),
                ('real_name', models.CharField(blank=True, max_length=60, null=True)),
                ('tz', models.CharField(blank=True, default='INDIA', max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, default='2020-02-10 11:34:35', null=True)),
                ('end_time', models.DateTimeField(blank=True, default='2020-02-10 11:34:35', null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.User')),
            ],
        ),
    ]
