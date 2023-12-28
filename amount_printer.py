import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class FileHandler(FileSystemEventHandler):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.latest_line_count = 0
        self.numbers = [
            [
                "  #####  ",
                " ##   ## ",
                "##     ##",
                "##     ##",
                "##     ##",
                " ##   ## ",
                "  #####  "
            ],
            [
                "       ##",
                "       ##",
                "       ##",
                "       ##",
                "       ##",
                "       ##",
                "       ##"
            ],
            [
                "  #####  ",
                "       ##",
                "      ## ",
                "    ###  ",
                "  ##     ",
                " ##      ",
                " ########"
            ],
            [
                "  #####  ",
                "       ##",
                "   ##### ",
                "       ##",
                "       ##",
                " ##    ##",
                "  #####  "
            ],
            [
                " ##   ## ",
                " ##   ## ",
                " ##   ## ",
                " ########",
                "       ##",
                "       ##",
                "       ##"
            ],
            [
                " ########",
                " ##      ",
                " ##      ",
                " ########",
                "       ##",
                "       ##",
                " ########"
            ],
            [
                "  #####  ",
                " ##      ",
                " ##      ",
                " ########",
                " ##    ##",
                " ##    ##",
                "  #####  "
            ],
            [
                " ########",
                "       ##",
                "      ## ",
                "     ##  ",
                "    ##   ",
                "   ##    ",
                "  ##     "
            ],
            [
                "  #####  ",
                " ##   ## ",
                " ##   ## ",
                "  #####  ",
                " ##   ## ",
                " ##   ## ",
                "  #####  "
            ],
            [
                "  #####  ",
                " ##   ## ",
                " ##   ## ",
                "  ###### ",
                "       ##",
                "      ## ",
                "  ####   "
            ]
        ]
        self.update_lines()

    def on_modified(self, event):
        if event.src_path.endswith(self.filename):
            self.update_lines()

    def update_lines(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                line_count = len(lines)
                if line_count != self.latest_line_count:
                    self.latest_line_count = line_count
                    clear_console()

                    line_count_str = str(line_count)
                    for row in range(7):
                        for digit in line_count_str:
                            print(self.numbers[int(digit)][row], end=' ')
                        print()

                    print("Codes Generated!")

        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")

if __name__ == "__main__":
    file_name = "promos.txt"  # Replace with your file name
    event_handler = FileHandler(file_name)
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
