from django.contrib import admin
from . models import LatestNews, BangladeshNews, PoliticsNews,WorldNews,SportsNews,TradeNews,TechnologyNews,EntertainmentNews

# Register your models here.
class NewsBaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'title', 'desc', 'date']


@admin.register(LatestNews)
class latest(NewsBaseAdmin):
    pass


@admin.register(BangladeshNews)
class b_desh(NewsBaseAdmin):
    pass

@admin.register(PoliticsNews)
class politics(NewsBaseAdmin):
    pass

@admin.register(WorldNews)
class world(NewsBaseAdmin):
    pass

@admin.register(SportsNews)
class Sports(NewsBaseAdmin):
    pass

@admin.register(TradeNews)
class Trade(NewsBaseAdmin):
    pass

@admin.register(TechnologyNews)
class Technology(NewsBaseAdmin):
    pass

@admin.register(EntertainmentNews)
class Entertainment(NewsBaseAdmin):
    pass