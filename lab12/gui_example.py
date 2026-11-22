# gui_example.py
import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Проверка интерфейса")
    value = tk.StringVar()
    result = tk.StringVar(value="Введите название")

    def show_title():
        title = value.get().strip()
        result.set(title if title else "Название не должно быть пустым")

    ttk.Entry(root, textvariable=value).pack(padx=12, pady=8)
    ttk.Button(root, text="Показать", command=show_title).pack(pady=8)
    ttk.Label(root, textvariable=result).pack(padx=12, pady=8)
    root.mainloop()


if __name__ == "__main__":
    main()
