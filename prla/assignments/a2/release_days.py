import csv
from pprint import pprint
import datetime


# def release_days(cast, dates, actors):

def release_days(cast, dates, actors):
    cast_lis = open(cast, newline='')
    cast_reader = csv.reader(cast_lis)
    cast_header = next(cast_reader)
    cast_data = [row for row in cast_reader]
    print(cast_header)
    titles = set()
    for ac in actors:
        name = ac.lower()
        for d in cast_data:
            if d[2].lower() == name:
                titles.add(d[0])
    # pprint(titles)

    # Data search by actor.
    # t_set = set()
    # for d in cast_data:
    #     if d[2].lower() == 'meg ryan' or d[2].lower() == 'tom hanks':
    #         # t_set.add(d[0])
    #         print(d)
    # pprint(t_set)

    # Dates and shit.
    # Filter by USA releses.
    dates_lis = open(dates, newline='')
    dates_reader = csv.reader(dates_lis)
    dates_header = next(dates_reader)
    dates_data = [row for row in dates_reader]
    dat = []
    print(dates_header)
    for d in dates_data:
        if d[0] in titles and d[2] == 'USA':
            sdfg = d[3].split('-')
            ye, mo, da = sdfg
            dat.append(dict({d[0]: datetime.date(int(ye), int(mo), int(da))}))
    pprint(dat)
    # dick = dict()
    # for i in range(1, 8):
    #     result = set()
    #     for df in dat:
    #         if wert.weekday() + 1 == i:
    #             result.add(df.keys())
    #     if len(result) > 0:
    #         dick[i] = result
    # pprint(dick)

    # for i, df in enumerate(dat):
    #     dic_lis = set()
    #     ye, mo, da = df[1]
    #     wert = datetime.date(int(ye), int(mo), int(da))
    #     if wert.weekday() == i:
    #         dic
    #     dick.update({wert.weekday(): d[0]})
    #     print(dick)
    #     # print(ye, mo, da)

print(release_days(
    './data/cast.csv', './data/dates.csv', ['Tom Hanks', 'Meg Ryan']))
# {2: {'Kate & Leopold'},
#  3: {'A League of Their Own',
#      'Catch Me If You Can',
#      'Forrest Gump',
#      'Innerspace',
#      'Nothing in Common',
#      'The Money Pit',
#      'The Polar Express',
#      'Toy Story',
#      'Toy Story 2'},
#  5: {'Addicted to Love',
#      'Against the Ropes',
#      'Amityville 3-D',
#      'Anastasia',
#      'Angels & Demons',
#      'Apollo 13',
#      'Armed and Dangerous',
#      'Bachelor Party',
#      'Big',
#      'Bridge of Spies',
#      'Captain Phillips',
#      'Cars',
#      'Cast Away',
#      "Charlie Wilson's War",
#      'City of Angels',
#      'Cloud Atlas',
#      'Courage Under Fire',
#      'D.O.A.',
#      'Dragnet',
#      'Extremely Loud & Incredibly Close',
#      'Flesh and Bone',
#      'French Kiss',
#      'Hanging Up',
#      "He Knows You're Alone",
#      'Hurlyburly',
#      'In the Cut',
#      'In the Land of Women',
#      "Io sono l'amore",
#      'Joe Versus the Volcano',
#      'Larry Crowne',
#      'Philadelphia',
#      'Prelude to a Kiss',
#      'Proof of Life',
#      'Punchline',
#      'Radio Flyer',
#      'Restoration',
#      'Road to Perdition',
#      'Saving Mr. Banks',
#      'Saving Private Ryan',
#      'Serious Moonlight',
#      'Sleepless in Seattle',
#      'Splash',
#      'Sully',
#      'That Thing You Do!',
#      "The 'Burbs",
#      'The Bonfire of the Vanities',
#      'The Da Vinci Code',
#      'The Doors',
#      'The Great Buck Howard',
#      'The Green Mile',
#      'The Ladykillers',
#      'The Man with One Red Shoe',
#      'The Presidio',
#      'The Queen',
#      'The Simpsons Movie',
#      'The Terminal',
#      'Top Gun',
#      'Toy Story 3',
#      'Turner & Hooch',
#      'Volunteers',
#      'When Harry Met Sally...',
#      'When a Man Loves a Woman',
#      "You've Got Mail"},
#  7: {'I.Q.'}}
