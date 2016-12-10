from django.db import models


class GroupRecord(models.Model):
    _id = models.AutoField(primary_key=True)
    group_name = models.CharField(verbose_name='group_name', max_length=50)

    def __str__(self):
        return str(self.group_name)
    
    def __unicode__(self):
        return u'%s' % self.group_name

    class Meta:
        db_table = 'GroupRecord'


class ZodiacRecord(models.Model):
    _id = models.AutoField(primary_key=True)
    zod_month = models.PositiveSmallIntegerField(unique=True, verbose_name='zod_month')
    zod_sign = models.CharField(unique=True, verbose_name='zod_sign', max_length=64)

    def __str__(self):
        return str(self.zod_sign)
    
    def __unicode__(self):
        return u'%s' % self.zod_sign

    class Meta:
        db_table = 'ZodiacRecord'


class NameZodiacRecord(models.Model):
    _id = models.AutoField(primary_key=True)
    name_id = models.ForeignKey('NameRecord', on_delete=models.CASCADE)
    zodiac_id = models.ForeignKey(ZodiacRecord, on_delete=models.CASCADE)

    class Meta:
        db_table = 'NameZodiacRecord'


class NameRecord(models.Model):
    GENDER_CHOICE = (
        (1, 'Boy'),
        (0, 'Girl')
    )
    _id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='name', unique=True, max_length=64)
    selected = models.IntegerField(verbose_name='selected', default=0)
    description = models.TextField(verbose_name='description', null=True)
    groups = models.ForeignKey(GroupRecord, blank=True, null=True, on_delete=models.SET_NULL)
    sex = models.PositiveIntegerField(verbose_name='sex', choices=GENDER_CHOICE, default=1)
    zodiacs = models.ManyToManyField(ZodiacRecord, through=NameZodiacRecord, through_fields=('name_id', 'zodiac_id'))

    class Meta:
        db_table = 'NameRecord'




