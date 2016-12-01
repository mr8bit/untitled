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
                    lifts.append(["1", i['@state']])
                elif i['@name_en'] == 'ZAPOVEDNYY LES':
                    lifts.append(["2", i['@state']])
                elif i['@name_en'] == 'KAVKAZSKIY EXPRESS above 1600':
                    lifts.append(["3", i['@state']])
                elif i['@name_en'] == 'KAVKAZSKIY EXPRESS below 1600':
                    lifts.append(["4", i['@state']])
                elif i['@name_en'] == 'VOLCHYA SKALA':
                    lifts.append(["5", i['@state']])
                elif i['@name_en'] == 'BESEDA':
                    lifts.append(["6", i['@state']])
                elif i['@name_en'] == 'KVARTET':
                    lifts.append(["7", i['@state']])
                elif i['@name_en'] == 'SKAZKA':
                    lifts.append(["8", i['@state']])
                elif i['@name_en'] == 'KABAN':
                    lifts.append(["9", i['@state']])
                elif i['@name_en'] == 'EXTREME':
                    lifts.append(["10", i['@state']])
                elif i['@name_en'] == 'STRELA':
                    lifts.append(["11", i['@state']])
                elif i['@name_en'] == 'CHALET':
                    lifts.append(["12", i['@state']])
                elif i['@name_en'] == 'KROKUS':
                    lifts.append(["13", i['@state']])
                elif i['@name_en'] == 'EDELWEISS':
                    lifts.append(["14", i['@state']])
                elif i['@name_en'] == 'JUVENTA':
                    lifts.append(["15", i['@state']])
                elif i['@name_en'] == 'DRIADA':
                    lifts.append(["16", i['@state']])
                elif i['@name_en'] == 'TUNDRA':
                    lifts.append(["17", i['@state']])
                elif i['@name_en'] == 'Rope tow Tubing':
                    lifts.append(["19", i['@state']])
                elif i['@name_en'] == 'Rope tow Snowpark':
                    lifts.append(["20", i['@state']])
                elif i['@name_en'] == 'Rope tow Rosa 1600':
                    lifts.append(["21", i['@state']])
                elif i['@name_en'] == 'Magic carpet Junior Training Slope':
                    lifts.append(["22", i['@state']])
        if 'SLOPES' == x['@nom_en']:
            for i in x['TRAIL']:
                if i['@name_en'] == 'Mini-Park':
                    lifts.append(["23", i['@state']])
                elif i['@name_en'] == 'THE STASH PARK':
                    lifts.append(["24", i['@state']])
                elif i['@name_en'] == 'Snow-park':
                    lifts.append(["25", i['@state']])
                elif i['@name_en'] == 'Arbor':
                    lifts.append(["26", i['@state']])
                elif i['@name_en'] == 'Chalet':
                    lifts.append(["27", i['@state']])

                elif i['@name_en'] == 'Juventa':
                    lifts.append(["28", i['@state']])
                elif i['@name_en'] == 'Borey':
                    lifts.append(["29", i['@state']])
                elif i['@name_en'] == 'Ehkho':
                    lifts.append(["30", i['@state']])
                elif i['@name_en'] == 'AIBGA':
                    lifts.append(["31", i['@state']])

                elif i['@name_en'] == 'B 52 above 1600':
                    lifts.append(["32", i['@state']])
                elif i['@name_en'] == 'B 52 below 1600':
                    lifts.append(["33", i['@state']])
                elif i['@name_en'] == 'VANCOUVER 10':
                    lifts.append(["34", i['@state']])
                elif i['@name_en'] == 'VERONIKA':
                    lifts.append(["35", i['@state']])

                elif i['@name_en'] == 'VIRAZH above 1800':
                    lifts.append(["36", i['@state']])
                elif i['@name_en'] == 'VIRAZH below 1800':
                    lifts.append(["37", i['@state']])
                elif i['@name_en'] == 'Vstrecha':
                    lifts.append(["38", i['@state']])
                elif i['@name_en'] == 'GORIZONT above 1600':
                    lifts.append(["39", i['@state']])
                elif i['@name_en'] == 'GORIZONT below 1600':
                    lifts.append(["40", i['@state']])

                elif i['@name_en'] == 'ZHENSKIY OLYMPIC above 1600':
                    lifts.append(["41", i['@state']])
                elif i['@name_en'] == 'ZHENSKIY OLYMPIC B below 1600':
                    lifts.append(["42", i['@state']])

                elif i['@name_en'] == 'ZMEIKA above 1665':
                    lifts.append(["43", i['@state']])
                elif i['@name_en'] == 'ZMEIKA below 1665':
                    lifts.append(["44", i['@state']])

                elif i['@name_en'] == 'KASKAD above 1600':
                    lifts.append(["45", i['@state']])
                elif i['@name_en'] == 'KASKAD below 1600':
                    lifts.append(["46", i['@state']])

                elif i['@name_en'] == 'KVARTET':
                    lifts.append(["47", i['@state']])

                elif i['@name_en'] == 'CRAZY KHUTOR above 1400':
                    lifts.append(["48", i['@state']])
                elif i['@name_en'] == 'CRAZY KHUTOR below 1400':
                    lifts.append(["49", i['@state']])

                elif i['@name_en'] == 'LABIRINT above 1400':
                    lifts.append(["50", i['@state']])
                elif i['@name_en'] == 'LABIRINT below 1400':
                    lifts.append(["51", i['@state']])

                elif i['@name_en'] == 'MUZHSKOY OLYMPIC above 1600':
                    lifts.append(["52", i['@state']])
                elif i['@name_en'] == 'MUZHSKOY OLYMPIC below 1600':
                    lifts.append(["53", i['@state']])


                elif i['@name_en'] == 'NAGANO 98':
                    lifts.append(["54", i['@state']])

                elif i['@name_en'] == 'OBER KHUTOR above 1600':
                    lifts.append(["55", i['@state']])
                elif i['@name_en'] == 'OBER KHUTOR below 1600':
                    lifts.append(["56", i['@state']])


                elif i['@name_en'] == 'OZERNAYA':
                    lifts.append(["57", i['@state']])
                elif i['@name_en'] == 'OREL':
                    lifts.append(["58", i['@state']])
                elif i['@name_en'] == 'Perehod':
                    lifts.append(["59", i['@state']])
                elif i['@name_en'] == 'PLATO':
                    lifts.append(["60", i['@state']])

                elif i['@name_en'] == 'PRIMULA':
                    lifts.append(["61", i['@state']])
                elif i['@name_en'] == 'ROSA STAR':
                    lifts.append(["62", i['@state']])
                elif i['@name_en'] == 'ROSA BLADE':
                    lifts.append(["63", i['@state']])

                elif i['@name_en'] == 'TRITON above 2000':
                    lifts.append(["64", i['@state']])
                elif i['@name_en'] == 'TRITON middle 1600':
                    lifts.append(["65", i['@state']])
                elif i['@name_en'] == 'TRITON below 1600':
                    lifts.append(["66", i['@state']])

                elif i['@name_en'] == 'FIALKA':
                    lifts.append(["67", i['@state']])
                elif i['@name_en'] == 'CHAMONIX 24':
                    lifts.append(["68", i['@state']])
                elif i['@name_en'] == 'YUREV KHUTOR':
                    lifts.append(["69", i['@state']])

                elif i['@name_en'] == 'OREADA':
                    lifts.append(["70", i['@state']])
                elif i['@name_en'] == 'STOROZHKA':
                    lifts.append(["71", i['@state']])
                elif i['@name_en'] == 'YAVOR (2320 – 2221)':
                    lifts.append(["72", i['@state']])

                elif i['@name_en'] == 'YAVOR (2221 – 2118)':
                    lifts.append(["73", i['@state']])
                elif i['@name_en'] == 'YAVOR (2118 – 1472)':
                    lifts.append(["74", i['@state']])

                elif i['@name_en'] == 'NAYADA':
                    lifts.append(["75", i['@state']])
                elif i['@name_en'] == 'PRIMAVERA':
                    lifts.append(["76", i['@state']])
                elif i['@name_en'] == 'BARVINOK':
                    lifts.append(["77", i['@state']])
                elif i['@name_en'] == 'GORITSVET':
                    lifts.append(["78", i['@state']])
    return HttpResponse(json.dumps(lifts), content_type='application/json')
