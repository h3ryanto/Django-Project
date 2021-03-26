# Generated by Django 3.1.6 on 2021-03-26 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_barang', models.CharField(max_length=5)),
                ('nama_barang', models.CharField(max_length=10)),
                ('satuan', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'barang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BarangBackup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_barang', models.CharField(max_length=5)),
                ('nama_barang', models.CharField(max_length=10)),
                ('qty', models.IntegerField()),
                ('kategory', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'barang_backup',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistoryPenjualan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_transaksi_pembelian', models.CharField(max_length=5)),
                ('kode_barang', models.CharField(max_length=5)),
                ('qty', models.IntegerField()),
            ],
            options={
                'db_table': 'history_penjualan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Penjualan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_transaksi', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('status_history', models.IntegerField()),
            ],
            options={
                'db_table': 'penjualan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TransaksiPembelian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_transaksi', models.CharField(blank=True, max_length=5, null=True)),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('stok', models.IntegerField()),
            ],
            options={
                'db_table': 'transaksi_pembelian',
                'managed': False,
            },
        ),
    ]
