#https://sports.news.naver.com/kbaseball/schedule/index?date=20220714&month=06&year=2022&teamCode=
from bs4 import BeautifulSoup
import requests
import calendar
def kboscorelist(teamname, year, month) :
    def deleteBalise(string):
        for i in range(2):
            # identifying  <
            rankBegin = 0
            for carac in string:
                if carac == '<':
                    break
                rankBegin += 1
            # identifying  >
            rankEnd = 0
            for carac in string:
                if carac == '>':
                    break
                rankEnd += 1
            stringToReplace = string[rankBegin:rankEnd+1]
            string = string.replace(stringToReplace,'')
        return string



    teamcode = {"전체":"", "KT" : "KT", "두산": "OB", "삼성":"SS", "LG":"LG", "키움":"WO", "SSG":"SK", "NC":"NC", "롯데":"LT", "기아":"HT", "한화":"HH"}
    team = teamcode[teamname]
    url = "https://sports.news.naver.com/kbaseball/schedule/index?&month=%s&year=%s&teamCode=%s"% (month, year, team)

    html = requests.get(url)
    parsar = BeautifulSoup(html.text, "html.parser")
    list = []
    for i in range(1, calendar.monthrange(int(year), int(month))[1]+1, 1) :
        tmplst = []
        if(i % 2 == 0) :
            for j in range(1, 7, 2) :
                if j != 3 :
                    res = parsar.select('div.sch_tb2:nth-child(%s) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > span:nth-child(%s)' % (str(i), str(j)))
                else :
                    res = parsar.select('div.sch_tb2:nth-child(%s) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > strong'% str(i))
                    res = deleteBalise(str(res))
                tmplst.append(deleteBalise(str(res)))
            #print(tmplst)
        else :
            for j in range(1, 7, 2) :
                if j != 3 :
                    res = parsar.select('div.sch_tb:nth-child(%s) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > span:nth-child(%s)' % (str(i), str(j)))
                else :
                    res = parsar.select('div.sch_tb:nth-child(%s) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > strong'% str(i))
                    res = deleteBalise(str(res))
                tmplst.append(deleteBalise(str(res)))
            #print(tmplst)
        list.append(str(i) + '일 | ' + " ".join(tmplst).replace('[','').replace(']',''))
    #print(list)
    return list
if __name__ == "__main__" :
    teamname = input()
    year = input()
    month = input()
    list = kboscorelist(teamname, year, month)
    print('%s년 %s월 %s 경기 결과 - '%(year, month, teamname))
    print('-'*30)
    for i in range(0, len(list), 1) :
        print(list[i])
#print(list)