# Generated by Django 3.2.7 on 2021-09-04 15:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hackathonguild', '0003_auto_20210904_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='token',
            field=models.CharField(default='', max_length=200, verbose_name='トークン'),
        ),
        migrations.AddField(
            model_name='participant',
            name='token_delete_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='トークン削除日'),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='', max_length=200, verbose_name='トークン'),
        ),
    ]
