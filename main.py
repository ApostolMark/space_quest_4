energy = 100
reactor_fixed = False
room_now = ""
have_tool = False
print("Почините реактор и запустите спасательную капсулу ^*-*^")
print("введите help для помощи")
while True:
    command = input(">")
    if (energy == 0):
        print("Кислород на корабле кончился... Видимо, вы тут остались навсегда...")
        break
    if (command == "help"):
        print("""look - описание текущей комнаты
go <направление> - куда идти
take <предмет> - взять предмет
use <предмет> - использовать предмет
energy - узнать свою оставшуюся энергию
exit - выйти из игры
для старта введите go bridge""")
#-------------------------------------------

    elif (command == "go bridge"):
        if (room_now == "" or room_now == "cargo" or room_now == "mess"):
            room_now = "bridge"
            energy -= 5
            print("вы зашли на мостик")
        else:
            print("невозможное действие!")

    elif (command == "go mess"):
        if (room_now == "bridge" or room_now == "reactor"):
            room_now = "mess"
            energy -= 5
            print("вы зашли в каюты")
        else:
            print("невозможное действие!")

    elif (command == "go reactor"):
        if (room_now == "mess"):
            room_now = "reactor"
            print("вы зашли в реактор")
        else:
            print("невозможное действие!")

    elif (command == "go cargo"):
        if (room_now == "bridge" or room_now == "airlock"):
            room_now = "cargo"
            energy -= 5
            print("вы зашли в грузовой отсек")
        else:
            print("невозможное действие!")

    elif (command == "go airlock"):
        if (room_now == "capsule" or room_now == "cargo"):
            room_now = "airlock"
            energy -= 5
            print("вы зашли в шлюз")
        else:
            print("невозможное действие!")
    elif (command == "go capsule"):
        if (room_now == "airlock"):
            room_now = "capsule"
            energy -= 5
            print("вы зашли к спасательной капсуле")
        else:
            print("невозможное действие!")
#-------------------------------------------
    elif (command == "use tool"):
        if (room_now == "reactor"):
            if (have_tool):
                reactor_fixed = True
                print("Вы починили реактор!")
            else:
                print("У вас нет инструмента!")
        else:
            print("тут нечего чинить")
    elif (command == "energy"):
        print(f"Оставшаяся энергия: {energy}")
    elif (command == "exit"):
        exit(0)
    elif (command == "take tool"):
        if (room_now == "cargo" and have_tool == False):
            have_tool = True
            print("Вы подобрали ремонтный инструмент!")
        else:
            print("Тут нечего подбирать")
    elif (command == "use capsule"):
        if (room_now == "capsule"):
            if (reactor_fixed and energy > 0):
                print("Вы выбрались, но видимо только один...")
                break
            else:
                print("Капсула не открывается!")
        else:
            print("Тут нет капсулы!")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif (command == "look"):
        if (room_now == "bridge"):
            print("""Вы стоите на капитанском мостике.
Вы видите 2 двери: грузовой отсек(cargo),
в противоположной стороне - спальная комната(mess)
вокруг только мусор, ничего интересного нет.""")
        elif (room_now == "mess"):
            print("""вы стоите в каютах.
Вы видите 2 двери: капитанский мостик(bridge)
и реакторный отсек(reactor).
Вокруг ничего интересного, только личные вещи экипажа.""")
        elif (room_now == "reactor"):
            print("""Вы стоите в реакторе.
Реактор необходимо починить, но для этого явно нужен какой-то инструмент...
Тут только одна дверь - каюты(mess)""")
        elif (room_now == "cargo"):
            print("""Вы стоите в грузовом отсеке.
Тут 2 двери: мостик капитана(bridge) и шлюз(airlock)""")
            if (have_tool == True):
                print("тут больше ничего нет")
            else:
                print("""Вы заметили что-то на ящике...
похоже на инструмент(tool)""")
        elif (room_now == "airlock"):
            print("""Вы зашли в шлюз.
Тут 2 двери: грузовой отсек(cargo) и капсула спасения(capsule).
Больше тут ничего нет.""")
        elif (room_now == "capsule"):
            print("""вы стоите возле капсулы спасения.
Для её работы нужно починить реактор,
возможно после этого можно будет использовать капсулу(capsule).
Тут 1 дверь - шлюз(airlock)""")
        elif (room_now == ""):
            print("Вы прячетесь в шкафу, звуки снаружи давно затихли...")
    else:
        print("Ошибка!")