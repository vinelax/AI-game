import tkinter as tk
import tkinter.messagebox
import random
import SpelesKoks_MinMaks_AlfaBeta


def choose_player_window():
    def izvelies_starta_speletaju():
        choice = var.get()
        if choice == 1:
            return "Lietotājs"
        elif choice == 2:
            return "Dators"
        else:
            tkinter.messagebox.showerror("Kļūda", "Lūdzu izvēlies spēlētāju lai sāktu spēli.")

    def start_game():
        starting_player = izvelies_starta_speletaju()
        if starting_player:
            tkinter.messagebox.showinfo("Starta Spēlētājs", f"Spēli sāks {starting_player}.")
            window.destroy()

    window = tk.Tk()
    window.title("Izvēlies Starta Spēlētāju")

    label = tk.Label(window, text="Izvēlies kurš no spēlētājiem sāks spēli:")
    label.pack()
    var = tk.IntVar()

    player1_button = tk.Radiobutton(window, text="Lietotājs", variable=var, value=1)
    player1_button.pack()
    player2_button = tk.Radiobutton(window, text="Dators", variable=var, value=2)
    player2_button.pack()

    start_button = tk.Button(window, text="Sākt Spēli", command=start_game)
    start_button.pack()

    window.mainloop()


def choose_algorithm():
    def start_game():
        sp = SpelesKoks_MinMaks_AlfaBeta.Speles_koks()

        algorithm = var.get()
        if algorithm == 1:
            tkinter.messagebox.showinfo("Algoritms izvēlēts", "Tiks lietots Minimaksa algoritms.")
            SpelesKoks_MinMaks_AlfaBeta.minimaks(sp.virsotnu_kopa, sp.loku_kopa)
            window.destroy()
        elif algorithm == 2:
            tkinter.messagebox.showinfo("Algoritms izvēlēts", "Tiks lietots Alpha-beta algoritms.")
            SpelesKoks_MinMaks_AlfaBeta.alfabeta(sp.virsotnu_kopa, sp.loku_kopa, 0, float('-inf'), float('inf'))
            window.destroy()
        else:
            tkinter.messagebox.showerror("Kļūda", "Izvēlies algoritmu lai sāktu spēli.")

    window = tk.Tk()
    window.title("Choose Algorithm")

    label = tk.Label(window, text="Izvēlies algoritmu priekš datora gājieniem:")
    label.pack()

    var = tk.IntVar()

    minimax_button = tk.Radiobutton(window, text="Minimaks", variable=var, value=1)
    minimax_button.pack()

    alphabeta_button = tk.Radiobutton(window, text="Alpha-Beta", variable=var, value=2)
    alphabeta_button.pack()

    start_button = tk.Button(window, text="Sākt spēli", command=start_game)
    start_button.pack()

    window.mainloop()


def game():
    window = tk.Tk()
    window.title("Spēle")
    window.title("Choose Starting Player")
    window.geometry("400x450")

    current_turn = [1]  # Uzglabā informāciju par pašreizējo spēlētāju iekš saraksta, lai būtu iespējama modificēšana
    player_points = [80, 80]  # Sākotnējie punkti abiem spēlētājiem

    #Funkcija jaunas spēles uzsākšanai, visu elementu atjaunošana uz sākuma stāvokli
    def new_game():
        global numbers_list
        numbers_list = []
        ok_button.pack()
        player_points = [80, 80]
        winner_label.config(text="Uzvarētājs:")
        num_input.config(state="normal")
        player_input.config(state="disabled")
        numbers_label.config(text="")
        player1_points_label.config(text="Lietotājs punkti: 80")
        player2_points_label.config(text="Dators punkti: 80")
        new_game_button.pack_forget()

    def update_points():
        # Tā kā current_turn tagad ir saraksts, mēs izmantojam current_turn[0]
        num = int(player_input.get())
        if num in [1, 2, 3]:
            player_points[current_turn[0] - 1] -= num
            global numbers_list
            numbers_list.remove(num)
            numbers_label.config(text = str(numbers_list))
            player1_points_label.config(text=f"Lietotājs punkti: {player_points[0]}")
            player2_points_label.config(text=f"Dators punkti: {player_points[1]}")
            winner_check()

            # Pārslēdzam kārtu uz nākamo spēlētāju
            current_turn[0] = 2 if current_turn[0] == 1 else 1

            # Atjauninām kārtas etiķeti
            turn_label.config(text=f"Spēlētāja kārta: {current_turn[0]}")
            if current_turn[0] == 2:
                computer_turn()
            player_input.delete(0, tk.END)
        else:
            turn_label.config(text="Ievadiet skaitli: 1, 2 vai 3")

    def computer_turn():
        computer_choice = random.choice([1, 2, 3])
        player_points[1] -= computer_choice
        numbers_list.remove(computer_choice)
        numbers_label.config(text=str(numbers_list))
        player1_points_label.config(text=f"Lietotājs punkti: {player_points[0]}")
        player2_points_label.config(text=f"Dators punkti: {player_points[1]}")
        winner_check()

        # Pārslēdzam kārtu uz nākamo spēlētāju
        current_turn[0] = 1

        # Atjauninām kārtas etiķeti
        turn_label.config(text=f"Spēlētāja kārta: {current_turn[0]}")

    #Funkcija, kas nosaka uzvarētāju
    def winner_check():
        global numbers_list
        if not numbers_list:
            winner = None
            if player_points[0] > player_points[1]:
                winner = "Lietotājs"
            elif player_points[0] < player_points[1]:
                winner = "Dators"
            else:
                winner = "Neizšķirts"

            winner_label.config(text=f"Uzvarētājs: {winner}")
            new_game_button.pack()

    instructions_label = tk.Label(window, text="Izvēlies skaitli no 15-25")
    instructions_label.pack()

    num_input = tk.Entry(window)
    num_input.pack()

    def get_input():
        try:
            length = int(num_input.get())
            if 15 <= length <= 25:
                global numbers_list
                numbers_list = [random.randint(1, 3) for _ in range(length)]
                numbers_label.config(text=str(numbers_list))
                player1_points_label.config(text="Lietotājs punkti: 80")
                player2_points_label.config(text="Dators punkti: 80")
                turn_label.config(text="Spēlētāja kārta: 1")
                winner_label.config(text="Uzvarētājs: ")
                player_input.config(state="normal")
                ok_button.pack_forget()
                num_input.config(state="disabled")
            else:
                numbers_label.config(text="Garumam jābūt diapazonā no 15 līdz 25")
        except ValueError:
            numbers_label.config(text="Lūdzu ievadiet skaitli")

    ok_button = tk.Button(window, text="OK", command=get_input)
    ok_button.pack()

    numbers_label = tk.Label(window, text="")
    numbers_label.pack(pady=30)

    turn_label = tk.Label(window, text="Spēlētāja kārta: 1")
    turn_label.pack(pady=10)

    player_input = tk.Entry(window)
    player_input.pack()
    player_input.pack()
    player_input.config(state="disabled")

    player1_points_label = tk.Label(window, text="Lietotājs punkti: 80")
    player1_points_label.pack(pady=10)

    player2_points_label = tk.Label(window, text="Dators punkti: 80")
    player2_points_label.pack(pady=10)

    move_button = tk.Button(window, text="Veikt gājienu", command=update_points)
    move_button.pack(pady=5)

    winner_label = tk.Label(window, text="Uzvarētājs")
    winner_label.pack(pady=20)

    new_game_button = tk.Button(window, text="Spēlēt vēlreiz!", command=new_game)
    move_button.pack()

    tk.mainloop()


def main():
    choose_player_window()
    choose_algorithm()
    game()


if __name__ == '__main__':
    main()
