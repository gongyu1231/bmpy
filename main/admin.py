from django.contrib import admin

from .models import adduser, points, consume
# Register your models here.
class adduserAdmin(admin.ModelAdmin):
    list_display = ('name','ename', 'company', 'money',)

class pointsAdmin(admin.ModelAdmin):
    list_display = ('name', 'money', 'total', 'pointstimes')

class consumeAdmin(admin.ModelAdmin):
    list_display = ('consumename', 'amount', 'add', 'consumetimes',)


admin.site.register(adduser, adduserAdmin)
admin.site.register(points,pointsAdmin)
admin.site.register(consume, consumeAdmin)