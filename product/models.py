from django.db import models
from . import json_data
# Create your models here.

class product(models.Model):
    product_name=models.CharField(max_length=40)
    product_detail=models.CharField(max_length=100)
    
class products(models.Model):
    name=models.CharField(max_length=50)
    date=models.DateField()
    detail=models.TextField()

class Dashboard(models.Model):
    start_year = models.CharField(null=True,max_length=100)
    end_year = models.CharField(null=True,max_length=100)
    sector = models.CharField(max_length=10,null=True)
    topic = models.CharField(max_length=100,null=True)
    insight = models.CharField(max_length=100,null=True)
    url = models.URLField(max_length=100,null=True)
    impact = models.CharField(max_length=100,null=True)
    added = models.CharField(max_length=100,null=True)
    published = models.CharField(max_length=100,null=True)
    country = models.CharField(max_length=100,null=True)
    relevance = models.CharField(max_length=100,null=True)
    source = models.CharField(max_length=100,null=True)
    pestle = models.CharField(max_length=100,null=True)
    title = models.TextField(max_length=100,null=True)
    likelihood = models.CharField(max_length=10,null=True)
    region = models.CharField(max_length=100,null=True)
    intensity = models.CharField(max_length=10,null=True)

# print(len(json_data.data))
# length_of_d = 0
# for i in json_data.data:
    
    # d = Dashboard()
    # if(length_of_d > 100):
    #     break
    
    # for k,v in i.items():
    #     setattr(d,k,v)
    
    # d.save()
    # length_of_d+=1
# print(length_of_d)

attributes = ['end_year', 'intensity', 'sector', 'topic', 'insight', 'url', 'region', 'start_year', 'impact', 'added', 'published', 'country', 'relevance', 'pestle', 'source', 'title', 'likelihood']
