# Generated by Django 5.0.6 on 2024-06-11 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0002_node_enumerations_node_enumerations_html_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='enumerations_html',
            field=models.CharField(blank=True, db_column='ENUMERATIONS_HTML', default='', max_length=255, null=True, verbose_name='속성값 목록 HTML'),
        ),
    ]
