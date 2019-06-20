from django.shortcuts import render
from django.contrib.auth.decorators import login_required.


def index(request):

    return render(request, 'display/index.html')
@login_required(login_url='/accounts/login/')
def article(request, article_id):
