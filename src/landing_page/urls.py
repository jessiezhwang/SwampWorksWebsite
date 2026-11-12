from django.urls import path, include
from . import views

app_name = 'landing_page'

urlpatterns = [
    path('', views.index, name='index'),
    path('meetings/<int:meeting_id>/delete/', views.delete_meeting, name='delete_meeting'),
    path('about/', views.index, name='about'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('projects/<int:project_id>/tasks/add/', views.task_add, name='task_add'),
    path('tasks/<int:task_id>/edit/', views.task_update, name='task_update'),
    path('tasks/<int:task_id>/move/', views.task_move, name='task_move'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('projects/<int:project_id>/status/', views.update_project_status, name='update_project_status'),
    path('projects/<int:project_id>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:project_id>/approve/', views.approve_project, name='approve_project'),
    path('projects/<int:project_id>/reject/', views.reject_project, name='reject_project'),
    path('projects/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('ideas/<int:idea_id>/delete/', views.delete_idea, name='delete_idea'),
    path('ideas/', views.ideas, name='ideas'),
    path('contact/', views.contact, name='contact'),
    path('contact/<int:contact_id>/delete/', views.delete_contact, name='delete_contact'),
]