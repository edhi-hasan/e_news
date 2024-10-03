from django.db import models

# Create your models here.

class NewsBase(models.Model):
    image = models.ImageField(upload_to="news_images/")
    title = models.CharField(max_length=250)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

# Models inheriting from the base model
class LatestNews(NewsBase):
    pass

class BangladeshNews(NewsBase):
    pass

class PoliticsNews(NewsBase):
    pass

class WorldNews(NewsBase):
    pass

class SportsNews(NewsBase):
    pass

class TradeNews(NewsBase):
    pass

class TechnologyNews(NewsBase):
    pass

class EntertainmentNews(NewsBase):
    pass

