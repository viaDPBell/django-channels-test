from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password(again)", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "is_admin")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("패스워드가 동일하지 않습니다.")
        return password2

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["email", "password"]


class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    ordering = ("id",)
    search_fields = ("email",)

    list_display = ("id", "email", "is_admin")
    list_filter = ("is_admin",)
    fieldsets = (("user default data", {"fields": ("email", "password", "name", "phone")}), ("account status", {"fields": ("is_del", "is_admin", "last_login")}))

    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)
