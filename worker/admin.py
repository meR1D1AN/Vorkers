from django.contrib import admin
from .models import Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        "last_name",
        "team_number",
        "salary",
        "specialization",
    )
    search_fields = (
        "last_name",
        "team_number",
        "specialization",
    )
    list_filter = (
        "team_number",
        "specialization",
    )
