# Generated by Django 3.2.2 on 2022-05-26 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_url', models.URLField(max_length=255, unique=True, verbose_name='源地址')),
                ('name', models.CharField(blank=True, default='', max_length=256, verbose_name='名称')),
                ('play_url', models.URLField(blank=True, default='', max_length=256, verbose_name='播放地址')),
                ('cover', models.URLField(blank=True, default='', max_length=256, verbose_name='封面')),
                ('duration', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='时长(秒)')),
                ('width', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='宽度')),
                ('height', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='高度')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('is_active', models.BooleanField(default=True, verbose_name='有效')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频',
                'ordering': ('-create_time',),
            },
        ),
    ]
