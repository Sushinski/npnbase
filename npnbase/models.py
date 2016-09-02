from django.db import models


class GroupRecord(models.Model):
    _id = models.PositiveIntegerField(primary_key=True)
    group_name = models.CharField(verbose_name='group_name', max_length=50)

    class Meta:
        db_table = 'GroupRecord'


class NameRecord(models.Model):
    _id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(verbose_name='name', unique=True, max_length=64)
    sex = models.PositiveIntegerField(verbose_name='sex')
    selected = models.IntegerField(verbose_name='selected', default=0)
    description = models.TextField(verbose_name='description')
    groups = models.ForeignKey(GroupRecord, blank=True, null=True, on_delete=models.SET_NULL)
    zodiacs = models.ManyToManyField(ZodiacRecord, through=NameZodiacRecord)

    class Meta:
        db_table = 'NameRecord'


class ZodiacRecord(models.Model):
    _id = models.PositiveIntegerField(primary_key=True)
    zod_month = models.PositiveSmallIntegerField(unique=True, verbose_name='zod_month')
    zod_sign = models.CharField(unique=True, verbose_name='zod_sign', max_length=64)

    class Meta:
        db_table = 'ZodiacRecord'


class NameZodiacRecord(models.Model):
    _id = models.PositiveIntegerField(primary_key=True)
    name_id = models.ForeignKey(NameRecord, on_delete=models.CASCADE)
    zodiac_id = models.ForeignKey(ZodiacRecord, on_delete=models.CASCADE)

    class Meta:
        db_table = 'NameZodiacRecord'
