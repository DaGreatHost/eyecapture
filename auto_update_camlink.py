import requests
import time

def get_ngrok_url():
    try:
        tunnels = requests.get("http://127.0.0.1:4040/api/tunnels").json()
        for tunnel in tunnels['tunnels']:
            if tunnel['proto'] == 'https':
                return tunnel['public_url']
    except Exception as e:
        print(f"❌ Failed to get ngrok URL: {e}")
        return None

def update_camlink_file(ngrok_url, filepath='camlink.txt'):
    try:
        with open(filepath, 'w') as f:
            f.write(ngrok_url)
        print(f"✅ camlink.txt updated with: {ngrok_url}")
    except Exception as e:
        print(f"❌ Failed to update camlink.txt: {e}")

print("🔄 Looking for ngrok HTTPS URL...")
while True:
    url = get_ngrok_url()
    if url:
        update_camlink_file(url)
        break
    time.sleep(5)
