from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class GroupRecord(models.Model):
    _id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=64, verbose_name='group_name', unique=True)

    def __str__(self):
        return self.group_name

    def __str__(self):
        return str(self.group_name)

    def __unicode__(self):
        return u'%s' % self.group_name

    class Meta:
        db_table = 'GroupRecord'


@python_2_unicode_compatible
class ZodiacRecord(models.Model):
    _id = models.AutoField(primary_key=True)
    zod_month = models.PositiveSmallIntegerField(unique=True, verbose_name='zod_month')
    zod_sign = models.CharField(max_length=64, unique=True, verbose_name='zod_sign')

    def __str__(self):
        return self.zod_sign

    class Meta:
        db_table = 'ZodiacRecord'


@python_2_unicode_compatible
class NameRecord(models.Model):
    GENDER_CHOICE = (
        (1, 'Boy'),
        (0, 'Girl')
    )
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, verbose_name='name', unique=True)
    selected = models.IntegerField(verbose_name='selected', default=0)
    description = models.TextField(verbose_name='description', null=True)
    groups = models.ForeignKey(GroupRecord, blank=True, null=True, on_delete=models.SET_NULL)
    sex = models.PositiveIntegerField(verbose_name='sex', choices=GENDER_CHOICE, default=1)
    zodiacs = models.ManyToManyField(ZodiacRecord, through='NameZodiacRecord', through_fields=('name_id', 'zodiac_id'))

    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        db_table = 'NameRecord'

    def __str__(self):
        return self.name


class NameZodiacRecord(models.Model):
    _id = models.AutoField(primary_key=True, default=None)
    name_id = models.ForeignKey(NameRecord, on_delete=models.CASCADE)
    zodiac_id = models.ForeignKey(ZodiacRecord, on_delete=models.CASCADE)

    class Meta:
        db_table = 'NameZodiacRecord'


class PrefRecord(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='name', unique=True, null=False, max_length=64)
    value = models.CharField(verbose_name='value', null=True, max_length=64)
    
    class Meta:
        db_table = 'PrefRecord'


