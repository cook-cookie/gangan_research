if __name__ == '__main__':
    filename = 'actor.txt'
    actor = {}
    this_year = 2017

    with open(filename) as f:
        actors_list = []
        for line in f.readlines():
            actors_info = (
                line.split()[0],  # 名前
                this_year - int(line.split()[1].split('-')[0]),  # 年齢
                int(line.split()[1].split('-')[0]),  # 年
                int(line.split()[1].split('-')[1]),  # 月
                int(line.split()[1].split('-')[2])  # 日
            )
            actors_list.append(actors_info)

        for elem in sorted(actors_list, key=lambda x: x[1]):
            print('{}\t{}歳 {}年{}月{}日'.format(elem[0].ljust(6), elem[1], elem[2], elem[3], elem[4]))
