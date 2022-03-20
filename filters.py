def translate_day(value):
    days = {
        'mon': 'Понедельник',
        'tue': 'Вторник',
        'wed': 'Среда',
        'thu': 'Четверг',
        'fri': 'Пятница',
        'sat': 'Суббота',
        'sun': 'Воскресенье'
    }
    return days[value]


def translate_travel(value):
    goals = {
        'travel': 'путешествий',
        'relocate': 'переезда',
        'study': 'школы',
        'work': 'работы',
    }
    return goals[value]
