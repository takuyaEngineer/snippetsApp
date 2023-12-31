# Generated by Django 4.2.6 on 2023-11-06 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_snippet_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, default='', null=True)),
                ('email', models.TextField(blank=True, default='', null=True)),
                ('password', models.TextField(blank=True, default='', null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=32, verbose_name='タグ名')),
                ('snippets', models.ManyToManyField(related_name='tags', related_query_name='tag', to='common.snippet')),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='本文')),
                ('commented_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.snippet', verbose_name='スニペット')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]
