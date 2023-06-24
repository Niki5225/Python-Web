from django import forms

from frutipedia_app.web.models import Profile, Fruit


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password')

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }


class FruitCreateForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.TextInput(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.TextInput(attrs={'placeholder': 'Nutrition Info'}),
        }

        labels = {
            'name': '',
            'nutrition': '',
            'image_url': '',
            'description': '',
        }


class FruitEditForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'

        labels = {
            'name': 'Name',
            'image_url': 'Image URL',
            'nutrition': 'Nutrition',
            'description': 'Description',
        }


class FruitDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    class Meta:
        model = Fruit
        fields = '__all__'

        labels = {
            'name': 'Name',
            'image_url': 'Image URL',
            'nutrition': 'Nutrition',
            'description': 'Description',
        }

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url', 'age')

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
            'age': 'Age'
        }


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        if commit:
            Profile.objects.all().delete()
            Fruit.objects.all().delete()

        return self.instance
