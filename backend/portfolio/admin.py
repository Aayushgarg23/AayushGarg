from django.contrib import admin
from .models import (
    About, Education, Background, Service, SkillCategory, Skill, Project, ProjectFeature, ProjectStat, ProjectTag,
    Experience, ExperienceDetail, ExperienceSkill, Resume, Blog, BlogAuthor, BlogTag, ContactMessage, SocialMedia, Testimonial,
    HeroSectionData
)

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class BackgroundInline(admin.TabularInline):
    model = Background
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [EducationInline, BackgroundInline]
    list_display = ("name", "title")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    inlines = [SkillInline]
    list_display = ("name",)

class ProjectFeatureInline(admin.TabularInline):
    model = ProjectFeature
    extra = 1

class ProjectTagInline(admin.TabularInline):
    model = ProjectTag
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectFeatureInline, ProjectTagInline]
    list_display = ("title",)

@admin.register(ProjectStat)
class ProjectStatAdmin(admin.ModelAdmin):
    list_display = ("project", "stars", "forks", "contributors")

class ExperienceDetailInline(admin.TabularInline):
    model = ExperienceDetail
    extra = 1

class ExperienceSkillInline(admin.TabularInline):
    model = ExperienceSkill
    extra = 1

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperienceDetailInline, ExperienceSkillInline]
    list_display = ("role", "company", "type", "duration")

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("file", "uploaded_at")

class BlogTagInline(admin.TabularInline):
    model = BlogTag
    extra = 1

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogTagInline]
    list_display = ("title", "published_date", "category", "author")
    list_filter = ("category", "published_date", "author")
    search_fields = ("title", "content", "excerpt")
    date_hierarchy = "published_date"

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "sent_at")

@admin.register(BlogAuthor)
class BlogAuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name", "bio")

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("platform", "url", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("platform", "is_active")
    search_fields = ("platform", "url")

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'rating', 'is_active', 'order', 'created_at')
    list_filter = ('is_active', 'rating', 'created_at')
    search_fields = ('client_name', 'company', 'content')
    list_editable = ('is_active', 'order')
    ordering = ('order', '-created_at')
    fieldsets = (
        ('Client Information', {
            'fields': ('client_name', 'client_position', 'company', 'client_image')
        }),
        ('Testimonial Content', {
            'fields': ('content', 'rating')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'order')
        }),
    )

@admin.register(HeroSectionData)
class HeroSectionDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline', 'profile_picture')
    fieldsets = (
        (None, {
            'fields': ('name', 'tagline', 'description', 'profile_picture')
        }),
    )
