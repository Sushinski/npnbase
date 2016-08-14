from rest_framework import serializers
from npnbase.models import NameRecord, NameGroupRecord, GroupRecord, ZodiacRecord, NameZodiacRecord


class NameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NameRecord
        fields = ('_id', 'name', 'sex', 'description')


class NameGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NameGroupRecord
        fields = ('name_id__name', 'group_id__name')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupRecord
        fields = ('_id', 'group_name')


class NameZodiacSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NameZodiacRecord
        fields = ('name_id__name', 'zodiac_id__zod_month')
