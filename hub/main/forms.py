from django import forms

from .models import RegistrationLocation, Location, Comentary


class preReg(forms.ModelForm):

    class Meta:
        model = RegistrationLocation
        fields = ('location', 'course_name', 'course_org', 'inform', 'email', 'many_course')


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ('location_name', 'location_present',)


class ComentaryForm(forms.ModelForm):

    class Meta:
        model = Comentary
        fields = ('location', 'comentary', 'name', 'email',)