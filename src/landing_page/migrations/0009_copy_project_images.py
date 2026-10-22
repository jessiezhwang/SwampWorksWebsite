from django.db import migrations


def copy_images(apps, schema_editor):
    Project = apps.get_model('landing_page', 'Project')
    ProjectImage = apps.get_model('landing_page', 'ProjectImage')

    for project in Project.objects.all():
        if not project.title:
            project.title = project.description[:50]
            project.save(update_fields=['title'])
        if project.image:
            ProjectImage.objects.create(project=project, image=project.image.name)


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0008_project_details'),
    ]

    operations = [
        migrations.RunPython(copy_images, migrations.RunPython.noop),
    ]
