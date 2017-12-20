from django import forms
from facturacionapp.models.profile import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'role',
        ]
        labels = {
            'role': 'Rol del usuario',
        }
        widgets = {
            'role': forms.Select(),
        }
