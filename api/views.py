from django.shortcuts import HttpResponse
import urllib.request as ur
import xmltodict
import json


def homepage(request):
    file = ur.urlopen('http://www.skiplan.com/php/getXmlInter.php?country=russia&region=alpes&resort=ROSA%20KHUTOR')
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    lifts = []
    list = data["RESORT"]["STATES"]["AREA"]
    for x in list:
        if 'LIFTS' == x['@nom_en']:
            for i in x['LIFT']:
                if i['@name_en'] == 'OLIMPIA':
                    if len(i['@state']) > 1:
                        lifts.append([1,  str(i['@state']).lower()])
                    else:
                        lifts.append([1,  str(i['@state']).upper()])

                elif i['@name_en'] == 'ZAPOVEDNYY LES':
                    if len(i['@state']) > 1:
                        lifts.append([2,  str(i['@state']).lower()])
                    else:
                        lifts.append([2,  str(i['@state']).upper()])

                elif i['@name_en'] == 'KAVKAZSKIY EXPRESS above 1600':

                    if len(i['@state']) > 1:
                        lifts.append([3,  str(i['@state']).lower()])
                    else:
                        lifts.append([3,  str(i['@state']).upper()])

                elif i['@name_en'] == 'KAVKAZSKIY EXPRESS below 1600':
                    if len(i['@state']) > 1:
                        lifts.append([4,  str(i['@state']).lower()])
                    else:
                        lifts.append([4,  str(i['@state']).upper()])

                elif i['@name_en'] == 'VOLCHYA SKALA':
                    if len(i['@state']) > 1:
                        lifts.append([5,  str(i['@state']).lower()])
                    else:
                        lifts.append([5,  str(i['@state']).upper()])
                elif i['@name_en'] == 'BESEDA':
                    if len(i['@state']) > 1:
                        lifts.append([6,  str(i['@state']).lower()])
                    else:
                        lifts.append([6,  str(i['@state']).upper()])

                elif i['@name_en'] == 'KVARTET':
                    if len(i['@state']) > 1:
                        lifts.append([7,  str(i['@state']).lower()])
                    else:
                        lifts.append([7,  str(i['@state']).upper()])
                elif i['@name_en'] == 'SKAZKA':
                    if len(i['@state']) > 1:
                        lifts.append([8,  str(i['@state']).lower()])
                    else:
                        lifts.append([8,  str(i['@state']).upper()])

                elif i['@name_en'] == 'KABAN':
                    if len(i['@state']) > 1:
                        lifts.append([9,  str(i['@state']).lower()])
                    else:
                        lifts.append([9,  str(i['@state']).upper()])
                elif i['@name_en'] == 'EXTREME':
                    if len(i['@state']) > 1:
                        lifts.append([10,  str(i['@state']).lower()])
                    else:
                        lifts.append([10,  str(i['@state']).upper()])

                elif i['@name_en'] == 'STRELA':
                    if len(i['@state']) > 1:
                        lifts.append([11,  str(i['@state']).lower()])
                    else:
                        lifts.append([11,  str(i['@state']).upper()])

                elif i['@name_en'] == 'CHALET':
                    if len(i['@state']) > 1:
                        lifts.append([12,  str(i['@state']).lower()])
                    else:
                        lifts.append([12,  str(i['@state']).upper()])

                elif i['@name_en'] == 'KROKUS':
                    if len(i['@state']) > 1:
                        lifts.append([13,  str(i['@state']).lower()])
                    else:
                        lifts.append([13,  str(i['@state']).upper()])

                elif i['@name_en'] == 'EDELWEISS':
                    if len(i['@state']) > 1:
                        lifts.append([14,  str(i['@state']).lower()])
                    else:
                        lifts.append([14,  str(i['@state']).upper()])

                elif i['@name_en'] == 'JUVENTA':
                    lifts.append([15, i['@state']])
                    if len(i['@state']) > 1:
                        lifts.append([15,  str(i['@state']).lower()])
                    else:
                        lifts.append([15,  str(i['@state']).upper()])

                elif i['@name_en'] == 'DRIADA':
                    if len(i['@state']) > 1:
                        lifts.append([16, str(i['@state']).lower()])
                    else:
                        lifts.append([16, str(i['@state']).upper()])

                elif i['@name_en'] == 'TUNDRA':
                    if len(i['@state']) > 1:
                        lifts.append([17, str(i['@state']).lower()])
                    else:
                        lifts.append([17, str(i['@state']).upper()])

                elif i['@name_en'] == 'Rope tow Tubing':
                    if len(i['@state']) > 1:
                        lifts.append([19, str(i['@state']).lower()])
                    else:
                        lifts.append([19, str(i['@state']).upper()])

                elif i['@name_en'] == 'Rope tow Snowpark':
                    if len(i['@state']) > 1:
                        lifts.append([20, str(i['@state']).lower()])
                    else:
                        lifts.append([20, str(i['@state']).upper()])
                elif i['@name_en'] == 'Rope tow Rosa 1600':
                    if len(i['@state']) > 1:
                        lifts.append([21, str(i['@state']).lower()])
                    else:
                        lifts.append([21, str(i['@state']).upper()])
                elif i['@name_en'] == 'Magic carpet Junior Training Slope':
                    if len(i['@state']) > 1:
                        lifts.append([22, str(i['@state']).lower()])
                    else:
                        lifts.append([22, str(i['@state']).upper()])
        if 'SLOPES' == x['@nom_en']:
            for i in x['TRAIL']:
                if i['@name_en'] == 'Mini-Park':
                    if len(i['@state']) > 1:
                        lifts.append([23, str(i['@state']).lower()])
                    else:
                        lifts.append([23, str(i['@state']).upper()])
                elif i['@name_en'] == 'THE STASH PARK':
                    if len(i['@state']) > 1:
                        lifts.append([24, str(i['@state']).lower()])
                    else:
                        lifts.append([24, str(i['@state']).upper()])
                elif i['@name_en'] == 'Snow-park':
                    if len(i['@state']) > 1:
                        lifts.append([25, str(i['@state']).lower()])
                    else:
                        lifts.append([25, str(i['@state']).upper()])
                elif i['@name_en'] == 'Arbor':
                    if len(i['@state']) > 1:
                        lifts.append([26, str(i['@state']).lower()])
                    else:
                        lifts.append([26, str(i['@state']).upper()])
                elif i['@name_en'] == 'Chalet':
                    if len(i['@state']) > 1:
                        lifts.append([27, str(i['@state']).lower()])
                    else:
                        lifts.append([27, str(i['@state']).upper()])

                elif i['@name_en'] == 'Juventa':
                    if len(i['@state']) > 1:
                        lifts.append([28, str(i['@state']).lower()])
                    else:
                        lifts.append([28, str(i['@state']).upper()])
                elif i['@name_en'] == 'Borey':
                    if len(i['@state']) > 1:
                        lifts.append([29, str(i['@state']).lower()])
                    else:
                        lifts.append([29, str(i['@state']).upper()])

                elif i['@name_en'] == 'Ehkho':
                    if len(i['@state']) > 1:
                        lifts.append([30, str(i['@state']).lower()])
                    else:
                        lifts.append([30, str(i['@state']).upper()])
                elif i['@name_en'] == 'AIBGA':
                    if len(i['@state']) > 1:
                        lifts.append([31, str(i['@state']).lower()])
                    else:
                        lifts.append([31, str(i['@state']).upper()])

                elif i['@name_en'] == 'B 52 above 1600':
                    if len(i['@state']) > 1:
                        lifts.append([32, str(i['@state']).lower()])
                    else:
                        lifts.append([32, str(i['@state']).upper()])
                elif i['@name_en'] == 'B 52 below 1600':
                    if len(i['@state']) > 1:
                        lifts.append([33, str(i['@state']).lower()])
                    else:
                        lifts.append([33, str(i['@state']).upper()])
                elif i['@name_en'] == 'VANCOUVER 10':
                    if len(i['@state']) > 1:
                        lifts.append([34, str(i['@state']).lower()])
                    else:
                        lifts.append([34, str(i['@state']).upper()])
                elif i['@name_en'] == 'VERONIKA':
                    if len(i['@state']) > 1:
                        lifts.append([35, str(i['@state']).lower()])
                    else:
                        lifts.append([35, str(i['@state']).upper()])

                elif i['@name_en'] == 'VIRAZH above 1800':
                    if len(i['@state']) > 1:
                        lifts.append([36, str(i['@state']).lower()])
                    else:
                        lifts.append([36, str(i['@state']).upper()])
                elif i['@name_en'] == 'VIRAZH below 1800':
                    if len(i['@state']) > 1:
                        lifts.append([37, str(i['@state']).lower()])
                    else:
                        lifts.append([37, str(i['@state']).upper()])
                elif i['@name_en'] == 'Vstrecha':
                    if len(i['@state']) > 1:
                        lifts.append([38, str(i['@state']).lower()])
                    else:
                        lifts.append([38, str(i['@state']).upper()])
                elif i['@name_en'] == 'GORIZONT above 1600':
                    if len(i['@state']) > 1:
                        lifts.append([39, str(i['@state']).lower()])
                    else:
                        lifts.append([39, str(i['@state']).upper()])
                elif i['@name_en'] == 'GORIZONT below 1600':
                    if len(i['@state']) > 1:
                        lifts.append([40, str(i['@state']).lower()])
                    else:
                        lifts.append([40, str(i['@state']).upper()])

                elif i['@name_en'] == 'ZHENSKIY OLYMPIC above 1600':
                    if len(i['@state']) > 1:
                        lifts.append([41, str(i['@state']).lower()])
                    else:
                        lifts.append([41, str(i['@state']).upper()])
                elif i['@name_en'] == 'ZHENSKIY OLYMPIC B below 1600':
                    if len(i['@state']) > 1:
                        lifts.append([42, str(i['@state']).lower()])
                    else:
                        lifts.append([42, str(i['@state']).upper()])

                elif i['@name_en'] == 'ZMEIKA above 1665':
                    if len(i['@state']) > 1:
                        lifts.append([43, str(i['@state']).lower()])
                    else:
                        lifts.append([43, str(i['@state']).upper()])
                elif i['@name_en'] == 'ZMEIKA below 1665':
                    if len(i['@state']) > 1:
                        lifts.append([44, str(i['@state']).lower()])
                    else:
                        lifts.append([44, str(i['@state']).upper()])

                elif i['@name_en'] == 'KASKAD above 1600':
                    if len(i['@state']) > 1:
                        lifts.append([45, str(i['@state']).lower()])
                    else:
                        lifts.append([45, str(i['@state']).upper()])
                elif i['@name_en'] == 'KASKAD below 1600':
                    if len(i['@state']) > 1:
                        lifts.append([46, str(i['@state']).lower()])
                    else:
                        lifts.append([46, str(i['@state']).upper()])

                elif i['@name_en'] == 'KVARTET':
                    if len(i['@state']) > 1:
                        lifts.append([47, str(i['@state']).lower()])
                    else:
                        lifts.append([47, str(i['@state']).upper()])

                elif i['@name_en'] == 'CRAZY KHUTOR above 1400':
                    if len(i['@state']) > 1:
                        lifts.append([48, str(i['@state']).lower()])
                    else:
                        lifts.append([48, str(i['@state']).upper()])
                elif i['@name_en'] == 'CRAZY KHUTOR below 1400':
                    if len(i['@state']) > 1:
                        lifts.append([49, str(i['@state']).lower()])
                    else:
                        lifts.append([49, str(i['@state']).upper()])

                elif i['@name_en'] == 'LABIRINT above 1400':
                    if len(i['@state']) > 1:
                        lifts.append([50, str(i['@state']).lower()])
                    else:
                        lifts.append([50, str(i['@state']).upper()])
                elif i['@name_en'] == 'LABIRINT below 1400':
                    if len(i['@state']) > 1:
                        lifts.append([51, str(i['@state']).lower()])
                    else:
                        lifts.append([51, str(i['@state']).upper()])

                elif i['@name_en'] == 'MUZHSKOY OLYMPIC above 1600':
                    if len(i['@state']) > 1:
                        lifts.append([52, str(i['@state']).lower()])
                    else:
                        lifts.append([52, str(i['@state']).upper()])
                elif i['@name_en'] == 'MUZHSKOY OLYMPIC below 1600':
                    if len(i['@state']) > 1:
                        lifts.append([53, str(i['@state']).lower()])
                    else:
                        lifts.append([53, str(i['@state']).upper()])


                elif i['@name_en'] == 'NAGANO 98':
                    if len(i['@state']) > 1:
                        lifts.append([54, str(i['@state']).lower()])
                    else:
                        lifts.append([54, str(i['@state']).upper()])

                elif i['@name_en'] == 'OBER KHUTOR above 1600':
                    if len(i['@state']) > 1:
                        lifts.append([55, str(i['@state']).lower()])
                    else:
                        lifts.append([55, str(i['@state']).upper()])
                elif i['@name_en'] == 'OBER KHUTOR below 1600':
                    if len(i['@state']) > 1:
                        lifts.append([56, str(i['@state']).lower()])
                    else:
                        lifts.append([56, str(i['@state']).upper()])


                elif i['@name_en'] == 'OZERNAYA':
                    if len(i['@state']) > 1:
                        lifts.append([57, str(i['@state']).lower()])
                    else:
                        lifts.append([57, str(i['@state']).upper()])
                elif i['@name_en'] == 'OREL':
                    if len(i['@state']) > 1:
                        lifts.append([58, str(i['@state']).lower()])
                    else:
                        lifts.append([58, str(i['@state']).upper()])
                elif i['@name_en'] == 'Perehod':
                    if len(i['@state']) > 1:
                        lifts.append([59, str(i['@state']).lower()])
                    else:
                        lifts.append([59, str(i['@state']).upper()])
                elif i['@name_en'] == 'PLATO':
                    if len(i['@state']) > 1:
                        lifts.append([60, str(i['@state']).lower()])
                    else:
                        lifts.append([60, str(i['@state']).upper()])

                elif i['@name_en'] == 'PRIMULA':
                    if len(i['@state']) > 1:
                        lifts.append([61, str(i['@state']).lower()])
                    else:
                        lifts.append([61, str(i['@state']).upper()])
                elif i['@name_en'] == 'ROSA STAR':
                    if len(i['@state']) > 1:
                        lifts.append([62, str(i['@state']).lower()])
                    else:
                        lifts.append([62, str(i['@state']).upper()])
                elif i['@name_en'] == 'ROSA BLADE':
                    if len(i['@state']) > 1:
                        lifts.append([63, str(i['@state']).lower()])
                    else:
                        lifts.append([63, str(i['@state']).upper()])

                elif i['@name_en'] == 'TRITON above 2000':
                    if len(i['@state']) > 1:
                        lifts.append([64, str(i['@state']).lower()])
                    else:
                        lifts.append([64, str(i['@state']).upper()])
                elif i['@name_en'] == 'TRITON middle 1600':
                    if len(i['@state']) > 1:
                        lifts.append([65, str(i['@state']).lower()])
                    else:
                        lifts.append([65, str(i['@state']).upper()])
                elif i['@name_en'] == 'TRITON below 1600':
                    if len(i['@state']) > 1:
                        lifts.append([66, str(i['@state']).lower()])
                    else:
                        lifts.append([66, str(i['@state']).upper()])

                elif i['@name_en'] == 'FIALKA':
                    if len(i['@state']) > 1:
                        lifts.append([67, str(i['@state']).lower()])
                    else:
                        lifts.append([67, str(i['@state']).upper()])
                elif i['@name_en'] == 'CHAMONIX 24':
                    if len(i['@state']) > 1:
                        lifts.append([68, str(i['@state']).lower()])
                    else:
                        lifts.append([68, str(i['@state']).upper()])
                elif i['@name_en'] == 'YUREV KHUTOR':
                    if len(i['@state']) > 1:
                        lifts.append([69, str(i['@state']).lower()])
                    else:
                        lifts.append([69, str(i['@state']).upper()])

                elif i['@name_en'] == 'OREADA':
                    if len(i['@state']) > 1:
                        lifts.append([70, str(i['@state']).lower()])
                    else:
                        lifts.append([70, str(i['@state']).upper()])
                elif i['@name_en'] == 'STOROZHKA':
                    if len(i['@state']) > 1:
                        lifts.append([71, str(i['@state']).lower()])
                    else:
                        lifts.append([71, str(i['@state']).upper()])
                elif i['@name_en'] == 'YAVOR (2320 – 2221)':
                    if len(i['@state']) > 1:
                        lifts.append([72, str(i['@state']).lower()])
                    else:
                        lifts.append([72, str(i['@state']).upper()])

                elif i['@name_en'] == 'YAVOR (2221 – 2118)':
                    if len(i['@state']) > 1:
                        lifts.append([73, str(i['@state']).lower()])
                    else:
                        lifts.append([73, str(i['@state']).upper()])
                elif i['@name_en'] == 'YAVOR (2118 – 1472)':
                    if len(i['@state']) > 1:
                        lifts.append([74, str(i['@state']).lower()])
                    else:
                        lifts.append([74, str(i['@state']).upper()])
                elif i['@name_en'] == 'NAYADA':
                    if len(i['@state']) > 1:
                        lifts.append([75, str(i['@state']).lower()])
                    else:
                        lifts.append([75, str(i['@state']).upper()])
                elif i['@name_en'] == 'PRIMAVERA':
                    if len(i['@state']) > 1:
                        lifts.append([76, str(i['@state']).lower()])
                    else:
                        lifts.append([76, str(i['@state']).upper()])
                elif i['@name_en'] == 'BARVINOK':
                    if len(i['@state']) > 1:
                        lifts.append([77, str(i['@state']).lower()])
                    else:
                        lifts.append([77, str(i['@state']).upper()])
                elif i['@name_en'] == 'GORITSVET':
                    if len(i['@state']) > 1:
                        lifts.append([78, str(i['@state']).lower()])
                    else:
                        lifts.append([78, str(i['@state']).upper()])
    data = {"data": lifts}
    return HttpResponse(json.dumps(data), content_type='application/json')
