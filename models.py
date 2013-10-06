from django.db import models
from django.utils.translation import ugettext_lazy as _

class DDUser(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    
class Issue(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(DDUser, related_name="user")
    text = models.TextField()
    thresshold = models.IntegerField(default=5000)
    positive = models.IntegerField(default = 0)
    negative = models.IntegerField(default = 0)
    neutral = models.IntegerField(default = 0)

class Comment(models.Model):
    issue = models.ForeignKey(Issue, related_name="comments")
    category = models.TextField(blank=True)
    author = models.ForeignKey(DDUser)
    content = models.TextField(blank=True)
    vote_up = models.IntegerField(default=0)
    vote_down = models.IntegerField(default=0)
    
class RelatedLink(models.Model):
    issue = models.ForeignKey(Issue, related_name="related_links")
    author = models.ForeignKey(DDUser)
    title = models.TextField(blank=True)
    content = models.TextField(blank=True) 
    #could be URL field
    vote_up = models.IntegerField(default=0)
    vote_down = models.IntegerField(default=0)

   

    