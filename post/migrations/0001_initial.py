# Generated by Django 3.0.5 on 2020-04-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postWriter', models.CharField(max_length=20, null=True)),
                ('postDate', models.CharField(max_length=200, null=True)),
                ('postContent', models.TextField(null=True)),
            ],
        ),
    ]
