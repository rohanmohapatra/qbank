from .models import User, Syllabus, StudentDetail, Subject, Science, YearScience, YearCommerce, Commerce
from .models import BookmarkQuest, YearClass10, Profile, Class10, SolvedQuest
from rest_framework import serializers
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['email'],
            validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class SyllabusSerializer(serializers.ModelSerializer):
    subjects = serializers.StringRelatedField(many=True)

    class Meta:
        model = Syllabus
        fields = ('id','syllabus', 'classes', 'subjects')
    
class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetail
        fields = ('__all__')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetail
        fields = ('id','student_name','user','phone','syllabus','Class','sub1','sub2','sub3','sub4','sub5','sub6')

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookmarkQuest
        fields = ('__all__')

class SolvedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolvedQuest
        fields = ('__all__')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('__all__')

class SubjectSienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Science
        fields = ('subject',)

class ScienceSerializer(serializers.ModelSerializer):
    year = serializers.StringRelatedField(many=True)

    class Meta:
        model = Science
        fields = ('qid','qclass','qno','subject','topic','question','image1','image2','year')

class yearScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearScience
        fields = ('years',)

class TopicScienceSerializer(serializers.ModelSerializer):
    year = serializers.StringRelatedField(many=True)

    class Meta:
        model = Science
        fields = ('topic','year')

class SubjectCommerceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commerce
        fields = ('subject',)

class CommerceSerializer(serializers.ModelSerializer):
    year = serializers.StringRelatedField(many=True)

    class Meta:
        model = Science
        fields = ('qid','qclass','qno','subject','topic','question','image1','image2','year')

class yearCommerceSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearCommerce
        fields = ('years',)

class TopicCommerceSerializer(serializers.ModelSerializer):
    year = serializers.StringRelatedField(many=True)

    class Meta:
        model = Commerce
        fields = ('topic','year')

class SubjectClass10Serializer(serializers.ModelSerializer):
    class Meta:
        model = Class10
        fields = ('subject',)

class Class10Serializer(serializers.ModelSerializer):
    year = serializers.StringRelatedField(many=True)

    class Meta:
        model = Class10
        fields = ('qid','qclass','qno','subject','topic','question','image1','image2', 'year')

class TopicClass10Serializer(serializers.ModelSerializer):

    class Meta:
        model = Class10
        fields = ('topic',)

class yearClass10Serializer(serializers.ModelSerializer):
    class Meta:
        model = YearClass10
        fields = ('years',)

