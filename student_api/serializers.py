from rest_framework import serializers
from .models import Student, Path
from django.utils.timezone import now



# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=50)
#     number = serializers.IntegerField()
#     # id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.save()
#         return instance


class StudentSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()
    class Meta:
        model = Student
        # fields = ('id', 'first_name', 'last_name', 'number')
        fields = '__all__'
        # exclude = ('id',)

    def validate_number(self, value):
     
        if value > 1000:
            raise serializers.ValidationError("Numbers must below 1000!")
        return value

    def validate_first_name(self, value):
         
        if value.lower() == "rafe":
            raise serializers.ValidationError("rafe not a student!")
        return value
    
    def get_days_since_joined(self, obj):
        return (now() - obj.register_date).days

class PathSerializer(serializers.ModelSerializer):
    # students = StudentSerializer(many=True, read_only=True) #*tüm bilgiler gelir
    #students = serializers.StringRelatedField(many=True) #* modelde yapılan str methodu görünür.
    students = serializers.PrimaryKeyRelatedField(many=True, read_only=True) #* modelde yapılan path_name field ve id gösterir
    class Meta:
        model = Path
        fields = "__all__"