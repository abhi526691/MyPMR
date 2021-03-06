# Generated by Django 3.2.7 on 2021-09-26 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pmr', '0003_auto_20210926_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='vitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hip_circum', models.CharField(blank=True, max_length=50, null=True)),
                ('waist_circum', models.CharField(blank=True, max_length=50, null=True)),
                ('whr', models.CharField(blank=True, max_length=50, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='pmr.profile')),
            ],
        ),
    ]
