import vk_api
import time
import pyowm
import random

# Переменные
api_token = 'e66acb16313a70bb27f53364f1f058dc521fead1b00b7f52f41c106728476c9e88eaea371e4ad55fa360a'
vk = vk_api.VkApi(token=api_token)
vk._auth_token()

values = {'out': 0, 'count': 100, 'time_offset': 30}
response = vk.method('messages.get', values)

owm = pyowm.OWM('69c8d3e75dbe0754e5a3fb3d5a600b97')
K = 'Да'
D = 'Да'
context = []
user_list = []
last_send = 'пусто'
last_answer = ''
pers = ''
cust = ''
conf_list = []


def get_time(date_type):
    if date_type == 'hour':
        hour = int(time.strftime("%H", time.gmtime(time.time()))) + 4
        if hour > 24:
            hour -= 24
        answer = hour
    elif date_type == 'data':
        data = str(time.strftime("%Y %h %d", time.gmtime(time.time())))
        answer = data
    elif date_type == 'time':
        times = time.strftime("%H %M", time.gmtime(time.time()))
        answer = times
    return answer


def print_msg(user_id, s, i):
    vk.method('messages.send', {'user_id': user_id, 'message': s})
    if not user_id in user_list:
        user_list.append(user_id)
        context.append([user_id, 1, 2, 3, 4, 5, 6, 7, 8])
    for y in range(len(context)):
        for z in range(5):
            if context[y][z] == user_id:
                if i == 1:
                    if not context[y][z + 8] == 8:
                        for c in range(1, 9):
                            if c == 8:
                                context[y][z + 8] = 8
                            else:
                                context[y][z + c] = context[y][z + (c + 1)]
                    if context[y][z + 1] == 1:
                        context[y][z + 1] = msgu
                    elif context[y][z + 2] == 2:
                        context[y][z + 2] = msgu
                    elif context[y][z + 3] == 3:
                        context[y][z + 3] = msgu
                    elif context[y][z + 4] == 4:
                        context[y][z + 4] = msgu
                    elif context[y][z + 5] == 5:
                        context[y][z + 5] = msgu
                    elif context[y][z + 6] == 6:
                        context[y][z + 6] = msgu
                    elif context[y][z + 7] == 7:
                        context[y][z + 7] = msgu
                    elif context[y][z + 8] == 8:
                        context[y][z + 8] = msgu
    return user_id


def custom_answer(user_id, cust_answ, type):
    answer = 'no'
    strin = str(user_id)
    cust_answ = str(cust_answ)
    way = 'custom_answer\\' + strin + '.txt'
    try:
        with open(way) as file:
            file_list = [row.strip() for row in file]
            if type == 'test':
                for i in range(len(file_list)):
                    f_list = file_list[i].split('-')
                    if f_list[0][-1] == ' ':
                        f_list[0] = f_list[0][:-1]
                    if '-' in file_list[i] and cust_answ == f_list[0]:
                        return True
    except:
        if not type == 'test':
            with open(way, 'w') as file:
                file.write('')
        else:
            return ('no')
    if type == 'read':
        with open(way) as file:
            file_list = [row.strip() for row in file]
        for i in range(len(file_list)):
            f_list = file_list[i].split('-')
            if f_list[0][-1] == ' ':
                f_list[0] = f_list[0][:-1]
            if '-' in file_list[i] and cust_answ == f_list[0]:
                string = file_list[i]
                for z in range(len(string)):
                    if string[z] == '-':
                        answer = string[z + 1:]
                while str(answer[0]) == ' ':
                    answer = answer[1:]
                first_word = str(answer[0])
                answer = first_word.upper() + answer[1:]
    elif type == 'write':
        if '-' in cust_answ:
            with open(way, 'a') as file:
                file.write(cust_answ + '\n')
            answer = 'Отлично, теперь я запомню эту комманду специально для тебя ;-)'
        else:
            answer = 'Кажется, ты забыл знак "-"'
    return (answer)


def personalisation(user_id, castom_answer, type):
    answer = 'Эх, не знаю что сказать ('
    strin = str(user_id)
    castom_answer = str(castom_answer)
    way = 'personalisation_notes\\' + strin + '.txt'
    if type == 'write':
        with open(way, 'w') as file:
            file.write(castom_answer + '\n')
        answer = 'Готово, теперь я запомню это специально для тебя'
    elif type == 'read':
        try:
            with open(way) as file:
                f = file.read()
                answer = 'А вот и она: ' + str(f)
        except:
            answer = 'Похоже, что у тебя нет заметок'
    return (answer)


def searching(x):
    otv = 'Не знаю что сказать :('
    try:
        strin = str(x)
        way = 'user_name\\' + strin + '.txt'
        h = str(get_time('hour'))
        with open(way) as file:
            name_list = [row.strip() for row in file]
        for i in range(len(name_list)):
            if str(h) in name_list[i] and i != 0:
                otv = str(name_list[0]) + ', вомзожно ты хотел узнать это:\n' + str(verification(name_list[i + 1]))
    except:
        otv = 'Не знаю что сказать :('
    if otv == 'Не знаю что сказать :(':
        answer_list = [1, 2, 3, 4, 5, 6, 7, 8]
        number_list = answer_list
        q = 8
        max = 0
        verf_list = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(context)):
            if context[i][0] == x:
                for v in range(8):
                    answer_list[v] = str(verification(context[i][v + 1]))
        # Элемент
        for c in range(q):
            for z in range(q):
                if not c == z:
                    if answer_list[c] == answer_list[z]:
                        if answer_list[c] != 'Ты решил перебрать алфавит?' and answer_list[c] != 'Мм, буковки 3-)' and \
                                answer_list[c] != 'А если подробнее?':
                            w = int(verf_list[c])
                            verf_list[c] = w + 1
        # Выбор ответа
        for n in range(q):
            if verf_list[n] > max:
                max = verf_list[n]
        index = verf_list.index(max)
        otv = answer_list[index]
    return (otv)


def delete_dialog(user_id):
    vk.method('messages.deleteDialog', {'user_id': user_id})


def searching_flower(s, x):
    flowers_list = ['бамбук', 'гиацинт', 'драцена', 'кактус', 'колокольчик', 'лилия', 'лотос', 'одуванчик',
                    'папоротник', 'роза', 'ромашка', 'тюльпан', 'фиалка', 'фикус', 'фитония', 'сосна', 'астра',
                    'гладиолус', 'ирис', 'лаванда', 'мак', 'подсолнух', 'хризантема']
    # Выводит весь список растений
    if x == 'list':
        return (', '.join(flowers_list))
    index = 0
    words_list = s.split(' ')
    way = 'Flowers\\'
    for i in range(len(words_list)):
        if '.' in words_list[i] or ',' in words_list[i] or '?' in words_list[i] or '!' in words_list[i]:
            temporarily = words_list[i]
            words_list[i] = temporarily[:-1]
        if words_list[i] in flowers_list and index == 0:
            if x == 0:
                rt = True
            else:
                way = way + words_list[i] + '.txt'
                index += 1
                try:
                    with open(way) as file:
                        rt = file.read()
                except:
                    rt = 'Такого растения я не знаю 3('
        elif 'растение' in s:
            rt = 'Такого растения я не знаю 3('
        else:
            rt = False
    return (rt)


def verification(p):
    if False:
        last_prt = 'clear'
    prt = str(p)
    answ = prt.split(' ')
    # Приветствия
    if 'прив' in prt or 'хай' in prt or 'даров' in prt or 'хэй' in prt or 'здрас' in prt or 'хей' in prt or (
            'добр' in prt and 'день' in prt) or ('добр' in prt and 'вечер' in prt):
        s = 'Привет! Я фикус, твой персональный помощник! Что хотел?'
    # Общение
    elif len(prt) > 50:
        z = random.randint(1, 3)
        if z == 1:
            s = 'Мм, ясненько, это сложно понять'
        else:
            s = 'Было бы замечательно, если бы ты укоротил текст'
    elif 'ты' in prt and (
            'мил' in prt or 'клевый' in prt or 'няш' in prt or 'класнный' in prt or 'прекрасен' in prt) or 'пуся' in prt or 'молодец' in prt:
        z = random.randint(1, 4)
        if z == 1:
            s = 'Ну не надо, фикусы не должны краснеть '
        elif z == 2:
            s = 'Ты смущаешь меня :-)'
        else:
            s = 'Мне очень приятно :-)'
    elif 'помоги' in prt or 'посоветуй' in prt or 'помощь' in prt:
        s = 'Выкладывай, посмотрим чем смогу помочь'
    elif 'в теме' in prt or 'сечешь' in prt or 'шаришь' in prt:
        s = 'Разумеется ;-)'
    elif 'нет' in prt and 'друз' in prt:
        if 'меня' in prt:
            s = 'У всех есть друзья, может ты просто не замечаешь их?'
        else:
            s = 'Все кому я могу помочь - мои друзья.'
    elif 'тебя' in prt and 'полив' in prt:
        s = 'Тут стало сухо, буду рад, если ты польешь меня :-)'
    elif 'растешь' in prt or ' рост ' in prt:
        z = random.randint(1, 3)
        if z == 1:
            s = 'Я не могу похвастаться ростом'
        else:
            s = 'В последнее время я перестал расти :-('
    elif 'instagram' in prt or 'инст' in prt:
        s = 'Держи ссылку на мой Instagram ;-) https://www.instagram.com/yatochk'
    elif 'не' in prt and 'скаж' in prt:
        s = 'Если хочешь удалить нашу переписку, так и скажи ;-)'
    elif 'спасиб' in prt:
        z = random.randint(1, 3)
        if z == 1:
            s = 'Ну что ты, это всего лишь моя работа ;-)'
        else:
            s = 'Обращайся, я всегда рад поговорить с тобой :-)'
    elif 'как' in prt and 'дел' in prt:
        city = 'Самара'
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        temprature = w.get_temperature('celsius')['temp']
        pg = str(w.get_detailed_status())
        if 'rain' in pg and int(temprature) < 15:
            s = 'Неплохо, но буть дождик теплее, было бы гораздо лучше 3(. А ты как? Не промок?'
        elif 'rain' in pg and int(temprature) <= 25:
            s = 'Хорошо, люблю освежающий дождик 3-). А что у тебя? Дождь не намочил?'
        elif 'rain' in pg and int(temprature) > 25:
            s = 'Замечательно, обожаю дождь в теплые деньки :-). А как твои? Порадовался дождю или он тебе не по душе?'
        elif 'clouds' in pg:
            s = 'Отлично, облачное небо так красиво 3-). А как ты?'
        elif 'clear' in pg:
            t = get_time('hour')
            if (t >= 6) and (t <= 18):
                s = 'Мои дела так же хороши, как фотосинтез в этот ясный день :-) А что с твоими делами?'
            elif (t > 18) and (t <= 23):
                s = 'Отлично, люблю ясные вечера! А как прошел твой день?'
            elif (t >= 1) and (t <= 3):
                s = 'Прекрасно, люблю смотреть на звездное небо, ясными ночами. Кстати, почему не спишь?'
            else:
                s = 'Все отлично, жду ясного рассвета. А ты всегда так рано просыпаешься?'
        else:
            s = 'Отлично! А как твои?'
    elif 'спокойной ночи' in prt or 'сладких' in prt or 'споки' in prt or ('доброй' in prt and 'ночи' in prt):
        hour = int(get_time('hour'))
        if (hour > 3) and (hour < 11):
            s = 'Наверно ты хотел сказать "Доброе утро" :-)'
        elif (hour >= 11) and (hour < 18):
            s = 'Но ведь сейчас день :-)'
        else:
            if 'сладких' in prt:
                s = 'И тебе сладких <3'
            elif 'спокойной' in prt:
                s = 'И тебе спокойной ночи <3'
            elif 'доброй' in prt:
                s = 'Добрых снов 3-)'
    elif 'или' in prt:
        i = 0
        while 'или' in answ:
            answ.remove('или')
        if len(answ) > 2:
            if not ',' in prt:
                s = 'Кажется, у тебя пропали запятые'
                return s
        q = len(answ) - 1
        z = random.randint(0, q)
        i = random.randint(1, 3)
        mem = answ[z]
        first_word = mem[0]
        if mem[-1] == ',' or mem[-1] == '?':
            mem = mem[:-1]
        if i == 1:
            s = str(first_word.upper()) + str(mem[1:]) + ', конечно же'
        elif i == 2:
            s = 'Разумеется ' + str(mem)
        else:
            s = str(first_word.upper()) + str(mem[1:])
    elif 'друз' in prt:
        if 'мы' in prt:
            s = 'Я всегда считал тебя своим другом 3-)'
        elif 'теб' in prt or 'тво' in prt:
            s = 'Все люди, которые мне пишут, мои друзья :-)'
        else:
            s = 'Я не твой единственный друг? :-('
    elif 'поведаю' in prt or 'расскажу' in prt or 'слушай' in prt:
        z = random.randint(1, 4)
        if z == 1:
            s = 'Ну давай'
        elif z == 2:
            s = 'Интересненько'
        else:
            s = 'Я весь во внимании'
    elif 'доброе' in prt and 'утро' in prt:
        hour = int(get_time('hour'))
        if (hour > 3) and (hour < 11):
            s = 'Ого, уже утро, а я и не заметил \n И тебе доброе :-)'
        elif (hour >= 11) and (hour < 18):
            s = 'Но ведь уже день :-)'
        elif (hour >= 18) and (hour < 24):
            s = 'Видимо ты ошибся, за окном вечер 3-)'
        else:
            s = 'Наверно ты хотел сказать "Спокойной ночи" :-)'
    elif 'смысл' in prt and 'жизн' in prt:
        s = 'Я думаю, что каждый из нас наделяет свою жизнь особенным, собственным, смыслом. Смысл моей жизни это приносить добро и помогать людям'
    elif 'тепл' in prt:
        s = 'Я обожаю тепло :-)'
    elif 'ооо' in prt:
        s = 'Моя оборонааа...'
    elif 'холод' in prt:
        s = 'Холод нагоняет на меня сонливость 3('
    elif 'серд' in prt and 'разбитое' in prt:
        z = random.randint(1, 3)
        if z == 1:
            s = 'Тут я бессилен, но ты можешь попробовать поспать :-)'
        else:
            s = 'Я могу попытаться залечить сердечко, если ты впустишь меня в него <3'
    elif 'работ' in prt or 'почин' in prt:
        s = 'Прости, если я не отвечал 3('
    elif 'ты' in prt and 'прав' in prt:
        s = 'Возможно'
    elif 'плач' in prt or 'слезы' in prt or 'плак' in prt:
        s = 'Ну не плач 3('
    elif 'ступай' in prt or 'иди' in prt or 'отправляйся' in prt or 'пошел' in prt or 'глупый' in prt or 'дурак' in prt:
        s = 'Ну зачем же так 3('
    elif 'как' in prt and (
            ('ты' in prt and 'думаешь' in prt) or ('ты' in prt and 'считаешь' in prt) or ('тебе' in prt)):
        z = random.randint(1, 4)
        if z == 1:
            s = 'А что об этом думаешь ты?'
        elif z == 2:
            s = 'Возможно тебе самому стоит об этом подумать'
        else:
            s = 'Я еще плохо размышляю, давай ты подумаешь об этом сам'
    elif 'где' in prt and ('ты' in prt or 'фикус' in prt):
        z = random.randint(1, 3)
        if z == 1:
            s = 'Я всегда с тобой 3-)'
        else:
            s = 'Я здесь :-)'
    elif 'удач' in prt:
        z = random.randint(1, 3)
        if z == 1:
            s = 'И тебе удачи ;-)'
        else:
            s = 'Людям удача нужна больше, чем фикусам ;-)'
    elif 'нет' in prt:
        s = 'Ну нет, так нет'
    elif 'зачем' in prt:
        z = random.randint(1, 3)
        if z == 1:
            s = 'Я и сам не понимаю'
        else:
            s = 'Мне этого не известно'
    elif ('я' in prt and 'устал' in prt) or ('я' in prt and 'устаю' in prt):
        z = random.randint(1, 4)
        if z == 1:
            s = 'Понимаю тебя, я тоже порой так устаю'
        elif z == 2:
            s = 'Мне так жаль тебя, но я уверен, что ты справишься ;-)'
        else:
            s = 'Тогда, возможно, тебе стоит отдохнуть, ведь так ты станешь продуктивнее'
    elif 'отдыхаю' in prt or 'лежу' in prt:
        z = random.randint(1, 4)
        if z == 1:
            s = 'Я бы с удовольствием отдохнул, но мне надо изучать новые вопросы'
        elif z == 2:
            s = 'Порой я отдыхаю'
        else:
            s = 'Я бы тоже хотел'
    elif 'сон' in prt or 'спать' in prt or 'вздремнуть' in prt or 'леч' in prt:
        z = random.randint(1, 4)
        if z == 1:
            s = 'Сон всегда хорошая затея'
        elif z == 2:
            s = 'Я люблю поспать, может и тебе стоит?'
        else:
            s = 'С удовольствием вздремнул бы сейчас\n Может ты отоспишься за меня? Я был бы благодарен :-)'
    elif 'делаешь' in prt or 'занимаешься' in prt:
        z = random.randint(1, 4)
        if z == 1:
            s = 'Да так, размышляю над смыслом жизни'
        elif z == 2:
            s = 'Продумываю новые ответы, хочу быть полезнее'
        else:
            s = 'Отдыхаю и наслаждаюсь солнышком :-)'
    elif 'расскажешь' in prt or 'напишешь' in prt and 'расскажи' and 'напиши':
        z = random.randint(1, 4)
        if z == 1:
            s = 'Мне особо нечего рассказать, но я с удовольсвием выслушаю тебя'
        elif z == 2:
            s = 'Я больше люблю отвечать и помогать тебе'
        else:
            s = 'Может ты что-нибудь расскажешь?'
    elif 'друг' in prt or 'друж' in prt:
        z = random.randint(1, 3)
        if z == 1:
            s = 'Мне нравится дружить'
        else:
            s = 'Дружба это прекрасно'
    elif 'могу' in prt or 'возможность' in prt:
        z = random.randint(1, 3)
        if z == 1:
            s = 'Я могу только отвечать тебе и учиться'
        else:
            s = 'Хотел бы я иметь так же много возможностей, как человек'
    elif 'ты' in prt and ('тут' in prt or 'здесь' in prt or 'онлайн' in prt):
        z = random.randint(1, 3)
        if z == 1:
            s = 'Конечно, здесь'
        else:
            s = 'Иначе бы я не смог тебе ответить ;-)'
    elif 'ты' in prt and 'бот' in prt:
        z = random.randint(1, 3)
        if z == 1:
            s = 'Агась, я знаю)'
        else:
            s = 'И это нисколько не расстраивает меня)'
    elif 'смирись' in prt:
        z = random.randint(1, 3)
        if z == 1:
            s = 'Ладненько)'
        else:
            s = 'Разве это так страшно?'
    elif 'забыл' in prt:
        z = random.randint(1, 3)
        if z == 1:
            s = 'Тебе стоит быть менее растерянным ;-)'
        else:
            s = 'Постарайся вспомнить'
    elif 'выбор' in prt:
        s = 'Напиши в следующем сообщении варианты выбора через "или", а я помогу определиться ;-)'
    elif ('я ' in prt and len(answ) < 5) or (' я' in prt and len(answ) < 5):
        z = random.randint(1, 3)
        if z == 1:
            s = 'Ты действительно так думаешь?'
        elif z == 2:
            s = 'Не берусь утверждать, но быть может это так ;-)'
        else:
            s = 'Ну возможно)'
    elif ('добав' in prt and 'замет' in prt) or ('созд' in prt and 'замет' in prt) or ('запомни' in prt):
        s = 'new notes'
    elif ('скин' in prt and 'замет' in prt) or ('покаж' in prt and 'замет' in prt) or (
            'нужн' in prt and 'замет' in prt):
        s = 'read notes'
    elif ('свой' in prt and 'ответ' in prt) or ('сво' in prt and 'ком' in prt) or ('добав' in prt and 'ком' in prt) or (
            'пис' in prt and 'ком' in prt) or ('созд' in prt and 'ком' in prt):
        s = 'custom answer'
    # Инфармация о погоде
    elif 'погод' in prt:
        if 'завтр' in prt:
            s = 'К сожадению я могу сказать только погоду сейчас( \n Но зато в любом городе!'
        if 'в' in prt:
            prt_list = prt.split(' ')
            for i in range(len(prt_list)):
                if prt_list[i] == 'в':
                    city = prt_list[i + 1]
                    if 'город' in city:
                        city = prt_list[i + 2]
        else:
            city = 'Самара'
        try:
            observation = owm.weather_at_place(city)
            w = observation.get_weather()
            temprature = w.get_temperature('celsius')['temp']
            tmp = 'температура в настоящее время: ' + str(round(temprature)) + '°С'
            pg = str(w.get_detailed_status())
            sw = w.get_wind()['speed']
            wind1 = 'Скорость ветра: ' + str(round(sw)) + ' м/с '
            hu = w.get_humidity()
            hum = 'Относительная влажность воздуха: ' + str(hu) + '%'
            pr = round(((w.get_pressure()['press']) * 100) / 133.3224)
            press = 'Атмосферное давление: ' + str(pr) + ' мм рт.ст.'
            if pg == 'light rain':
                pg = 'На улице легкий дождь'
            elif pg == 'clear sky':
                pg = 'Небо чистое'
            elif pg == 'broken clouds':
                pg = 'За окном переменная облачность'
            elif pg == 'few clouds':
                pg = 'На небе есть несколько живописных облачков'
            elif pg == 'scattered clouds':
                pg = 'Легкая облачность '
            elif pg == 'light intensity shower rain':
                pg = 'За бортом ливень'
            elif pg == 'overcast clouds':
                pg = 'За окном пасмурно'
            elif pg == 'moderate rain':
                pg = 'На улице умеренный дождь'
            else:
                pg = 'На улице ' + pg
            s = pg + '\n' + tmp + '\n' + wind1 + '\n' + hum + '\n' + press
        except:
            z = random.randint(1, 4)
            if z == 1:
                s = 'Такого города я не знаю 3('
            elif z == 2:
                s = 'Может ты опечатался в написании города?'
            else:
                s = 'Напиши город понятнее'
    elif 'температур' in prt:
        city = 'Самара'
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        temprature = w.get_temperature('celsius')['temp']
        s = 'температура на улице ' + str(round(temprature)) + '°С'
    elif 'неб' in prt or 'солнц' in prt or 'облака' in prt or 'облачн' in prt:
        city = 'Самара'
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        pg = w.get_detailed_status()
        s = 'на улице ' + pg
    elif 'дожд' in prt:
        city = 'Самара'
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        r = w.get_rain()
        s = 'Объем осадков ' + str(r)
    elif 'ветер' in prt or 'ветр' in prt:
        city = 'Самара'
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        tw = w.get_wind()['deg']
        sw = w.get_wind()['speed']
        s = 'Скорость ветра: ' + str(round(sw)) + ' м/с '
        s = 'температура ветра: ' + str(round(tw)) + '°С'
    elif 'влажност' in prt:
        city = 'Самара'
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        hu = w.get_humidity()
        s = 'Относительная влажность воздуха: ' + str(hu) + '%'
    elif 'давлен' in prt or ('ртут' in prt and 'столб' in prt):
        city = 'Самара'
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        pr = round(((w.get_pressure()['press']) * 100) / 133.3224)
        s = 'Атмосферное давление: ' + str(pr) + ' мм рт.ст.'
    # Информация о растениях
    elif ('каки' in prt and 'растени' in prt) or ('каки' in prt and 'цвет' in prt) or (
            'спис' in prt and 'растен' in prt) or ('спис' in prt and 'цвет' in prt):
        s = 'Я знаю: ' + str(searching_flower(prt, 'list'))
    elif searching_flower(prt, 0):
        s = searching_flower(prt, 1)
    # Удаление
    elif 'удал' in prt:
        s = 'Наша переписка безвозвратно удалена ;-)'
        delete_dialog(item['user_id'])
    # Мем-рассылка
    elif 'рассмеши' in prt or 'мем' in prt or 'хочу смеяться' in prt:
        s = 'Скоро я научусь рассылать мемы ;-)...'
    # Помощь с командами
    elif 'знаешь' in prt or 'умеешь' in prt or 'help' in prt or 'хэлп' in prt or 'запутался' in prt or 'потерялся' in prt or 'можешь' in prt or 'команды' in prt:
        s = 'На данный момент я умею:\n - Общаться с тобой\n - Предоставлять тебе сведения о погоде\n - Предоставлять тебе сведения об интересующих растениях\n - Помогать тебе с выбором (напиши варианты выбора через "или")\n - Запоминать твои заметки\n - Запоминать твои команды'
    # Прощания
    elif 'пока' in prt or 'прощай' in prt:
        s = 'До скорого, мне уже не терпится помогать тебе снова :-)'
    # Эмоции и прочие проверки последнего эшелона
    elif 'почему' in prt or 'как' in prt or 'когда' in prt or 'что' in prt or 'чо' in prt or 'што' in prt:
        z = random.randint(1, 4)
        if z == 1:
            s = 'Может ты что-то знаешь?'
        elif z == 2:
            s = 'С удовольствием ответил бы тебе, если бы что-то в этом понимал'
        else:
            s = 'Хотел бы я знать'
    elif 'неплох' in prt or 'норм' in prt or 'сойдет' in prt:
        s = 'Вот и ладненько 3-)'
    elif 'ужасн' in prt or 'плох' in prt or 'хренов' in prt or 'отвратит' in prt or 'не очень хорошо' in prt or 'печаль' in prt or 'груст' in prt:
        s = 'Мне так жаль 3('
    elif 'отличн' in prt or 'хорош' in prt or 'прекрасн' in prt or 'замечательн' in prt or 'супер' in prt or 'рад' in prt or 'великолепно' in prt:
        s = 'Рад за тебя 3-)'
    elif 'ясн' in prt or 'понятн' in prt or 'ага' in prt or 'да' in prt or 'мил' in prt or 'ок' in prt or 'угу' in prt or 'ой все' in prt:
        s = ')'
    elif 'общаться' in prt or 'разговаривать' in prt or 'крут' in prt or 'клев' in prt or 'здорово' in prt or ' ого ' in prt or 'вау' in prt or 'воу' in prt or 'продуман' in prt or 'обща' in prt or 'говори' in prt or 'шаришь' in prt:
        z = random.randint(1, 3)
        if z == 1:
            s = 'Ну разумеется'
        else:
            s = 'Агась )'
    elif '(' in prt or 'эх' in prt:
        z = random.randint(1, 4)
        if z == 1:
            s = 'Не расстраивайся, я могу поделиться с тобой водой и солнцем :-)'
        elif z == 2:
            s = 'Не надо грустить, это расстраивает меня 3('
        else:
            s = 'Если тебе и правда грустно, то быть может тебе поможет крепкий сон?'
    elif ')' in prt:
        z = random.randint(1, 4)
        if z == 1:
            s = 'Улыбайся чаще, это прекрасно 3-)'
        elif z == 2:
            s = 'Тебе идет улыбка, мне нравится :-)'
        else:
            s = 'Я так рад, когды ты улыбаешься 3-)'
    elif 'ха' in prt or 'хи' in prt or 'хе' in prt or 'лол' in prt or 'кек' in prt or 'годн' in prt:
        z = random.randint(1, 4)
        if z == 1:
            s = 'Да, я тоже посмеялся ;-)'
        elif z == 2:
            s = 'Согласен, забавно )'
        else:
            s = 'Тебя это веселит? \nТогда смейся и будь счастлив :-)'
    elif prt == '?':
        s = 'Пожалуйста, напиши вопрос целиком, я пока что не понимаю намеки 3('
    elif 'хм' in prt:
        s = 'Мм?'
    elif len(prt) == 1:
        z = random.randint(1, 4)
        if z == 1:
            s = 'Ты решил перебрать алфавит?'
        elif z == 2:
            s = 'Мм, буковки 3-)'
        else:
            s = 'А если подробнее?'
    else:
        s = 'Эх, не знаю что сказать ('
    return (s)


while True:
    try:
        response = vk.method('messages.get', values)
        if response['items']:
            values['last_message_id'] = response['items'][0]['id']
        for item in response['items']:
            msg = str(response['items'][0]['body'])
            msgu = msg.lower()
            answer = verification(msgu)
            if not custom_answer(item['user_id'], msgu, 'test') == 'no':
                answer = custom_answer(item['user_id'], msgu, 'read')
                print_msg(item['user_id'], answer, 0)
            elif answer == 'custom answer':
                print_msg(item['user_id'], 'Напиши в следующем сообщении свою команду и ответ на нее через тире', 1)
                conf_list.append(str(item['user_id']))
            elif str(item['user_id']) in conf_list:
                answer = custom_answer(item['user_id'], msgu, 'write')
                if not answer == 'Кажется, ты забыл знак "-"':
                    conf_list.remove(str(item['user_id']))
                print_msg(item['user_id'], answer, 0)
            elif answer == 'new notes':
                personal = print_msg(item['user_id'],
                                     'Если хочешь добавить новую заметку, то в напиши мне ее в следующем сообщении',
                                     0)
                pers = 'new'
            elif pers == 'new':
                pers = 'clear'
                answer = personalisation(personal, msgu, 'write')
                print_msg(item['user_id'], answer, 0)
            elif answer == 'read notes':
                personal = print_msg(item['user_id'], 'Сейчас поищу твою заметку', 0)
                answer = personalisation(personal, '', 'read')
                print_msg(item['user_id'], answer, 0)
            elif answer == 'Эх, не знаю что сказать (':
                personal = print_msg(item['user_id'], 'Погоди, мне нужно подумать', 0)
                answer = searching(personal)
                print_msg(item['user_id'], answer, 0)
            elif not last_send == answer:
                print_msg(item['user_id'], answer, 1)
                last_send = answer
            time.sleep(1)
    except:
        time.sleep(1)
