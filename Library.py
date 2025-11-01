from colorama import init, Fore, Back, Style


init()


print(Fore.RED + "Це червоний текст")
print(Back.GREEN + "Зелений фон")
print(Style.BRIGHT + "Яскравий текст")
print(Style.RESET_ALL + "Повернення до звичайного стилю")


print(Fore.YELLOW + Back.BLUE + "Жовтий текст на синьому фоні")
