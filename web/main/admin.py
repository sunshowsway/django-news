from django.contrib import admin
from .models import Post, Template
from .views import post_template


# Register your models here.


class TemplateAdmin(admin.ModelAdmin):
    def mark_as_default_template(modeladmin, request, queryset):
        if len(queryset) == 0:
            return
        else:
            template_string = queryset[0].content
            post_template[0] = "{% extends 'main/base.html' %}" + \
                               "{% block content %}" + template_string + \
                               "{% endblock %}"

    mark_as_default_template.short_description = '设置为新闻模板'
    actions = [mark_as_default_template]


admin.site.register(Post)
admin.site.register(Template, TemplateAdmin)
