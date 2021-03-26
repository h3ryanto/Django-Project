# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Barang(models.Model):
    kode_barang = models.CharField(max_length=5)
    nama_barang = models.CharField(max_length=10)
    satuan = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'barang'


class BarangBackup(models.Model):
    kode_barang = models.CharField(max_length=5)
    nama_barang = models.CharField(max_length=10)
    qty = models.IntegerField()
    kategory = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'barang_backup'


class HistoryPenjualan(models.Model):
    kode_transaksi_pembelian = models.CharField(max_length=5)
    kode_barang = models.CharField(max_length=5)
    qty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'history_penjualan'


class Penjualan(models.Model):
    kode_transaksi = models.IntegerField()
    kode_barang = models.ForeignKey(Barang, models.DO_NOTHING, db_column='kode_barang')
    qty = models.IntegerField()
    status_history = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'penjualan'


class TransaksiPembelian(models.Model):
    kode_transaksi = models.CharField(max_length=5, blank=True, null=True)
    kode_barang = models.ForeignKey(Barang, models.DO_NOTHING, db_column='kode_barang', blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    stok = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transaksi_pembelian'
