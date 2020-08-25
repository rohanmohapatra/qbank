from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User
from .models import Syllabus, Image, StudentDetail, SolvedQuest, BookmarkQuest, Subject, YearCommerce, YearScience, Science, Commerce, Class10, AnswersCommerce, AnswersScience, AnswersClass10

# Register your models here.

admin.site.register(Subject)
admin.site.register(Image)
admin.site.register(SolvedQuest)
admin.site.register(Syllabus)
admin.site.register(BookmarkQuest)
admin.site.register(StudentDetail)
admin.site.register(Commerce)
admin.site.register(Class10)
admin.site.register(Science)
admin.site.register(YearScience)
admin.site.register(YearCommerce)
admin.site.register(AnswersScience)
admin.site.register(AnswersCommerce)
admin.site.register(AnswersClass10)
@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)