from django.contrib import admin
from .models import User
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =('email','first_name', 'last_name')
    
    def clean_password2(self):
        password1 =self.cleaned_data.get("password1")
        password2 =self.cleaned_data.get("password2")
        if password1 and password2 and password1 !=password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user =super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
class UserChangeForm(forms.ModelForm):
    
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email','password','first_name', 'last_name', 'is_active','is_staff','is_superuser')

    def clean_password(self):
        return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    form = UserCreationForm
    add_form  = UserCreationForm
    
    list_display =('email','first_name','last_name','is_active','is_staff','is_superuser')

    list_filter=('is_superuser',)

    fieldsets = (
        
        (None,{'fields':('email','password')}),
        ('person info', {
            'fields': ('first_name','last_name',),
        }),
        ('permissions', {
            'fields':('is_staff','is_active','is_superuser'),
        })
    )

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('email','first_name','last_name','password1','password2')
        }),
    )

    search_fields =('email',)
    ordering = ('email',)
    filter_horizontal=()

admin.site.register(User,UserAdmin)
admin.site.unregister(Group)


