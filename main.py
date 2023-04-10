import sys
import threading
import tkinter
from tkinter import *
import webbrowser
from tkinter import Tk, Toplevel, Button
from discord import *
from tkinter.ttk import Progressbar

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
PAUSE = True
BACKGROUND_WINDOW = "#34495E"
BUTTONS_BACKGROUND = "#ABB2B9"
INFO_BUTTONS = "white"
FONT_TEXT = ('MathBold', 8, 'bold')
DISCORD_TOKEN_YOUTUBE = "www.youtube.com/watch?v=YEgFvgg7ZPI"
OPENWEATHER_TOKEN_YOUTUBE = "www.youtube.com/watch?v=SPfgbeJGnec"
VERSION = "v1.1"
counter = 1


# Website link
def open_web_browser():
    webbrowser.open("www.adrian-bogdan.com")


# Quit Second Window Fix
def quit_x_button_second_window():
    # quit()
    # exit()
    sys.exit()


class LoginWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pause = True
        self.coco = None
        self.protocol('WM_DELETE_WINDOW', quit_x_button_second_window)
        self.title("Discord Status Changer")
        self.geometry("400x400")
        self.config(bg=BACKGROUND_WINDOW)
        self.resizable(False, False)
        self.after(1000)
        self.iconbitmap('logo.ico')
        self.photo = tkinter.PhotoImage(file='logo.png')
        Button(self, image=self.photo, width=100, height=70, command=open_web_browser).place(x=150, y=10)
        self.progress = Progressbar(self, orient=HORIZONTAL, length=280, mode='indeterminate')
        self.label_write_save = Label(self,
                                      text="Info is saved",
                                      bg=BACKGROUND_WINDOW,
                                      fg="green",
                                      font=FONT_TEXT)
        self.msg_error_api_open = Label(self,
                                        text="Openweathermap API Error",
                                        font=FONT_TEXT,
                                        bg=BACKGROUND_WINDOW,
                                        fg="red")
        self.in_progress_text = Label(self,
                                      text="In Progress",
                                      bg=BACKGROUND_WINDOW,
                                      font=FONT_TEXT,
                                      fg="green")

        self.pause_label = Label(self,
                                 text="Pausing Script Execution",
                                 bg=BACKGROUND_WINDOW,
                                 font=FONT_TEXT,
                                 fg="green")

        # -----------------

        # Label

        var1 = IntVar()
        delay_number = IntVar()
        api_weather = StringVar()
        longitude = StringVar()
        latitude = StringVar()

        def save_weather_api():
            with open("weather_token.txt", "w") as file_weather:
                file_weather.write(api_weather.get())
            with open("longitude.txt", "w") as file_longitude:
                file_longitude.write(longitude.get())
            with open("latitude.txt", "w") as file_latitude:
                file_latitude.write(latitude.get())

            self.label_write_save.place(x=210, y=250)

        def do_test():
            if var1.get() == 1:

                # ------------------------------------------------------------------------ Label Openweather
                self.label_openweather = Label(self,
                                               text="Openweathermap API:",
                                               bg=BUTTONS_BACKGROUND,
                                               font=FONT_TEXT,
                                               width=18)
                self.label_openweather.place(x=70, y=160)

                # ------------------------------------------------------------------------ Entry Openweather

                self.entry_openweather = Entry(self, textvariable=api_weather)
                self.entry_openweather.place(x=210, y=160)

                # ------------------------------------------------------------------------ Label Longitude

                self.label_longitude = Label(self,
                                             text="Longitude:",
                                             bg=BUTTONS_BACKGROUND,
                                             font=FONT_TEXT,
                                             width=18)
                self.label_longitude.place(x=70, y=190)

                # ------------------------------------------------------------------------ Entry Longitude

                self.entry_longitude = Entry(self, textvariable=longitude)
                self.entry_longitude.place(x=210, y=190)

                # ------------------------------------------------------------------------ Label Latitude

                self.label_latitude = Label(self, text="Latitude:",
                                            bg=BUTTONS_BACKGROUND,
                                            font=FONT_TEXT,
                                            width=18)
                self.label_latitude.place(x=70, y=220)

                # ------------------------------------------------------------------------ Entry Latitude

                self.entry_latitude = Entry(self, textvariable=latitude)
                self.entry_latitude.place(x=210, y=220)

                # ------------------------------------------------------------------------ Save Button

                self.save_button = Button(self,
                                          text="Save",
                                          command=save_weather_api,
                                          bg=BUTTONS_BACKGROUND,
                                          font=FONT_TEXT
                                          )
                self.save_button.place(x=300, y=250)

                if len(api_weather.get()) < 1:
                    try:
                        with open("weather_token.txt", "r") as file_weather:
                            file_read = file_weather.read()
                            api_weather.set(file_read)
                    except FileNotFoundError:
                        with open("weather_token.txt", "w") as file_weather:
                            # noinspection PyTypeChecker
                            file_weather.write(api_weather)

                if len(longitude.get()) < 1:

                    try:
                        with open("longitude.txt", "r") as file_longitude:
                            file_read1 = file_longitude.read()
                            longitude.set(file_read1)
                    except FileNotFoundError:
                        with open("longitude.txt", "w") as file_longitude:
                            # noinspection PyTypeChecker
                            file_longitude.write(longitude)

                if len(latitude.get()) < 1:

                    try:
                        with open("latitude.txt", "r") as file_latitude:
                            file_read2 = file_latitude.read()
                            latitude.set(file_read2)
                    except FileNotFoundError:
                        with open("latitude.txt", "w") as file_latitude:
                            # noinspection PyTypeChecker
                            file_latitude.write(latitude)

            else:
                self.label_openweather.place_forget()
                self.entry_openweather.place_forget()
                self.label_longitude.place_forget()
                self.entry_longitude.place_forget()
                self.label_latitude.place_forget()
                self.entry_latitude.place_forget()
                self.save_button.place_forget()
                self.label_write_save.place_forget()

        Label(self,
              text="Delay:",
              bg=BUTTONS_BACKGROUND,
              font=FONT_TEXT).place(x=90, y=101)

        Label(self,
              text="Lower = BAN",
              fg="red",
              bg=BUTTONS_BACKGROUND,
              font=FONT_TEXT).place(x=260, y=101)

        Entry(self, textvariable=delay_number).place(x=130, y=101)
        delay_number.set(3)

        Checkbutton(self,
                    text="Use Weather for your status",
                    variable=var1,
                    onvalue=1,
                    offvalue=0,
                    command=do_test,
                    bg=BUTTONS_BACKGROUND,
                    font=FONT_TEXT).place(
            x=90, y=130)

        def discord_start():
            if PAUSE:
                with open("discord_token.txt", "r") as discord_file_text:
                    discord_token = discord_file_text.read()
                    discord_file_text.close()
                with open("status_text.txt", "r") as status_file_text:
                    status_text = status_file_text.read()
                    status_file_text.close()

                    DiscordBot(token=discord_token, status=status_text, delay=delay_number.get(), pause=PAUSE)
            self.after(1000)

        def start_discord_with_weather_status():
            if PAUSE:
                with open("discord_token.txt", "r") as discord_file_text:
                    discord_token = discord_file_text.read()
                    discord_file_text.close()

                    # Weather Discord Status --------------------

                    parameters = {
                        "lat": latitude.get(),
                        "lon": longitude.get(),
                        "appid": api_weather.get(),
                        "exclude": "current,minutely,daily"
                    }

                    if requests.patch(OWM_Endpoint, params=parameters).status_code == 405:
                        response = requests.get(OWM_Endpoint, params=parameters)
                        response.raise_for_status()
                        data = response.json()

                        self.msg_error_api_open.destroy()

                        code_list = []
                        will_do_something = ""
                        weather_slice = data["hourly"][:12]

                        for hour_data in weather_slice:
                            condition_code = hour_data["weather"][0]["id"]
                            code_list.append(hour_data)

                            if int(condition_code) < 700:
                                will_do_something = "rain"
                            elif 300 < int(condition_code) < 500:
                                will_do_something = "drizzle"
                            elif 500 < int(condition_code) < 600:
                                will_do_something = "rain"
                            elif 700 < int(condition_code) < 800:
                                will_do_something = "fog-sand"
                            elif int(condition_code) == 800:
                                will_do_something = "clear"
                            elif 800 < int(condition_code) < 900:
                                will_do_something = "clouds"

                        # Create a custom status depends on the weather
                        if will_do_something == "thunderstorm":
                            status = "Thunderstorm ⚡"
                        elif will_do_something == "drizzle":
                            status = "Drizzle 💨"
                        elif will_do_something == "rain":
                            status = "Rain 🌧"
                        elif will_do_something == "fog-sand":
                            status = "Fog.. 🌫"
                        elif will_do_something == "clear":
                            status = "Clear Sky 🔵"
                        elif will_do_something == "clouds":
                            status = "Clouds ☁"

                        # --------------------------------------------

                        DiscordBot(token=discord_token, status=status, delay=delay_number.get(), pause=PAUSE)
                    else:
                        self.in_progress_text.place_forget()
                        self.progress.place_forget()
                        self.msg_error_api_open.place(x=90, y=290)
                        stop_system()

            self.after(1000)

        def start_threading():
            start_system()
            if var1.get() == 1:
                self.button_start.config(relief=SUNKEN, state=DISABLED)
                self.pause_button.config(text="PAUSE", relief=RAISED, state=ACTIVE)
                self.label_write_save.config(text="")
                self.progress.place(x=50, y=290)
                self.progress.start()
                self.in_progress_text.config(text="In Progress")
                self.in_progress_text.place(x=160, y=260)
                threading.Thread(target=start_discord_with_weather_status, daemon=True).start()
                self.after(250)
            else:
                self.button_start.config(relief=SUNKEN, state=DISABLED)
                self.pause_button.config(text="PAUSE", relief=RAISED, state=ACTIVE)
                self.label_write_save.config(text="")
                self.msg_error_api_open.destroy()
                self.progress.place(x=50, y=290)
                self.progress.start()
                self.in_progress_text.config(text="In Progress")
                self.in_progress_text.place(x=160, y=260)
                threading.Thread(target=discord_start, daemon=True).start()
                self.after(250)

        def stop_threading():
            # quit()
            # exit()
            sys.exit()

        def pause_threading():
            stop_system()
            self.button_start.config(relief=RAISED, state=ACTIVE)
            self.progress.stop()
            self.label_write_save.config(text="")
            self.in_progress_text.config(text="PAUSE SCRIPT")
            self.pause_button.config(text="PAUSE", relief=SUNKEN, state=DISABLED)

        self.button_start = Button(self,
                                   text="START",
                                   command=start_threading,
                                   bg=BUTTONS_BACKGROUND,
                                   font=FONT_TEXT,
                                   width=14,
                                   activebackground="green")
        self.button_start.place(x=25, y=330)

        self.quit_button = Button(self,
                                  text="QUIT",
                                  command=stop_threading,
                                  bg=BUTTONS_BACKGROUND,
                                  font=FONT_TEXT,
                                  width=14,
                                  activebackground="red")

        self.quit_button.place(x=265, y=330)

        self.pause_button = Button(self,
                                   text="PAUSE",
                                   command=pause_threading,
                                   bg=BUTTONS_BACKGROUND,
                                   font=FONT_TEXT,
                                   width=14,
                                   activebackground="yellow")
        self.pause_button.place(x=145, y=330)

        Label(self, text="Discord Status Changer",
              bg=BACKGROUND_WINDOW,
              fg=BUTTONS_BACKGROUND,
              font=FONT_TEXT).place(x=130, y=370)

        Label(self,
              text=VERSION,
              bg=BACKGROUND_WINDOW,
              fg=BUTTONS_BACKGROUND,
              font=('MathBold', 8, 'bold')).place(x=370, y=380)

        def function_do_nothing():
            pass

        def open_next_information():
            global counter

            if counter < 2:
                InformationTab().protocol("WM_DELETE_WINDOW", function_do_nothing)
                counter += 1

        Button(self, text="Info",
               command=open_next_information,
               bg=INFO_BUTTONS, width=7,
               activebackground="#0080FF",
               font=FONT_TEXT).place(x=30, y=30)

        # -----------------


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Discord Status Changer")
        self.geometry("400x400")
        self.resizable(False, False)
        self.after(1000)
        self.iconbitmap('logo.ico')
        self.config(bg=BACKGROUND_WINDOW)
        self.photo = tkinter.PhotoImage(file='logo.png')
        Button(self, image=self.photo, width=100, height=70, command=open_web_browser).place(x=150, y=20)

        # Label

        Label(text="Discord API:",
              bg=BUTTONS_BACKGROUND,
              width=12,
              font=FONT_TEXT).place(x=30, y=130)
        Label(text="Set Status:",
              bg=BUTTONS_BACKGROUND,
              width=12,
              font=FONT_TEXT).place(x=30, y=160)

        # Entry box

        # -- Discord Token Entry Box
        text_discord = StringVar()
        Entry(textvariable=text_discord, width=36).place(x=140, y=130)
        with open("discord_token.txt", "r") as file_text:
            tex_discord_var = file_text.read()
            if len(tex_discord_var) > 50:
                text_discord.set(tex_discord_var)
                file_text.close()

        # -- Status Msg Entry Box
        text_status = StringVar()
        Entry(textvariable=text_status, width=36).place(x=140, y=160)

        # Button Login

        def function_do_nothing():
            pass

        def open_new_information():
            global counter
            if counter < 2:
                InformationTab().protocol("WM_DELETE_WINDOW", function_do_nothing)
                counter += 1

        def button_login_do_something():
            self.login_button.config(state=DISABLED)
            if requests.patch("https://discord.com/api/v9/users/@me",
                              headers={"authorization": text_discord.get(),
                                       "content-type": "application/json"}).status_code == 400:
                with open("discord_token.txt", "w") as file_discord:
                    file_discord.write(text_discord.get())
                with open("status_text.txt", "w") as file_status:
                    file_status.write(text_status.get())
                    Label(text="Successful connection !",
                          bg=BACKGROUND_WINDOW,
                          fg="green",
                          font=FONT_TEXT).place(x=130, y=240)
                    self.update()
                    time.sleep(1)
                    self.open_window()
                    self.withdraw()

            else:
                self.login_button.config(state=ACTIVE)
                Label(text="Discord API issue !",
                      bg=BACKGROUND_WINDOW,
                      fg="red",
                      font=FONT_TEXT).place(x=147, y=240)

        self.login_button = Button(text="Login",
                                   command=button_login_do_something,
                                   bg=BUTTONS_BACKGROUND,
                                   width=15,
                                   height=2,
                                   activebackground="green",
                                   font=FONT_TEXT)
        self.login_button.place(x=140, y=190)

        self.info_button = Button(text="Info",
                                  command=open_new_information,
                                  bg=INFO_BUTTONS, width=7,
                                  activebackground="#0080FF",
                                  font=FONT_TEXT)
        self.info_button.place(x=300, y=205)

        def quit_first_window():
            # quit()
            sys.exit()

        Button(text="Quit",
               command=quit_first_window,
               bg=INFO_BUTTONS, width=7,
               activebackground="red",
               font=FONT_TEXT).place(x=300, y=240)

        Label(text="Discord Status Changer",
              bg=BACKGROUND_WINDOW,
              fg=BUTTONS_BACKGROUND,
              font=FONT_TEXT).place(x=130, y=370)

        Label(text=VERSION,
              bg=BACKGROUND_WINDOW,
              fg=BUTTONS_BACKGROUND,
              font=('MathBold', 8, 'bold')).place(x=370, y=380)

    # Open a new window function // Button

    def open_window(self):
        window = LoginWindow(self)
        window.grab_set()


class InformationTab(Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-topmost', 1)
        self.title("Information")
        self.geometry("300x300")
        self.resizable(False, False)
        self.iconbitmap('logo.ico')
        self.config(bg=BACKGROUND_WINDOW)

        # How to use label

        Label(self,
              text="How to use ?",
              font=('MathBold', 12, 'bold'),
              fg=BUTTONS_BACKGROUND,
              bg=BACKGROUND_WINDOW).place(x=100, y=10)


        # Create Label for each step in tutorial  ---------------------------------------------------->

        def open_website_discord_token():
            webbrowser.open(DISCORD_TOKEN_YOUTUBE)

        def open_website_openweathermap_token():
            webbrowser.open(OPENWEATHER_TOKEN_YOUTUBE)

        Label(self,
              text="1.Get your Discord Token",
              font=('MathBold', 10, 'bold'),
              fg=BUTTONS_BACKGROUND,
              bg=BACKGROUND_WINDOW).place(x=30, y=50)

        Button(self,
               text="How to get your Discord Token",
               font=('MathBold', 10, 'bold'),
               fg=BUTTONS_BACKGROUND,
               bg=BACKGROUND_WINDOW,
               command=open_website_discord_token).place(x=50, y=80)

        Label(self,
              text="2.Get your Openweathermap Token",
              font=('MathBold', 10, 'bold'),
              fg=BUTTONS_BACKGROUND,
              bg=BACKGROUND_WINDOW).place(x=30, y=115)

        Button(self,
               text="Get Openweathermap Token",
               font=('MathBold', 10, 'bold'),
               fg=BUTTONS_BACKGROUND,
               bg=BACKGROUND_WINDOW,
               command=open_website_openweathermap_token).place(x=50, y=145)

        Label(self,
              text="3.Set status and click Login",
              font=('MathBold', 10, 'bold'),
              fg=BUTTONS_BACKGROUND,
              bg=BACKGROUND_WINDOW).place(x=30, y=180)

        Label(self,
              text="4.Check If you want to see the weather",
              font=('MathBold', 10, 'bold'),
              fg=BUTTONS_BACKGROUND,
              bg=BACKGROUND_WINDOW).place(x=30, y=210)

        Label(self,
              text="5.Press Start",
              font=('MathBold', 10, 'bold'),
              fg=BUTTONS_BACKGROUND,
              bg=BACKGROUND_WINDOW).place(x=30, y=240)

        # Function for quit process

        def tab_quit():
            global counter
            counter -= 1
            self.destroy()

        # Close window button

        Button(self, text="Close",
               command=tab_quit,
               bg=BUTTONS_BACKGROUND,
               font=FONT_TEXT,
               activebackground="red").place(x=130, y=270)

    def information_window_destroy(self):
        self.destroy()


def quit_x_button_first_window():
    # quit()
    # exit()
    sys.exit()


if __name__ == '__main__':
    root = MainWindow()
    root.attributes('-topmost', 1)
    root.protocol('WM_DELETE_WINDOW', quit_x_button_first_window)
    LoginWindow.mainloop(root)
    LoginWindow.attributes(root, '-topmost', 1)
    root.after(1000)
    LoginWindow.after(root, 1000)
