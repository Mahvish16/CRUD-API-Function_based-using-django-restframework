from rest_framework import serializers
from student.models import Student
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.CharField(max_length=100)
    class Meta:
        fields = ('id', 'name','roll')
    
    def create(self, validated_data):
        instance=Student.objects.create(**validated_data)
        return instance
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name')
        instance.roll = validated_data.get('roll')
        instance.save()
        return instance
    