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

    def get_groups(self):
        groups_ids = NameGroupRecord.objects.filter(name_id=self)
        return GroupRecord.objects.filter(_id__in=groups_ids.values_list('group_id', flat=True)).values_list('group_name', flat=True)

    def get_zodiacs(self):
        zodiac_ids = NameZodiacRecord.objects.filter(name_id=self)
        return ZodiacRecord.objects.filter(_id__in=zodiac_ids.values_list('zodiac_id', flat=True)).values_list('zod_month', flat=True)

    class Meta:
        db_table = 'NameRecord'


class NameGroupRecord(models.Model):
    _id = models.PositiveIntegerField(primary_key=True)
    group_id = models.ForeignKey(GroupRecord, on_delete=models.CASCADE)
    name_id = models.ForeignKey(NameRecord, on_delete=models.CASCADE)

    class Meta:
        db_table = 'NameGroupRecord'


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
