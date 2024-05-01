from django.contrib import admin
from .models import Category,Product,Commande

admin.site.site_header = "Bi3smart"
admin.site.site_title = "Bi3smart"
admin.site.index_title = "Manageur"

class AdminCategorie(admin.ModelAdmin):
    list_display=('name','date_added')

class AdminProduct(admin.ModelAdmin):
    list_display=('title','price','category','date_added')
    search_fields = ('title',)
    list_editable = ('price',)

class AdminCommande(admin.ModelAdmin):
    list_display=('items','nom','email','address','ville','pays','total','zipcode','date_commande')



admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
admin.site.register(Commande, AdminCommande)
