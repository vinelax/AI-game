import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Spēle")
    window.geometry("300x400")

    hello = tk.Label(text="Izvēlies skaitli no 15-25")
    hello.pack()
    
    button = tk.Button(text="OK")
    button.pack()

    lenght = random.randint(15, 25)
    list = [random.randint(1,3) for _ in range (lenght)]
    hello = tk.Label(text= list)
    hello.pack(pady = 30)

    tk.mainloop()


if __name__ == '__main__':
    main()
