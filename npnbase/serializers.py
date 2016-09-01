from rest_framework import serializers
from npnbase.models import NameRecord, GroupRecord, ZodiacRecord


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupRecord
        fields = ('group_name',)


class ZodiacSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZodiacRecord
        fields = ('zod_sign',)


class NameSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(source='get_groups', read_only=True, many=True)
    zodiacs = ZodiacSerializer(source='get_zodiacs', read_only=True, many=True)

    class Meta:
        model = NameRecord
        fields = ('_id', 'name', 'sex', 'description', 'groups', 'zodiacs')






