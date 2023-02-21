import telebot
import requests
from time import sleep

bot = telebot.TeleBot('6088262949:AAHd7JRvI8VeH1eoAEUv-lofDWGRT1UwHYQ')

current_regions_alarm = []

@bot.message_handler(commands=['start'])
def start(message):
    while True:
        headers = {'X-API-Key': '52b9d358bcb491a92d2ba114fd07dde825961358'}
        response = requests.get('https://alerts.com.ua/api/states', headers = headers)
                
        alarm_json = response.json()


        vinnytsia = alarm_json['states'][0]['alert']
        volyn = alarm_json['states'][1]['alert']
        dnipro = alarm_json['states'][2]['alert']
        donbas = alarm_json['states'][3]['alert']
        zhytomyr = alarm_json['states'][4]['alert']
        karpaty = alarm_json['states'][5]['alert']
        zaporizhya = alarm_json['states'][6]['alert']
        franik = alarm_json['states'][7]['alert']
        kyiv_obl = alarm_json['states'][8]['alert']
        kirovograd = alarm_json['states'][9]['alert']
        lugansk = alarm_json['states'][10]['alert']
        lviv = alarm_json['states'][11]['alert']
        mykolaiv = alarm_json['states'][12]['alert']
        odessa = alarm_json['states'][13]['alert']
        poltava = alarm_json['states'][14]['alert']
        rivne = alarm_json['states'][15]['alert']
        sumy = alarm_json['states'][16]['alert']
        ternopil = alarm_json['states'][17]['alert']
        kharkiv = alarm_json['states'][18]['alert']
        kherson = alarm_json['states'][19]['alert']
        khmel = alarm_json['states'][20]['alert']
        cherkasy = alarm_json['states'][21]['alert']
        chernivtsy = alarm_json['states'][22]['alert']
        chernihiv = alarm_json['states'][23]['alert']
        kyiv = alarm_json['states'][24]['alert']


        if vinnytsia:
            if vinnytsia not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][0]['name'])
                current_regions_alarm.append(vinnytsia)

        if vinnytsia in current_regions_alarm:
            if vinnytsia == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][0]['name'])
                current_regions_alarm.remove(vinnytsia)

        
        if volyn:
            if volyn not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][1]['name'])
                current_regions_alarm.append(volyn)

        if volyn in current_regions_alarm:
            if volyn == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][1]['name'])
                current_regions_alarm.remove(volyn)


        if dnipro:
            if dnipro not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][2]['name'])
                current_regions_alarm.append(dnipro)

        if dnipro in current_regions_alarm:
            if dnipro == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][2]['name'])
                current_regions_alarm.remove(dnipro)

        if donbas:
            if donbas not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][3]['name'])
                current_regions_alarm.append(donbas)

        if donbas in current_regions_alarm:
            if donbas == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][3]['name'])
                current_regions_alarm.remove(donbas)

            
        if zhytomyr:
            if zhytomyr not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][4]['name'])
                current_regions_alarm.append(zhytomyr)

        if zhytomyr in current_regions_alarm:
            if zhytomyr == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][4]['name'])
                current_regions_alarm.remove(zhytomyr)

        if karpaty:
            if karpaty not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][5]['name'])
                current_regions_alarm.append(karpaty)

        if karpaty in current_regions_alarm:
            if karpaty == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][5]['name'])
                current_regions_alarm.remove(karpaty)

                
        if zaporizhya:
            if zaporizhya not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][6]['name'])
                current_regions_alarm.append(zaporizhya)

        if zaporizhya in current_regions_alarm:
            if zaporizhya == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][6]['name'])
                current_regions_alarm.remove(zaporizhya)


        if franik:
            if franik not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][7]['name'])
                current_regions_alarm.append(franik)

        if franik in current_regions_alarm:
            if franik == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][7]['name'])
                current_regions_alarm.remove(franik)

        
        if kyiv_obl:
            if kyiv_obl not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][8]['name'])
                current_regions_alarm.append(kyiv_obl)

        if kyiv_obl in current_regions_alarm:
            if kyiv_obl == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][8]['name'])
                current_regions_alarm.remove(kyiv_obl)

        
        if kirovograd:
            if kirovograd not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][9]['name'])
                current_regions_alarm.append(kirovograd)

        if kirovograd in current_regions_alarm:
            if kirovograd == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][9]['name'])
                current_regions_alarm.remove(kirovograd)
        
        
        if lugansk:
            if lugansk not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][10]['name'])
                current_regions_alarm.append(lugansk)

        if lugansk in current_regions_alarm:
            if lugansk == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][10]['name'])
                current_regions_alarm.remove(lugansk)

        
        if lviv:
            if lviv not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][11]['name'])
                current_regions_alarm.append(lviv)

        if lviv in current_regions_alarm:
            if lviv == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][11]['name'])
                current_regions_alarm.remove(lviv)


        if mykolaiv:
            if mykolaiv not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][12]['name'])
                current_regions_alarm.append(mykolaiv)

        if mykolaiv in current_regions_alarm:
            if mykolaiv == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][12]['name'])
                current_regions_alarm.remove(mykolaiv)


        if odessa:
            if odessa not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][13]['name'])
                current_regions_alarm.append(odessa)

        if odessa in current_regions_alarm:
            if odessa == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][13]['name'])
                current_regions_alarm.remove(odessa)

        
        if poltava:
            if poltava not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][14]['name'])
                current_regions_alarm.append(poltava)

        if poltava in current_regions_alarm:
            if poltava == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][14]['name'])
                current_regions_alarm.remove(poltava)


        if rivne:
            if rivne not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][15]['name'])
                current_regions_alarm.append(rivne)

        if rivne in current_regions_alarm:
            if rivne == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][15]['name'])
                current_regions_alarm.remove(rivne)

            
        if sumy:
            if sumy not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][16]['name'])
                current_regions_alarm.append(sumy)

        if sumy in current_regions_alarm:
            if sumy == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][16]['name'])
                current_regions_alarm.remove(sumy)

        
        if ternopil:
            if ternopil not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][17]['name'])
                current_regions_alarm.append(ternopil)

        if ternopil in current_regions_alarm:
            if ternopil == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][17]['name'])
                current_regions_alarm.remove(ternopil)

            
        if kharkiv:
            if kharkiv not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][18]['name'])
                current_regions_alarm.append(kharkiv)

        if kharkiv in current_regions_alarm:
            if kharkiv == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][18]['name'])
                current_regions_alarm.remove(kharkiv)


        if kherson:
            if kherson not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][19]['name'])
                current_regions_alarm.append(kherson)

        if kherson in current_regions_alarm:
            if kherson == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][19]['name'])
                current_regions_alarm.remove(kherson)


        if khmel:
            if khmel not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][20]['name'])
                current_regions_alarm.append(khmel)

        if khmel in current_regions_alarm:
            if khmel == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][20]['name'])
                current_regions_alarm.remove(khmel)


        if cherkasy:
            if cherkasy not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][21]['name'])
                current_regions_alarm.append(cherkasy)

        if cherkasy in current_regions_alarm:
            if cherkasy == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][21]['name'])
                current_regions_alarm.remove(cherkasy)


        if chernivtsy:
            if chernivtsy not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][22]['name'])
                current_regions_alarm.append(chernivtsy)

        if chernivtsy in current_regions_alarm:
            if chernivtsy == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][22]['name'])
                current_regions_alarm.remove(chernivtsy)


        if chernihiv:
            if chernihiv not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][23]['name'])
                current_regions_alarm.append(chernihiv)

        if chernihiv in current_regions_alarm:
            if chernihiv == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][23]['name'])
                current_regions_alarm.remove(chernihiv)

            
        if kyiv:
            if kyiv not in current_regions_alarm:
                bot.send_message(message.chat.id, '🔴 Повітряна тривога зараз у ' + alarm_json['states'][24]['name'])
                current_regions_alarm.append(kyiv)

        if kyiv in current_regions_alarm:
            if kyiv == False:
                bot.send_message(message.chat.id, '🟢 Відбій повітряної тривоги у ' + alarm_json['states'][24]['name'])
                current_regions_alarm.remove(kyiv)

        sleep(12)

@bot.message_handler(commands=['a'])
def a(message):
    bot.send_message(message.chat.id, 'aaa')

bot.polling(none_stop=True)