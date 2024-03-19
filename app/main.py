import tkinter as tk
import random

def main():
    window = tk.Tk()
    window.title("Spēle")
    window.geometry("400x450")

    current_turn = [1]  # Uzglabā informāciju par pašreizējo spēlētāju iekš saraksta, lai būtu iespējama modificēšana
    player_points = [80, 80]  # Sākotnējie punkti abiem spēlētājiem

    def update_points():
        # Tā kā current_turn tagad ir saraksts, mēs izmantojam current_turn[0]
        num = int(player_input.get())
        if num in [1, 2, 3]:
            player_points[current_turn[0] - 1] -= num
            player1_points_label.config(text=f"Spēlētājs 1 punkti: {player_points[0]}")
            player2_points_label.config(text=f"Spēlētājs 2 punkti: {player_points[1]}")
            
            # Pārslēdzam kārtu uz nākamo spēlētāju
            current_turn[0] = 2 if current_turn[0] == 1 else 1
            
            # Atjauninām kārtas etiķeti
            turn_label.config(text=f"Spēlētāja kārta: {current_turn[0]}")
            player_input.delete(0, tk.END)
        else:
            turn_label.config(text="Ievadiet skaitli: 1, 2 vai 3")


    

    instructions_label = tk.Label(window, text="Izvēlies skaitli no 15-25")
    instructions_label.pack()
    
    num_input = tk.Entry(window)
    num_input.pack()
    
    def get_input():
        try:
            length = int(num_input.get())
            if 15 <= length <= 25:
                numbers_list = [random.randint(1, 3) for _ in range(length)]
                numbers_label.config(text=str(numbers_list))
                player1_points_label.config(text="Spēlētājs 1 punkti: 80")
                player2_points_label.config(text="Spēlētājs 2 punkti: 80")
                turn_label.config(text="Spēlētāja kārta: 1")
                winner_label.config(text="Uzvarētājs: ")
                player_input.config(state="normal")
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

    player1_points_label = tk.Label(window, text="Spēlētājs 1 punkti: 80")
    player1_points_label.pack(pady=10)

    player2_points_label = tk.Label(window, text="Spēlētājs 2 punkti: 80")
    player2_points_label.pack(pady=10)

    move_button = tk.Button(window, text="Veikt gājienu", command=update_points)
    move_button.pack(pady=5)

    winner_label = tk.Label(window, text="Uzvarētājs")
    winner_label.pack(pady=20)

    tk.mainloop()




if __name__ == '__main__':
    main()
