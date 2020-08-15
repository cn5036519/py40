# Generated by Django 2.2.5 on 2020-08-15 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20200815_0949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinfo',
            options={'verbose_name': '书籍信息'},
        ),
        migrations.AlterModelOptions(
            name='peopleinfo',
            options={'verbose_name': '人物信息'},
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='commentcount',
            field=models.IntegerField(default=0, verbose_name='评论量'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='name',
            field=models.CharField(max_length=10, verbose_name='书名'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='出版日期'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='readcount',
            field=models.IntegerField(default=0, verbose_name='阅读量'),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.BookInfo', verbose_name='关联书籍'),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='description',
            field=models.CharField(max_length=200, null=True, verbose_name='人物描述'),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(0, '男'), (1, '女')], default=1, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='name',
            field=models.CharField(max_length=10, verbose_name='人物'),
        ),
        migrations.AlterModelTable(
            name='bookinfo',
            table='bookinfo',
        ),
        migrations.AlterModelTable(
            name='peopleinfo',
            table='peopleinfo',
        ),
    ]
