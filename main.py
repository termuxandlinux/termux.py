import subprocess
import os

# Die Liste der Termux-Befehle mit kürzeren Namen
command_list = [
    "am", "am-socket", "api-start", "api-stop", "audio-info", "backup", "battery-status", "brightness",
    "call-log", "camera-info", "camera-photo", "change-repo", "clipboard-get", "clipboard-set",
    "contact-list", "dialog", "download", "fingerprint", "fix-shebang", "info", "infrared-frequencies",
    "infrared-transmit", "job-scheduler", "keystore", "location", "media-player"
]

# Kürzere Namen für die Termux-Befehle
short_command_names = [
    "am", "socket", "api-start", "api-stop", "audio-info", "backup", "battery", "brightness",
    "call-log", "camera-info", "camera-photo", "change-repo", "clipboard-get", "clipboard-set",
    "contact-list", "dialog", "download", "fingerprint", "fix-shebang", "info", "infrared-freq.",
    "infrared-trans.", "job-scheduler", "keystore", "location", "media-player"
]

def clear_screen():
    # Terminal leeren
    subprocess.run("clear", shell=True)

def show_ascii_art():
    # ASCII-Art-Bild in bunten Farben
    print("\033[32m  _____   ", end="")
    print("     _____   \033[0m")
    print("\033[32m |  __ \  ", end="")
    print("   |  __ \  \033[0m")
    print("\033[32m | |__) |__", end="")
    print("_  | |__) |__\033[0m")
    print("\033[32m |  ___/ _ \\", end="")
    print(" |  ___/ _ \\\033[0m")
    print("\033[32m | |  | (_) |", end="")
    print(" | | |  | (_) |\033[0m")
    print("\033[32m |_|   \___/ ", end="")
    print("|_|_|   \___/ \033[0m")

def show_menu(language):
    show_ascii_art()
    print("Easy Termux CMD Menu")
    if language == "deutsch":
        print("Bitte wählen Sie einen Befehl aus:")
    else:
        print("Please select a command:")
    
    for index, command in enumerate(command_list, 1):
        print(f"\033[32m[{index}] {short_command_names[index-1]}\033[0m", end="\t")
        if index % 2 == 0:
            print()

    if language == "deutsch":
        print("\n[99] setup.sh ausführen")
        print("[0] Beenden")
    else:
        print("\n[99] Run setup.sh")
        print("[0] Exit")

def main():
    clear_screen()
    language = input("Choose language / Wählen Sie die Sprache (Deutsch/English): ").lower()
    while language not in ["deutsch", "english"]:
        print("Invalid language / Ungültige Sprache")
        language = input("Choose language / Wählen Sie die Sprache (Deutsch/English): ").lower()

    while True:
        show_menu(language)
        choice = input("Enter your choice / Geben Sie Ihre Auswahl ein: ")
        if choice == '0':
            break
        elif choice == '99':
            # Hier kannst du setup.sh ausführen
            subprocess.run([".shell/setup.sh"], shell=True)
        elif not choice.isdigit() or int(choice) < 1 or int(choice) > len(command_list) + 1:
            print("Invalid choice / Ungültige Auswahl")
        else:
            command_index = int(choice) - 1
            command = f"termux-{command_list[command_index]}"
            print(f"Executing command: {command}")
            # Befehl ausführen
            result = subprocess.run([command], capture_output=True, text=True, shell=True)
            print(result.stdout)


if __name__ == "__main__":
    main()
