from django import forms

from my_plant_app.web.models import Profile, Plant


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class CreatePlantForm(PlantBaseForm):
    labels = {
        'plant_type': 'Type',
        'name': 'Name',
        'image_url': 'Image URL',
        'description': 'Description',
        'price': 'Price',
    }


class PlantEditForm(PlantBaseForm):
    pass


class PlantDeleteForm(PlantBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name')
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }


class CreateProfileForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(ProfileBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Plant.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()
