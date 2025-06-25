from django.contrib import admin

from .models import Post , Author , Tag , Player , Match , Transfer , Rumor , Legend


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author" , "tag" , "date",)
    list_display = ("title" ,"author" , "date",)
    prepopulated_fields = {"slug": ("title",)}



@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'from_team', 'to_team', 'fee', 'date')


@admin.register(Rumor)
class RumorAdmin(admin.ModelAdmin):
    list_display = ("player_name", "from_team", "credibility", "source", "date")
    search_fields = ("player_name", "from_team", "source")
    list_filter = ("date", "credibility")

@admin.register(Legend)
class LegendAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "years_active")



admin.site.register(Post , PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Player)
admin.site.register(Match)


# Register your models here.
