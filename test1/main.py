import os.path
import subprocess
import tkinter as tk
import cv2
from PIL import Image, ImageTk

import util


class App:
    def __init__(self):

        self.main_window = tk.Tk()
        self.main_window.geometry("1200x500+350+100")
        self.main_window.title("STAH App")

        self.login_button_main_window = util.get_button(self.main_window, 'Zaloguj sie', 'green', self.login)
        self.login_button_main_window.place(x=780, y=110)

        self.register_button_main_window = util.get_button(self.main_window, 'Zarejestruj użytkownika', 'grey',
                                                           self.register_new_user, fg='black')
        self.register_button_main_window.place(x=780, y=270)

        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

        self.add_webcam(self.webcam_label)

        self.db_dir = r'.\db'
        if not os.path.exists(self.db_dir):
            os.makedirs(self.db_dir)

    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)

        self._label = label

        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()
        self.most_recent_capture_arr = frame #CV2 format

        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)

        self.most_recent_capture_pil = Image.fromarray(img_) #Pillow format

        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(20, self.process_webcam)

    def login(self):
        unknown_img_path = r'.\tmp.jpg'

        cv2.imwrite(unknown_img_path, self.most_recent_capture_arr)
        output = str(subprocess.check_output(['face_recognition', self.db_dir, unknown_img_path ]))
        name = output.split(',')[1][:-5]

        if name in ['unknown_person', 'no_persons_found']:
            util.msg_box("Autoryzacja zakończona fiaskiem", 'Nieznany użytkownik. Proszę spróbuj ponownie albo skontaktuj sie z przełozonym')
        else:
            util.msg_box("Autoryzacja zakończona sukcesem", 'Witaj, {}'.format(name))

        os.remove(unknown_img_path)

    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1200x520+370+120")

        self.accept_button_register_user_window = util.get_button(self.register_new_user_window, "Akceptuj", "green", self.accept_new_user)
        self.accept_button_register_user_window.place(x=750, y=300)

        self.try_again_button_register_user_window = util.get_button(self.register_new_user_window, "Spróbuj ponownie", "red", self.try_again_new_user)
        self.try_again_button_register_user_window.place(x=750, y=400)

        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)

        self.add_img_to_label(self.capture_label)

        self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
        self.entry_text_register_new_user.place(x=750, y=150)

        self.text_label_register_new_user = util.get_text_label(self.register_new_user_window, 'Podaj proszę swoje\nimię i nazwisko:')
        self.text_label_register_new_user.place(x=750, y=70)

    def try_again_new_user(self):
        self.register_new_user_window.destroy()

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_new_user_capture = self.most_recent_capture_arr.copy()

    def accept_new_user(self):
        name = self.entry_text_register_new_user.get(1.0, "end-1c")

        cv2.imwrite(os.path.join(self.db_dir, '{}.jpg'.format(name)), self.register_new_user_capture)

        util.msg_box('Sukces', 'Użytkownik został zarejestrowany')

        self.register_new_user_window.destroy()

    def start(self):
        self.main_window.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()