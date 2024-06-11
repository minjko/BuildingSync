# Generated by Django 5.0.6 on 2024-06-10 00:31

import django.db.models.deletion
import django.db.models.manager
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStampedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_dt', models.DateTimeField(auto_now_add=True)),
                ('edt_dt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='schema.timestampedmodel')),
                ('nodeId', models.PositiveBigIntegerField(db_column='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='이름')),
                ('sub_name', models.CharField(db_column='SUB_NAME', max_length=255, null=True, verbose_name='서술용 이름')),
                ('sub_display_name', models.CharField(db_column='SUB_DISPLAY-NAME', max_length=255, null=True, verbose_name='화면용 이름')),
                ('dictionary', models.CharField(db_column='DOCUMENTATION', max_length=255, null=True, verbose_name='설명')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, db_column='PARENT', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='schema.node', verbose_name='상위분류')),
            ],
            options={
                'db_table': 'NODE',
                'ordering': ['reg_dt'],
            },
            bases=('schema.timestampedmodel', models.Model),
            managers=[
                ('_tree_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='LeafNode',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='schema.timestampedmodel')),
                ('leafNodeId', models.PositiveBigIntegerField(db_column='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='이름')),
                ('sub_name', models.CharField(db_column='SUB_NAME', max_length=255, null=True, verbose_name='서술용 이름')),
                ('sub_display_name', models.CharField(db_column='SUB_DISPLAY-NAME', max_length=255, null=True, verbose_name='화면용 이름')),
                ('dictionary', models.CharField(db_column='DOCUMENTATION', max_length=255, null=True, verbose_name='설명')),
                ('enumerations', models.JSONField(default='{}')),
                ('enumerations_html', models.CharField(db_column='ENUMERATIONS_HTML', max_length=255, verbose_name='속성값 목록 HTML')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, db_column='Node', null=True, on_delete=django.db.models.deletion.SET_NULL, to='schema.node', verbose_name='상위분류')),
            ],
            bases=('schema.timestampedmodel',),
        ),
    ]