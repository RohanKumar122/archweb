# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-17 20:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# releng.migrations.0003_release_populate_last_modified
def release_populate_last_modified_forwards(apps, schema_editor):
    Release = apps.get_model('releng', 'Release')
    Release.objects.update(last_modified=models.F('created'))

def release_populate_last_modified_backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    replaces = [(b'releng', '0001_initial'), (b'releng', '0002_release_last_modified'), (b'releng', '0003_release_populate_last_modified'), (b'releng', '0004_auto_20170524_0704'), (b'releng', '0005_auto_20180616_0947')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Architecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bootloader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BootType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClockChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Filesystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HardwareType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstallType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Iso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(editable=False)),
                ('removed', models.DateTimeField(blank=True, default=None, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'ISO',
            },
        ),
        migrations.CreateModel(
            name='IsoType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'ISO type',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.DateField(db_index=True)),
                ('version', models.CharField(max_length=50, unique=True)),
                ('kernel_version', models.CharField(blank=True, max_length=50)),
                ('md5_sum', models.CharField(blank=True, max_length=32, verbose_name=b'MD5 digest')),
                ('sha1_sum', models.CharField(blank=True, max_length=40, verbose_name=b'SHA1 digest')),
                ('created', models.DateTimeField(editable=False)),
                ('available', models.BooleanField(default=True)),
                ('info', models.TextField(blank=True, verbose_name=b'Public information')),
                ('torrent_data', models.TextField(blank=True, help_text=b'base64-encoded torrent file')),
                ('last_modified', models.DateTimeField(default=datetime.datetime(2001, 1, 1, 0, 0, tzinfo=utc), editable=False)),
            ],
            options={
                'ordering': ('-release_date', '-version'),
                'get_latest_by': 'release_date',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=500)),
                ('user_email', models.EmailField(max_length=75, verbose_name=b'email address')),
                ('ip_address', models.GenericIPAddressField(unpack_ipv4=True, verbose_name=b'IP address')),
                ('created', models.DateTimeField(editable=False)),
                ('success', models.BooleanField(default=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('architecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='releng.Architecture')),
                ('boot_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='releng.BootType')),
                ('bootloader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='releng.Bootloader')),
                ('clock_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='releng.ClockChoice')),
                ('filesystem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='releng.Filesystem')),
                ('hardware_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='releng.HardwareType')),
                ('install_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='releng.InstallType')),
                ('iso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='releng.Iso')),
                ('iso_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='releng.IsoType')),
                ('modules', models.ManyToManyField(blank=True, null=True, to=b'releng.Module')),
                ('rollback_filesystem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name=b'rollback_test_set', to='releng.Filesystem')),
                ('rollback_modules', models.ManyToManyField(blank=True, null=True, related_name=b'rollback_test_set', to=b'releng.Module')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='releng.Source')),
            ],
        ),
        migrations.RunPython(
            code=release_populate_last_modified_forwards,
            reverse_code=release_populate_last_modified_backwards
        ),
        migrations.RemoveField(
            model_name='test',
            name='modules',
        ),
        migrations.RemoveField(
            model_name='test',
            name='rollback_modules',
        ),
        migrations.AlterField(
            model_name='test',
            name='user_email',
            field=models.EmailField(max_length=254, verbose_name=b'email address'),
        ),
        migrations.RemoveField(
            model_name='test',
            name='architecture',
        ),
        migrations.RemoveField(
            model_name='test',
            name='boot_type',
        ),
        migrations.RemoveField(
            model_name='test',
            name='bootloader',
        ),
        migrations.RemoveField(
            model_name='test',
            name='clock_choice',
        ),
        migrations.RemoveField(
            model_name='test',
            name='filesystem',
        ),
        migrations.RemoveField(
            model_name='test',
            name='hardware_type',
        ),
        migrations.RemoveField(
            model_name='test',
            name='install_type',
        ),
        migrations.RemoveField(
            model_name='test',
            name='iso',
        ),
        migrations.RemoveField(
            model_name='test',
            name='iso_type',
        ),
        migrations.RemoveField(
            model_name='test',
            name='rollback_filesystem',
        ),
        migrations.RemoveField(
            model_name='test',
            name='source',
        ),
        migrations.DeleteModel(
            name='Architecture',
        ),
        migrations.DeleteModel(
            name='Bootloader',
        ),
        migrations.DeleteModel(
            name='BootType',
        ),
        migrations.DeleteModel(
            name='ClockChoice',
        ),
        migrations.DeleteModel(
            name='Filesystem',
        ),
        migrations.DeleteModel(
            name='HardwareType',
        ),
        migrations.DeleteModel(
            name='InstallType',
        ),
        migrations.DeleteModel(
            name='Iso',
        ),
        migrations.DeleteModel(
            name='IsoType',
        ),
        migrations.DeleteModel(
            name='Module',
        ),
        migrations.DeleteModel(
            name='Source',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
