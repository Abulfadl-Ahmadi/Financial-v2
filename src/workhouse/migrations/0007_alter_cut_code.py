# Generated by Django 4.1.7 on 2023-04-30 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workhouse', '0006_alter_cut_code_alter_cut_model_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cut',
            name='code',
            field=models.CharField(blank=True, max_length=4, null=True, unique=True, verbose_name='کد برش'),
        ),
    ]
