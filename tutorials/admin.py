from django.contrib import admin
#from tutorials.models import User, Belt, StudentBelt, ServiceDojo, Lesson, StudentLesson, Photo, ServiceDojoStudent
from tutorials.models import User, Belt, ServiceDojo, Lesson, StudentLesson, Photo, ServiceDojoStudent, ServiceDojoStudentBelt

from django import forms

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

'''
class StudentBeltAdmin(admin.ModelAdmin):
    list_display = ['student', 'belt', 'examDate', 'calification']
    list_filter = ('calification',)

    search_fields = ('belt',)
    ordering = ('belt',)
    filter_horizontal = ()
'''
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    #username = forms.CharField(label='username')

    class Meta:
        model = User
        fields = ('username',)


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_staff', 'user_permissions', 'points', 'phone', 'dateofBirth')

    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Personal', {'fields': ('phone', 'points', 'belt')}),
        ('Progress', {'fields': ('points', 'belt')}),
        ('Permissions', {'fields': ('is_staff')}),
    )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('completeName', 'username','email', 'is_staff', 'points', )
    list_filter = ('is_staff','to_delete')
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Personal ', {'fields': ('completeName','dni', 'phone', 'dateofBirth')}),
        ('Progress ', {'fields': ('points',)}),
        ('Status ', {'fields': ('to_delete',)}),
        ('Permissions', {'fields': ('is_staff','user_permissions')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()




class ServiceDojoStudentBeltAdmin(admin.ModelAdmin):
    list_display = ['studentService', 'belt', 'examDate', 'calification']
    list_filter = ('calification',)

    search_fields = ('belt',)
    ordering = ('belt',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Belt)
#admin.site.register(StudentBelt, StudentBeltAdmin)
admin.site.register(ServiceDojoStudentBelt, ServiceDojoStudentBeltAdmin)
admin.site.register(ServiceDojoStudent)
admin.site.register(ServiceDojo)
admin.site.register(Lesson)
admin.site.register(StudentLesson)
admin.site.register(Photo)




# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)