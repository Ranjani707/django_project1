from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
def tom(request):
    return HttpResponse('Tom and Jerry is a remarkable and one of the top 10 most famous cartoons in India.')
def shinchan(request):
    return HttpResponse('<h1>Shinchan, a 5-year-old boy, is featured in this cartoon. Shinchan has many friends.</h1>')
def tushitha(request):
    return HttpResponse('<h1><marquee>tushitha is studying in little elly</h1></marquee>')
def nature(request):
    return HttpResponse('<img src="https://www.bsr.org/images/heroes/bsr-focus-nature-hero.jpg" width="200px" height="200px">')
