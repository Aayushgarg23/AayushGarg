from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    About, Education, Background, Service, SkillCategory, Skill,
    Project, ProjectFeature, ProjectStat, ProjectTag, Experience,
    ExperienceDetail, ExperienceSkill, Resume, Blog, BlogTag,
    ContactMessage, SocialMedia, Testimonial, HeroSectionData
)
from .serializers import (
    AboutSerializer, EducationSerializer, BackgroundSerializer,
    ServiceSerializer, SkillCategorySerializer, SkillSerializer,
    ProjectSerializer, ProjectFeatureSerializer, ProjectStatSerializer,
    ProjectTagSerializer, ExperienceSerializer, ExperienceDetailSerializer,
    ExperienceSkillSerializer, ResumeSerializer, BlogSerializer,
    BlogTagSerializer, ContactMessageSerializer, SocialMediaSerializer,
    TestimonialSerializer, HeroSectionDataSerializer
)
from django.http import FileResponse

# Create your views here.

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return About.objects.all()[:1]  # Only return the first about entry

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]

class SkillCategoryViewSet(viewsets.ModelViewSet):
    queryset = SkillCategory.objects.all()
    serializer_class = SkillCategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_projects = self.queryset[:3]  # Get first 3 projects
        serializer = self.get_serializer(featured_projects, many=True)
        return Response(serializer.data)

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_experiences = self.queryset[:3]  # Get first 3 experiences
        serializer = self.get_serializer(featured_experiences, many=True)
        return Response(serializer.data)

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Resume.objects.all()[:1]  # Only return the latest resume

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        resume = self.get_object()
        if resume.file:
            response = FileResponse(resume.file, as_attachment=True)
            response['Content-Disposition'] = f'attachment; filename="{resume.file.name}"'
            return response
        return Response({'error': 'Resume file not found'}, status=404)

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_blogs = self.queryset[:3]  # Get first 3 blogs
        serializer = self.get_serializer(featured_blogs, many=True)
        return Response(serializer.data)

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def perform_create(self, serializer):
        # Simply save the message without sending email
        serializer.save()

class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.filter(is_active=True)
    serializer_class = SocialMediaSerializer
    permission_classes = [IsAdminOrReadOnly]

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.AllowAny]

class HeroSectionDataViewSet(viewsets.ModelViewSet):
    queryset = HeroSectionData.objects.all()
    serializer_class = HeroSectionDataSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        # Only return the first entry, as there should only be one for the hero section
        return HeroSectionData.objects.all()[:1]
