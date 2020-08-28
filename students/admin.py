from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User
from .models import Syllabus, leftWhere, YearClass10, Class10Answer, ScienceAnswer, CommerceAnswer, ImageClass10, ImageCommerce, ImageScience, StudentDetail, SolvedQuest, BookmarkQuest, Subject, YearCommerce, YearScience, Science, Commerce, Class10


# Register your models here.

admin.site.register(leftWhere)
admin.site.register(Subject)
admin.site.register(Class10Answer)
admin.site.register(ScienceAnswer)
admin.site.register(CommerceAnswer)
admin.site.register(ImageClass10)
admin.site.register(ImageCommerce)
admin.site.register(ImageScience)
admin.site.register(SolvedQuest)
admin.site.register(Syllabus)
admin.site.register(BookmarkQuest)
admin.site.register(StudentDetail)
admin.site.register(Commerce)
admin.site.register(Class10)
admin.site.register(Science)
admin.site.register(YearScience)
admin.site.register(YearClass10)
admin.site.register(YearCommerce)
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
