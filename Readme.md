# Battery Alert Monitor

A simple Windows CLI application that monitors your battery level and alerts you when it drops below a specified threshold.

## Current Functionality

- **Battery Monitoring**: Continuously checks battery percentage in the background
- **Custom Threshold**: Set your preferred alert level (1-100%)
- **CLI Interface**: Simple command-line interface for control
- **Background Threading**: Monitoring runs in background while CLI remains responsive
- **Start/Stop Control**: Toggle monitoring on and off as needed
- **Status Display**: View current monitoring status and threshold

## Installation

### Step 1: Clone the Repository
```bash
git clone git@github.com:Punith-19/CLI-app-to-Warn-low-battery.git
cd battery-alert-monitor
```

### Step 2: Create Virtual Environment (Recommended)

**Create the virtual environment:**
```bash
python -m venv myenv
```

**Activate the virtual environment:**

On Windows Command Prompt:
```bash
myenv\Scripts\activate
```


### Step 3: Install Required Libraries

**With the virtual environment activated, install all dependencies:**
```bash
pip install -r requirements.txt
```

**What gets installed:**
- `psutil` - For reading battery information

**Alternative (manual installation):**
```bash
pip install psutil
```

## How to Run

### Method 1: Using Batch File (Easiest)
Simply double-click `run.bat`
- Note: when bat file is runned it will run in venv ie "myenv"

### Method 2: Using Command Prompt
1. Open Command Prompt in the project folder
2. Run:
```bash
python Main.py
```

### Setup auto start (Batch file needed)
1. Create a short cut for the batch file by left clicking in .bat file.
2. Now click "win+R" and type following command there "shell:startup".
3. File explorer opens in a certain directory paste your .bat file short cut there.
4. Now the script runs on start up, to terminate you can use task manager or "exit" command in CLI.

## Project Structure

```
battery-alert-monitor/
├── Main.py              # Entry point
├── Moniter_battery.py   # Battery monitoring logic
├── clip.py              # CLI interface
├── run.bat              # Batch file for easy execution
├── warning_gui.py       # gui for warning
├── requirements.txt     # Python dependencies
├── config.ini           # Config file to save threshold
├── myenv/               # Virtual environment (not in git)
└── README.md            # This file
```

## How It Works

1. The program runs in the background on start up 
2. Every 50 seconds, it checks your battery percentage
3. If battery is below threshold AND not plugged in, it displays a warning
4. The CLI remains responsive for you to control the monitoring