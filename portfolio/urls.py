from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'about', views.AboutViewSet)
router.register(r'services', views.ServiceViewSet)
router.register(r'skill-categories', views.SkillCategoryViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'experiences', views.ExperienceViewSet)
router.register(r'resume', views.ResumeViewSet)
router.register(r'blogs', views.BlogViewSet)
router.register(r'contact', views.ContactMessageViewSet)
router.register(r'social-media', views.SocialMediaViewSet)
router.register(r'testimonials', views.TestimonialViewSet)
router.register(r'hero-data', views.HeroSectionDataViewSet)

urlpatterns = router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 