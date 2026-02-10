from Moniter_battery import MoniterBattery
from clip import cliclass
def main():
    moniter = MoniterBattery()
    moniter.cli_header()    # Show header
    moniter.start()    
    cliclass.cli(moniter)
if __name__ == "__main__":
    main()