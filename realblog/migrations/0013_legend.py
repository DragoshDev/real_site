# Generated by Django 5.2.3 on 2025-06-24 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realblog', '0012_rename_current_club_rumor_from_team_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Legend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='legends/')),
                ('position', models.CharField(max_length=50)),
                ('years_active', models.CharField(max_length=100)),
            ],
        ),
    ]
