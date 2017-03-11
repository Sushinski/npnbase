from rest_framework import serializers
from npnbase.models import NameRecord, GroupRecord, ZodiacRecord


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupRecord
        fields = ('group_name',)


class ZodiacSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZodiacRecord
        fields = ('zod_month',)


class NameSerializer(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(many=False)
    zodiacs = serializers.SlugRelatedField(many=True, read_only=True, slug_field='zod_month')

    class Meta:
        model = NameRecord
        fields = ('_id', 'name', 'sex', 'description', 'groups', 'zodiacs')






