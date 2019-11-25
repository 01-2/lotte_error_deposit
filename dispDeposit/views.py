from django.shortcuts import render

from parsed_total_data.models import TotalData

# Create your views here.
def index(request):
    total_data = TotalData.objects.last()
    total_money = (total_data.stkOut * 500) + (total_data.dbplay * 1000) + \
                  (total_data.homerun * 1000) + (total_data.balk * 3000) + \
                  (total_data.passedBall * 5000) + (total_data.error * 10000)
    context = {'total_data':total_data, 'total_money':total_money}
    return render(request, 'index.html', context)

def history(request):
    return render(request, 'dispDeposit/history.html')

def patch_note(request):
    return render(request, 'dispDeposit/patch_note.html')

def contact(request):
    return render(request, 'contact.html')