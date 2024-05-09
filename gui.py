import tkinter as tk


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FoxiLoveBot for RoK")

        # Создание текстового поля для вывода сообщений
        self.message_text = tk.Text(self.root, height=10, width=50)
        self.message_text.pack()

        # Создание кнопок
        self.create_button("Запустить Зрение", self.button1_action)
        self.create_button("Остановка маршей", self.button2_action)
        self.create_button("Поиск гемов", self.button3_action)
        self.create_button("Лицей знаний", self.button4_action)

        # Кнопка выхода
        exit_button = tk.Button(self.root, text="Выход", command=root.quit)
        exit_button.pack()

    def create_button(self, text, action):
        button = tk.Button(self.root, text=text, command=action)
        button.pack()

    def button1_action(self):
        self.display_message("Нажата кнопка 1")

    def button2_action(self):
        self.display_message("Нажата кнопка 2")

    def button3_action(self):
        self.display_message("Нажата кнопка 3")

    def button4_action(self):
        self.display_message("Нажата кнопка 4")

    def display_message(self, message):
        self.message_text.insert(tk.END, message + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()