# Generated by Django 2.2.5 on 2020-08-15 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20200814_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='commentcount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='pub_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='readcount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='name',
            field=models.CharField(max_length=10, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='gender',
            field=models.SmallIntegerField(),
        ),
    ]
