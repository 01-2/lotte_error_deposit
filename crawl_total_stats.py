import pandas as pd
import datetime

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lotte_error_deposit.settings")
import django
django.setup()

from parsed_total_data.models import TotalData, SeasonData

'''
    SO(Strike Outs/500) & DP(Double Plays/1000) : http://www.statiz.co.kr/stat.php?re=0&lr=5
    HR(Home Run/1000) & BK(Balk/3000) & PB(Passed Balls/5000) : http://www.statiz.co.kr/stat.php?re=1&lr=5
    E(Error/10000) : http://www.statiz.co.kr/stat.php?re=2&lr=5
'''

def calc_money(stkOut, dbplay, homerun, balk, passedBall, error):
    money = (stkOut * 500) + (dbplay * 1000) + \
            (homerun * 1000) + (balk * 3000) + \
            (passedBall * 5000) + (error * 10000)

    return money

def get_data() :
    df_bat = pd.read_html('http://www.statiz.co.kr/stat.php?re=0&lr=5')[0]
    df_pit = pd.read_html('http://www.statiz.co.kr/stat.php?re=1&lr=5')[0]
    df_def = pd.read_html('http://www.statiz.co.kr/stat.php?re=2&lr=5')[0]

    df_bat = df_bat.drop(df_bat.index[0:4])
    df_pit = df_pit.drop(df_pit.index[0:4])
    df_def = df_def.drop(df_def.index[0:4])


    col_list = []
    for i in range(0, df_bat.columns.size):
        col_list.append(df_bat.columns.values[i][2])

    df_bat.columns = col_list

    col_list = []
    for i in range(0, df_pit.columns.size):
        col_list.append(df_pit.columns.values[i][2])

    df_pit.columns = col_list

    col_list = []
    for i in range(0, df_def.columns.size):
        col_list.append(df_def.columns.values[i][2])

    df_def.columns = col_list


    df_bat = df_bat.loc[:, ~df_bat.columns.str.contains('^Unnamed')]
    df_pit = df_pit.loc[:, ~df_pit.columns.str.contains('^Unnamed')]
    df_def = df_def.loc[:, ~df_def.columns.str.contains('^Unnamed')]

    bat_lotte = df_bat[df_bat['이름'].isin(['롯데'])]
    pit_lotte = df_pit[df_pit['이름'].isin(['롯데'])]
    def_lotte = df_def[df_def['이름'].isin(['롯데'])]

    print(bat_lotte)
    print(pit_lotte)
    print(def_lotte)

    so_num = bat_lotte['삼진'].astype(int)
    dp_num = bat_lotte['병살'].astype(int)
    print('삼진 : {0} / 병살 : {1}'.format(so_num.values, dp_num.values))

    hr_num = pit_lotte['홈런'].astype(int)
    bk_num = pit_lotte['보크'].astype(int)
    pb_num = pit_lotte['폭투'].astype(int)
    print('피홈런 : {0} / 보크 : {1} / 폭투 : {2}'.format(hr_num.values, bk_num.values, pb_num.values))

    e_num = def_lotte['실책'].astype(int)
    print('실책 : {0}'.format(e_num.values))

    result = {'stkOut':so_num,
              'dbplay':dp_num,
              'homerun':hr_num,
              'balk':bk_num,
              'passedBall':pb_num,
              'error':e_num}

    return result

if __name__=='__main__':

    season_data = SeasonData.objects.last()
    total_data = get_data()

    if season_data is not None :
        diff_stkOut = int(total_data['stkOut']) - (getattr(season_data, 'stkOut'))
        diff_dbplay = int(total_data['dbplay']) - (getattr(season_data, 'dbplay'))
        diff_homerun = int(total_data['homerun']) - (getattr(season_data, 'homerun'))
        diff_balk = int(total_data['balk']) - (getattr(season_data, 'balk'))
        diff_passedBall = int(total_data['passedBall']) - (getattr(season_data, 'passedBall'))
        diff_error = int(total_data['error']) - (getattr(season_data, 'error'))

        print(diff_stkOut)

        # 실책이 발생한 날만 저장하도록 수정할 것
        TotalData(date = datetime.date.today(),
                  stkOut = diff_stkOut,
                  dbplay = diff_dbplay,
                  homerun = diff_homerun,
                  balk = diff_balk,
                  passedBall = diff_passedBall,
                  error = diff_error,
                  money = calc_money(diff_stkOut, diff_dbplay,
                                     diff_homerun, diff_balk,
                                     diff_passedBall, diff_error)).save()

        if getattr(season_data,'date') == datetime.date.today():
            SeasonData.objects.delete()

    SeasonData(date = datetime.date.today().year,
               stkOut = total_data['stkOut'],
               dbplay = total_data['dbplay'],
               homerun = total_data['homerun'],
               balk = total_data['balk'],
               passedBall = total_data['passedBall'],
               error = total_data['error'],
               money = calc_money(int(total_data['stkOut']),
                                  int(total_data['dbplay']),
                                  int(total_data['homerun']),
                                  int(total_data['balk']),
                                  int(total_data['passedBall']),
                                  int(total_data['error']))
               ).save()
