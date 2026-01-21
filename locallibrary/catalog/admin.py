from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Author)
class AuthorInline(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [AuthorInline]
    fields = ('first_name', 'last_name', ('date_of_birth', 'date_of_death'))
                
            
            
            

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'due_back', 'id', 'borrower')
    
    fieldsets = (
            ('Informations', {
                'fields': ('book','imprint', 'id'),
                
                }),
            ('Availability', {
                'fields': ('status', 'due_back', 'borrower'),
                }
            ))
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)
