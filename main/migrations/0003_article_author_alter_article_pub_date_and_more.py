# Generated by Django 4.2.6 on 2023-11-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_article_options_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(auto_created=True, default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(auto_created=True, verbose_name='publication date'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_date',
            field=models.DateField(auto_now_add=True, verbose_name='update date'),
        ),
    ]
