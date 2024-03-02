from django.contrib import admin

# Register your models here.

from django.contrib import admin

from django.utils.safestring import mark_safe

from .models import Recipe





@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Для списка рецептов"""

    list_display = ['display_id', 'title', 'cooking_time', 'author']
    list_filter = ['ingredients', 'cooking_time']
    readonly_fields = ['preview']
    search_fields = ['description']
    search_help_text = 'Поиск рецепта по описанию'

    """Для отдельного рецепта"""
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title']
            }
        ),
        (
            'Описание рецепта',
            {
                'description': 'Подробная информация о рецепте',
                'fields': ['description', 'cooking_steps', 'cooking_time'],
            }
        ),
        (
            'Ингредиенты',
            {
                'description': 'Ингредиенты для приготовления',
                'fields': ['ingredients'],
            }
        ),
        (
            'Загрузка изображения',
            {
                'description': 'Добавьте изображение для рецепта',
                'fields': ['image'],
            }
        ),
        (
            'Превью рецепта',
            {
                'fields': ['preview'],
            }
        ),
        (
            'Прочее',
            {
                'classes': ['collapse'],
                'description': 'Автор',
                'fields': ['author'],
            }
        ),
    ]

    def display_id(self, obj):
        return f"Рецепт №{obj.id}"

    display_id.short_description = 'Рецепт'

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width: 200px; height: auto;" alt="Изображения нет">')

    preview.short_description = 'Фото'


