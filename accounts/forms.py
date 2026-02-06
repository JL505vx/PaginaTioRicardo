from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class RegistroPacienteForm(UserCreationForm):
    """
    Registro para pacientes: fija el rol en 'paciente'.
    """

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.rol = CustomUser.ROLE_PACIENTE
        if commit:
            user.save()
        return user


class RegistroDoctorForm(UserCreationForm):
    """
    Registro para doctor: fija el rol en 'doctor'.
    """

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.rol = CustomUser.ROLE_DOCTOR
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    """
    Login base para ambos roles. Se personaliza el template por vista.
    """

    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contrasena', widget=forms.PasswordInput)


class MensajePrivadoForm(forms.Form):
    """
    Formulario simple para enviar mensajes privados.
    """

    cuerpo = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={'rows': 4}),
    )
