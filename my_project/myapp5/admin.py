from django.contrib import admin
from .models import Category, Product


@admin.action(description="Сбросить количество до нуля")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'category', 'quantity']
    ordering = ('category', '-quantity')
    list_filter = ['date_added', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю описание продукта (Description)'
    actions = [reset_quantity]

    """Отдельный продукт."""
    # fields = ['name', 'category', 'description', 'date_added', 'rating']
    readonly_fields = ['date_added', 'rating']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное опсиание',
                'fields': ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            },
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['date_added', 'rating'],
            },
        ),
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
