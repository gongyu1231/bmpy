# Generated by Django 2.0.1 on 2018-01-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180114_1512'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consume',
            options={'ordering': ['consumename'], 'verbose_name': '积分消费', 'verbose_name_plural': '消费名称'},
        ),
        migrations.AlterField(
            model_name='adduser',
            name='email',
            field=models.EmailField(max_length=20, verbose_name='电子邮箱'),
        ),
    ]