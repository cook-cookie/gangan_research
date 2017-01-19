from operator import itemgetter

if __name__ == '__main__':
    filename = 'actor.txt'
    actor = {}
    this_year = 2017

    with open(filename) as f:
        for line in f.readlines():
            actor['名前'] = line.split()[0]
            # actor['誕生日'] = line.split()[1]
            actor['年'] = line.split()[1].split('-')[0]
            actor['年齢'] = str(this_year - int(line.split()[1].split('-')[0]))
            actor['月'] = line.split()[1].split('-')[1]
            actor['日'] = line.split()[1].split('-')[2]

        for key, value in sorted(actor.items(), key=itemgetter(1)):
            print(key, value)
        # print('{}\t{}歳 {}年{}月{}日'.format(actor['name'].ljust(6), actor['age'], actor['year'], actor['month'], actor['day']))
