from django.shortcuts import render

from parsed_total_data.models import TotalData, SeasonData


def calc_money(stkOut, dbplay, homerun, balk, passedBall, error):
    money = (stkOut * 500) + (dbplay * 1000) + \
            (homerun * 1000) + (balk * 3000) + \
            (passedBall * 5000) + (error * 10000)

    return money

# Create your views here.
def index(request):
    total_data = SeasonData.objects.last()
    total_money = calc_money(total_data.stkOut, total_data.dbplay,
                             total_data.homerun, total_data.balk,
                             total_data.passedBall, total_data.error)

    total_money = str(format(total_money, ","))
    print(total_money)
    context = {'total_data':total_data, 'total_money':total_money}
    return render(request, 'index.html', context)

def history(request):
    m_history = TotalData.objects.all()
    s_data = SeasonData.objects.last()
    context = {'history':m_history, 'season':s_data}
    return render(request, 'history.html', context)

def patch_note(request):
    return render(request, 'patch_note.html')

def contact(request):
    return render(request, 'contact.html')