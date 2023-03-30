import requests
import json
import time

SYSTEM = True


def stop_system():
    global SYSTEM
    SYSTEM = False


def start_system():
    global SYSTEM
    SYSTEM = True


class DiscordBot:
    def __init__(self, token, status, delay, pause):
        self.token = token
        self.status = status
        self.pause = pause
        i = 0
        try:
            while SYSTEM:
                string = self.status[0:i + 1]
                print(string)
                self.set_status(string)
                i += 1
                if len(string) > len(self.status) - 1:
                    time.sleep(delay)
                    i = 0
                    string = self.status[0:i + 1]
                    print(string)
                    self.set_status(string)
                    i += 1
                time.sleep(delay)

        except KeyboardInterrupt:
            print("Oprire manuala, Status schimbat manual !")
            exit()

    def set_status(self, status):
        requests.patch("https://discord.com/api/v9/users/@me/settings",
                       headers={"authorization": self.token, "content-type": "application/json"},
                       data=json.dumps({"custom_status": {"text": status, "emoji_name": "🤙"}}))
