import random
import os
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

def generate_card(bin_format, count):
    cards = []
    for _ in range(count):
        card = bin_format
        while 'x' in card:
            card = card.replace('x', str(random.randint(0, 9)), 1)
        mm = str(random.randint(1, 12)).zfill(2)
        yy = str(random.randint(datetime.now().year + 1, datetime.now().year + 5))[-2:]
        cvv = str(random.randint(100, 999))
        cards.append(f"{card}|{mm}|{yy}|{cvv}")
    return cards

def print_ascii():
    print(Fore.RED + Style.BRIGHT + "\n" + "="*60)
    print(Fore.MAGENTA + Style.BRIGHT + """
     █████╗ ██╗     ██████╗ ██╗  ██╗ █████╗     ██████╗ ███████╗██╗   ██╗
    ██╔══██╗██║     ██╔══██╗██║  ██║██╔══██╗    ██╔══██╗██╔════╝██║   ██║
    ███████║██║     ██████╔╝███████║███████║    ██║  ██║█████╗  ██║   ██║
    ██╔══██║██║     ██╔═══╝ ██╔══██║██╔══██║    ██║  ██║██╔══╝  ╚██╗ ██╔╝
    ██║  ██║███████╗██║     ██║  ██║██║  ██║    ██████╔╝███████╗ ╚████╔╝ 
    ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝  ╚═══╝  
    """)
    print(Fore.CYAN + Style.BRIGHT + "    " + "▀" * 54)
    print(Fore.YELLOW + Style.BRIGHT + "    " + "█" * 2 + " CARD GENERATOR TOOL " + "█" * 2)
    print(Fore.GREEN + Style.BRIGHT + "    " + "▄" * 54)
    print(Fore.RED + Style.BRIGHT + "="*60 + "\n")

def print_main_menu():
    print(Fore.BLUE + "[1] GEN VISA")
    print(Fore.BLUE + "[2] GEN MASTER")
    print(Fore.BLUE + "[3] GEN Discover")
    print(Fore.BLUE + "[4] UPDATE")
    print(Fore.BLUE + "[5] EXIT\n")

def print_save_menu():
    print(Fore.GREEN + "[1] SAVE")
    print(Fore.GREEN + "[2] DON'T SAVE")
    print(Fore.GREEN + "[3] REGEN\n")

def get_target():
    while True:
        try:
            target = int(input(Fore.YELLOW + "YOU WANT? (Enter number of cards): "))
            if target > 0:
                return target
            else:
                print(Fore.RED + "Please enter a number greater than 0.")
        except:
            print(Fore.RED + "Invalid input. Enter a number.")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_ascii()
        print_main_menu()
        choice = input(Fore.YELLOW + "SELECT ANY OPTION (1-5): ")

        if choice == '1':
            target = get_target()
            cards = generate_card("439700004xxxxxxxx", target)
        elif choice == '2':
            target = get_target()
            cards = generate_card("555270xxxxxxxxxx", target)
        elif choice == '3':
            target = get_target()
            cards = generate_card("601100xxxxxxxxxx", target)
        elif choice == '4':
            print(Fore.YELLOW + "UPDATE COMING SOON...")
            input("Press ENTER to continue...")
            continue
        elif choice == '5':
            print(Fore.RED + "EXITING... THANK YOU!")
            break
        else:
            print(Fore.RED + "INVALID OPTION!")
            input("Press ENTER to retry...")
            continue

        os.system('cls' if os.name == 'nt' else 'clear')
        print_ascii()
        for c in cards:
            print(Fore.LIGHTCYAN_EX + c)

        print("\n")
        print_save_menu()
        save_opt = input(Fore.YELLOW + "SELECT OPTION (1-3): ")

        if save_opt == '1':
            if not os.path.exists("Results"):
                os.makedirs("Results")
            file_path = f"Results/CARDS-{datetime.now().strftime('%H%M%S')}.txt"
            with open(file_path, 'w') as f:
                f.write("\n".join(cards))
            print(Fore.GREEN + f"Saved to {file_path}")
        elif save_opt == '2':
            print(Fore.YELLOW + "Not saved!")
        elif save_opt == '3':
            continue
        else:
            print(Fore.RED + "Invalid Save Option!")

        input(Fore.CYAN + "\nPress ENTER to return to main menu...")

if __name__ == "__main__":
    main()
