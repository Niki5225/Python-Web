from django import forms

from exam1.web.models import Profile, Album


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
        }


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class AlbumCreateForm(AlbumBaseForm):
    widgets = {
        'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
        'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
        'description': forms.TextInput(attrs={'placeholder': 'Description'}),
        'price': forms.TextInput(attrs={'placeholder': 'Price'}),
        'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'})
    }


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(AlbumBaseForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Album.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()
