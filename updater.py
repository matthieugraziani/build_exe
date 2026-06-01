import requests
from version import APP_VERSION, GITHUB_REPO

def check_for_updates():
    try:
        url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        latest = response.json()
        latest_version = latest["tag_name"].replace("v", "")

        if latest_version != APP_VERSION:
            return {
                "available": True,
                "version": latest_version,
                "download_url": latest["html_url"]
            }
    except Exception as e:
        print("Erreur update:", e)

    return {"available": False}
