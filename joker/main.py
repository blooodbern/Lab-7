import pygsheets


gc = pygsheets.authorize(service_file= 'joker-386922-697e74e49889.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1zuSrduOXo6U-16J1VOKD2rZ8cb9cala3hKfiLBH4p70/edit?usp=sharing')


wk1 = sh[0]


def main():
    raw = 2
    col = 1

    date = wk1.cell((raw, col)).value

    category = input('choose one of categories: food and drink, pets, shopping, to close a program enter exit\ninput a category from proposed: ')
    if category == 'food and drink':

        while date != '':
            date = wk1.cell((raw, col)).value
            joke = wk1.cell((raw, col+1)).value
            print(date, joke)
            raw = raw + 1


    if category == 'pets':
        while date != '':
            date = wk1.cell((raw, col)).value
            joke = wk1.cell((raw, col + 2)).value
            print(date, joke)
            raw = raw + 1

    if category == 'shopping':
        while date != '':
            date = wk1.cell((raw, col)).value
            joke = wk1.cell((raw, col + 3)).value
            print(date, joke)
            raw = raw + 1

    if category == 'exit':
        print('thanx for using')
        exit()
    main()

main()
