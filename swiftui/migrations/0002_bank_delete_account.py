# Generated by Django 4.0.4 on 2022-05-24 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiftui', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('category', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('active', models.BooleanField()),
                ('balance', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
