from django.db import models

# Create your models here.

# About/Profile
class About(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    about = models.ForeignKey(About, related_name='educations', on_delete=models.CASCADE)
    year = models.CharField(max_length=50)
    degree = models.CharField(max_length=150)
    institution = models.CharField(max_length=150)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Background(models.Model):
    about = models.ForeignKey(About, related_name='backgrounds', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    story = models.TextField()

    def __str__(self):
        return self.title

# Services
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title

# Skills
class SkillCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text='Icon class name (e.g., "fab fa-react")', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Projects
class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github = models.URLField(blank=True)
    demo = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title

class ProjectFeature(models.Model):
    project = models.ForeignKey(Project, related_name='features', on_delete=models.CASCADE)
    feature = models.CharField(max_length=200)

    def __str__(self):
        return self.feature

class ProjectStat(models.Model):
    project = models.OneToOneField(Project, related_name='stats', on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(default=0)
    forks = models.PositiveIntegerField(default=0)
    contributors = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Stats for {self.project.title}"

class ProjectTag(models.Model):
    project = models.ForeignKey(Project, related_name='tags', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Experience
class Experience(models.Model):
    TYPE_CHOICES = [
        ('work', 'Work'),
        ('certification', 'Certification'),
        ('project', 'Project'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='experience_icons/', blank=True)
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.role} at {self.company}"

class ExperienceDetail(models.Model):
    experience = models.ForeignKey(Experience, related_name='details', on_delete=models.CASCADE)
    detail = models.CharField(max_length=200)

    def __str__(self):
        return self.detail

class ExperienceSkill(models.Model):
    experience = models.ForeignKey(Experience, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Resume
class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume uploaded at {self.uploaded_at}" 

# Blog
class Blog(models.Model):
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='blogs/')
    excerpt = models.TextField()
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    read_time = models.PositiveIntegerField(help_text='Estimated reading time in minutes')
    url = models.URLField(blank=True)
    category = models.CharField(max_length=100)
    author = models.ForeignKey('BlogAuthor', related_name='blogs', on_delete=models.SET_NULL, null=True, blank=True)
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['order', '-published_date']

    def __str__(self):
        return self.title

class BlogAuthor(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='blog_authors/', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class BlogTag(models.Model):
    blog = models.ForeignKey(Blog, related_name='tags', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Contact
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

# Social Media
class SocialMedia(models.Model):
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
    ]
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon = models.CharField(max_length=50, help_text='Icon class name (e.g., "fab fa-github")')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Social Media Links"

    def __str__(self):
        return f"{self.get_platform_display()} - {self.url}"

#testimonial data 
class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    client_image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.client_name} - {self.company}"

# Hero Section Data
class HeroSectionData(models.Model):
    name = models.CharField(max_length=100, help_text="Your name for the Hero section.")
    tagline = models.CharField(max_length=150, help_text="Your tagline or short title.")
    description = models.TextField(help_text="The main descriptive text for the Hero section.")
    profile_picture = models.ImageField(upload_to='hero_profile_pics/', help_text="Profile picture for the Hero section.")

    class Meta:
        verbose_name = "Hero Section Data"
        verbose_name_plural = "Hero Section Data"

    def __str__(self):
        return f"{self.name} - Hero Data"
