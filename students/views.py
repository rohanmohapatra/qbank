from rest_framework import generics, permissions
from knox.models import AuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Syllabus, StudentDetail, Subject, Science, YearScience, BookmarkQuest
from .models import Profile, YearCommerce, Commerce, Class10, YearClass10, SolvedQuest
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer, SubjectSerializer, SyllabusSerializer , StudentCreateSerializer,   StudentSerializer
from .serializers import ScienceSerializer, yearScienceSerializer, SubjectSienceSerializer, CommerceSerializer, yearCommerceSerializer
from .serializers import SubjectCommerceSerializer, SubjectClass10Serializer, Class10Serializer, ProfileSerializer, BookmarkSerializer
from .serializers import TopicClass10Serializer, TopicCommerceSerializer, TopicScienceSerializer, yearClass10Serializer, SolvedSerializer

#Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

#Resgiter API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

#Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Syllabus
class SyllList(generics.ListCreateAPIView):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer


class SyllDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a student instance.
    """
    serializer_class = StudentSerializer
    lookup_url_kwarg = 'pk'
    lookup_field = 'user_id'
    queryset = StudentDetail.objects.all()

    def put(self, request, *args, **kwargs):
        kwargs['partial'] = True 
        return self.update(request, *args, **kwargs)

class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    lookup_url_kwarg = 'pk'
    lookup_field = 'user_id'
    queryset = Profile.objects.all()

class SubjectList(APIView):
    """
    Retrieve teachers list instance.
    """

    def get_object(self, syll_id):
        try:
            return Subject.objects.filter(syllabus_id=syll_id)
        except Subject.DoesNotExist:
            raise Http404

    def get(self, request, syll_id, format=None):
        subject = self.get_object(syll_id)
        serializer = SubjectSerializer(subject, many=True)
        return Response(serializer.data)

class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset =  StudentDetail.objects.all()

class ProfileList(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset =  Profile.objects.all()

class BookmarkList(APIView):
    def get_object(self, user):
        try:
            return BookmarkQuest.objects.filter(user=user)
        except BookmarkQuest.DoesNotExist:
            raise Http404

    def get(self, request, user, format=None):
        bookmark = self.get_object(user)
        serializer = BookmarkSerializer(bookmark, many=True)
        return Response(serializer.data)

class SolvedList(APIView):
    def get_object(self, user):
        try:
            return SolvedQuest.objects.filter(user=user)
        except SolvedQuest.DoesNotExist:
            raise Http404

    def get(self, request, user, format=None):
        bookmark = self.get_object(user)
        serializer = SolvedSerializer(bookmark, many=True)
        return Response(serializer.data)

class CreateBookmark(generics.ListCreateAPIView):
    serializer_class = BookmarkSerializer
    queryset = BookmarkQuest.objects.all()

class CreateSolved(generics.ListCreateAPIView):
    serializer_class = SolvedSerializer
    queryset = SolvedQuest.objects.all()

class BookmarkDelete(APIView):
    def get_object(self, user, qid):
        try:
            return BookmarkQuest.objects.filter(user=user, qid=qid)
        except BookmarkQuest.DoesNotExist:
            raise Http404

    def delete(self, request, user, qid, *args, **kwargs):
        bookmark = self.get_object(user, qid)
        bookmark.delete()
        return Response("Bookmark deleted")

class SubjectSience(generics.ListCreateAPIView):
    queryset = Science.objects.values('subject').distinct()
    serializer_class = SubjectSienceSerializer

class ScienceView(generics.ListAPIView):
    serializer_class = ScienceSerializer
    def get_queryset(self):
        sub = self.kwargs['subject']
        queryset = Science.objects.filter(subject=sub)
        return queryset

class ScienceYear(generics.ListAPIView):
    queryset = YearScience.objects.values('years').distinct()
    serializer_class = yearScienceSerializer

class TopicScience(generics.ListAPIView):
    serializer_class = TopicScienceSerializer
    def get_queryset(self):
        sub = self.kwargs['subject']
        queryset = Science.objects.filter(subject=sub)
        return queryset

class SubjectCommerce(generics.ListCreateAPIView):
    queryset = Commerce.objects.values('subject').distinct()
    serializer_class = SubjectCommerceSerializer

class CommerceView(generics.ListAPIView):
    serializer_class = CommerceSerializer
    def get_queryset(self):
        sub = self.kwargs['subject']
        queryset = Commerce.objects.filter(subject=sub)
        return queryset

class CommerceYear(generics.ListAPIView):
    queryset = YearCommerce.objects.values('years').distinct()
    serializer_class = yearCommerceSerializer

class TopicCommerce(generics.ListAPIView):
    serializer_class = TopicCommerceSerializer
    def get_queryset(self):
        sub = self.kwargs['subject']
        queryset = Commerce.objects.filter(subject=sub)
        return queryset

class SubjectClass10(generics.ListCreateAPIView):
    queryset = Class10.objects.values('subject').distinct()
    serializer_class = SubjectClass10Serializer

class Class10View(generics.ListAPIView):
    serializer_class = Class10Serializer
    def get_queryset(self):
        sub = self.kwargs['subject']
        queryset = Class10.objects.filter(subject=sub)
        return queryset

class TopicClass10(generics.ListAPIView):
    serializer_class = TopicClass10Serializer
    def get_queryset(self):
        sub = self.kwargs['subject']
        queryset = Class10.objects.filter(subject=sub)
        return queryset

class Class10Year(generics.ListAPIView):
    queryset = YearClass10.objects.values('years').distinct()
    serializer_class = yearClass10Serializer