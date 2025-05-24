from rest_framework import serializers
from .models import (
    About, Education, Background, Service, SkillCategory, Skill,
    Project, ProjectFeature, ProjectStat, ProjectTag, Experience,
    ExperienceDetail, ExperienceSkill, Resume, Blog, BlogTag,
    ContactMessage, BlogAuthor, SocialMedia, Testimonial, HeroSectionData
)

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'year', 'degree', 'institution', 'details']

class BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        fields = ['id', 'title', 'story']

class AboutSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=True, read_only=True)
    backgrounds = BackgroundSerializer(many=True, read_only=True)

    class Meta:
        model = About
        fields = ['id', 'name', 'title', 'profile_picture', 'bio', 'educations', 'backgrounds']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'image']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'icon', 'description']

class SkillCategorySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = SkillCategory
        fields = ['id', 'name', 'skills']

class ProjectFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFeature
        fields = ['id', 'feature']

class ProjectTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTag
        fields = ['id', 'name']

class ProjectStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStat
        fields = ['id', 'stars', 'forks', 'contributors']

class ProjectSerializer(serializers.ModelSerializer):
    features = ProjectFeatureSerializer(many=True, read_only=True)
    tags = ProjectTagSerializer(many=True, read_only=True)
    stats = ProjectStatSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'image', 'github', 'demo', 'features', 'tags', 'stats']

class ExperienceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceDetail
        fields = ['id', 'detail']

class ExperienceSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceSkill
        fields = ['id', 'name']

class ExperienceSerializer(serializers.ModelSerializer):
    details = ExperienceDetailSerializer(many=True, read_only=True)
    skills = ExperienceSkillSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = ['id', 'type', 'role', 'company', 'duration', 'description', 'icon', 'details', 'skills']

class ResumeSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Resume
        fields = ['id', 'file', 'file_url', 'uploaded_at']

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file and hasattr(obj.file, 'url'):
            return request.build_absolute_uri(obj.file.url) if request else obj.file.url
        return None

class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = ['id', 'name']

class BlogAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogAuthor
        fields = ['id', 'name', 'avatar', 'bio']

class BlogSerializer(serializers.ModelSerializer):
    tags = BlogTagSerializer(many=True, read_only=True)
    author = BlogAuthorSerializer(read_only=True, required=False)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'cover_image', 'excerpt', 'content', 'published_date', 'read_time', 'url', 'category', 'author', 'tags']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not instance.author:
            representation.pop('author', None)
        return representation

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message', 'sent_at']
        read_only_fields = ['sent_at']

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['id', 'platform', 'url', 'icon', 'is_active', 'order']

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class HeroSectionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSectionData
        fields = '__all__' 