from django.forms import ModelForm, EmailInput, TextInput

from personas.models import Persona


class FormaPersona(ModelForm):
     class Meta:

        model = Persona
        fields = '__all__'
        widgets = {

            'email': EmailInput(attrs={'type': 'email'})


        }

# class FormaDomicilio(ModelForm):
#     class Meta:
#
#         model = Domicilio
#         fields = '__all__'
#         widgets = {
#
#             'no_domicilio' : TextInput(attrs={'type': 'number'})
#         }
#
#
#

