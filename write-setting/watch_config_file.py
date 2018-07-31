import configparser, os, time
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

iniFilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.ini')
mode = []
class IniFileHandler(PatternMatchingEventHandler):
    def __init__(self, patterns, callback):
        super(IniFileHandler, self).__init__(patterns)
        self.callback = callback

    def on_modified(self, event):
        if event.is_directory:
            return
        try:
            inifile = configparser.ConfigParser()
            inifile.read(iniFilePath, 'UTF-8')
            mode = inifile.get('setting', 'mode')
            self.callback(mode)
        except configparser.NoSectionError:
            pass

def set_mode(value):
    mode[0] = value

if __name__ == '__main__':
    # load setting on fist
    inifile = configparser.ConfigParser()
    inifile.read(iniFilePath, 'UTF-8')
    mode.append(inifile.get('setting', 'mode'))

    # set watchdog handler
    event = IniFileHandler(['*.ini'], set_mode)
    observer = Observer()
    observer.schedule(event, os.path.dirname(os.path.abspath(__file__)), recursive=True)
    observer.start()

    # loop and print setting value
    while True:
        print(mode)
        time.sleep(1)
