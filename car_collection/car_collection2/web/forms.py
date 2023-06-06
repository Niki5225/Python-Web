from django import forms

from car_collection2.web.models import Profile, Car


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')

        widgets = {
            'password': forms.TextInput(attrs={'type': 'password'}),
        }

        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
            'password': 'Password',
        }


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

        labels = {
            'car_type': 'Type',
            'car_model': 'Model',
            'year': 'Year',
            'image_url': 'Image URL',
            'price': 'Price',
        }


class CarCreateForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

        labels = {
            'car_type': 'Type',
            'car_model': 'Model',
            'year': 'Year',
            'image_url': 'Image URL',
            'price': 'Price',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            return self.instance


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
            'password': 'Password',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()
            return self.instance
