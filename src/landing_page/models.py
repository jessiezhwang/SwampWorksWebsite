from django.db import models


class Project(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=200, default='')
    description = models.TextField()
    technologies = models.CharField(
        max_length=300,
        blank=True,
        help_text='Comma-separated, e.g. Python, Pygame, Arduino',
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ongoing')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title or self.description[:50]

    def technology_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]


class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.name} ({self.role})"


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"Image for {self.project}"


class Idea(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.description[:50]


class ClubMeeting(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f"{self.title} ({self.date})"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.name} ({self.role})"