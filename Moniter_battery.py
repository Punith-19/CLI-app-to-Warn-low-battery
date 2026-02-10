import time
import psutil
import threading
import configparser
from warning_gui import warning
class MoniterBattery:
 
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.running = False
        self.thread = None
        self.threshold = config.get('General', 'th')

    def Battery_check_loop(self):
        # Intervel to read percentage
        sleep_time = 50
        
        while self.running:
            curr_bstter_percent = psutil.sensors_battery().percent
            plugged_in = psutil.sensors_battery().power_plugged
            print(f"\n[DEBUG] Battery: {curr_bstter_percent}%, Plugged: {plugged_in}, Threshold: {self.threshold}%")

            if(int(curr_bstter_percent)<=int(self.threshold) and not plugged_in):
                warning.lowbattery(curr_bstter_percent)
                print("warning battery low plugin")
            else:
                print("no alert")
            time.sleep(sleep_time)

    def start(self):
        if self.running:
            print("\tAlready running")
        else:
            self.running = True
            self.thread = threading.Thread(target = self.Battery_check_loop)
            self.thread.daemon = True
            self.thread.start()
            print("\tMonitoring Started!!")

    def stop(self):
        if self.running:
            self.running = False
            print("\tMonitoring Stopped")
        else:
            print("\tAlready stopped")

    def get_status(self):
        if self.running:
            return "Running" 
        else: return "Stopped"

    def cli_header(self):
        ## display header in cli
        print("\n" + "="*50)
        print("        BATTERY ALERT MONITOR")
        print("="*50)
        print(f"Status: {self.get_status()}")
        print(f"Current threshold: {self.threshold}%")
        print("="*50)

    def set_threshold(self):
        config = configparser.ConfigParser()
        print("\tenter a new threshold value in '%' from 1 to 100")
        a = int(input())
        config['General'] = {'th' : a}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        self.threshold = a
        print(f"\tthreshold changed to {self.threshold}")

    def cli_menu(self):
        print("use:\n 'start' to start monitoring\n 'stop' to stop monitoring\n 'set' to set a new threshold\n 'exit' to terminate program")