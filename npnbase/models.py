from django.db import models


class GroupRecord(models.Model):
    _id = models.PositiveIntegerField(primary_key=True)
    group_name = models.TextField(verbose_name='group_name')


class NameRecord(models.Model):
    _id = models.PositiveIntegerField(primary_key=True)
    name = models.TextField(verbose_name='name', unique=True)
    sex = models.PositiveIntegerField(verbose_name='sex')
    selected = models.IntegerField(verbose_name='selected', default=0)
    description = models.TextField(verbose_name='description')


class NameGroupRecord(models.Model):
    _id = models.PositiveIntegerField(primary_key=True)
    group_id = models.ForeignKey(GroupRecord, on_delete=models.CASCADE)
    name_id = models.ForeignKey(NameRecord, on_delete=models.CASCADE)


class ZodiacRecord(models.Model):
    _id = models.PositiveIntegerField(primary_key=True)
    zod_month = models.PositiveSmallIntegerField(unique=True, verbose_name='zod_month')
    zod_sign = models.TextField(unique=True, verbose_name='zod_sign')


class NameZodiacRecord(models.Model):
    _id = models.PositiveIntegerField(primary_key=True)
    name_id = models.ForeignKey(NameRecord, on_delete=models.CASCADE)
    zodiac_id = models.ForeignKey(ZodiacRecord, on_delete=models.CASCADE)
