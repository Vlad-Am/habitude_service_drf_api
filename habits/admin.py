from django.contrib import admin

from habits.models import Habits


@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = ('owner', 'action', "time", "place", "data", )
    list_filter = ('data',)
