from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexView(View):
    """ 获取首页 """
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        pass




