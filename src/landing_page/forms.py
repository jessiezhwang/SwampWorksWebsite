from django import forms
from django.forms import inlineformset_factory
from .models import Project, ProjectImage, ProjectMember, Idea, ClubMeeting, Contact


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleImageField(forms.ImageField):
    """An image field that accepts several files and returns a list of them."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        clean_one = super().clean
        if isinstance(data, (list, tuple)):
            if not data:
                return clean_one(None, initial)
            return [clean_one(item, initial) for item in data]
        return [clean_one(data, initial)]


class ProjectForm(forms.ModelForm):
    images = MultipleImageField(
        label='Photos',
        help_text='Select one or more photos of the project.',
    )

    class Meta:
        model = Project
        fields = ['title', 'description', 'technologies']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Project title'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe your project...'}),
            'technologies': forms.TextInput(attrs={'placeholder': 'Python, Pygame, Arduino'}),
        }


ProjectMemberFormSet = inlineformset_factory(
    Project,
    ProjectMember,
    fields=['name', 'role'],
    extra=5,
    can_delete=False,
    widgets={
        'name': forms.TextInput(attrs={'placeholder': 'Name'}),
        'role': forms.TextInput(attrs={'placeholder': 'Role'}),
    },
)


class ProjectEditForm(forms.ModelForm):
    new_images = MultipleImageField(
        label='Add more photos',
        required=False,
        help_text='Select one or more photos to add.',
    )
    delete_images = forms.ModelMultipleChoiceField(
        queryset=ProjectImage.objects.none(),
        required=False,
    )

    class Meta:
        model = Project
        fields = ['title', 'description', 'technologies', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['delete_images'].queryset = self.instance.images.all()

    def clean(self):
        cleaned = super().clean()
        remaining = self.instance.images.count() - len(cleaned.get('delete_images') or [])
        added = len(cleaned.get('new_images') or [])
        if remaining + added < 1:
            raise forms.ValidationError('A project needs at least one photo.')
        return cleaned


EditMemberFormSet = inlineformset_factory(
    Project,
    ProjectMember,
    fields=['name', 'role'],
    extra=3,
    can_delete=True,
    widgets={
        'name': forms.TextInput(attrs={'placeholder': 'Name'}),
        'role': forms.TextInput(attrs={'placeholder': 'Role'}),
    },
)


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Share a project idea...'}),
        }


class MeetingForm(forms.ModelForm):
    class Meta:
        model = ClubMeeting
        fields = ['title', 'description', 'date', 'time']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Optional details...'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'role', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Secretary'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
        }