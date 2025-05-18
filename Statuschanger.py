import requests
import time

## 🔴⚠️ MET TON TOKEN ET NE LE PARTAGE JAMAIS LOUOLOU⚠️🔴
TOKEN = ""

def Title(text):
    print(f"=== {text} ===")

def current_time_hour():
    return time.strftime("%H:%M:%S")

def check_token():
    """Vérifie si le token est valide en faisant une requête test."""
    headers = {'Authorization': TOKEN}
    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
    
    if response.status_code == 200:
        print(f"[{current_time_hour()}] ✅ Token valide !")
    else:
        print(f"[{current_time_hour()}] ❌ Erreur : Token invalide ou expiré ({response.status_code})")
        exit(1)

def main():
    print("\nSI TU AS BESOIN D'AIDE CONTACT 632213356127846439 sur Discord ou va sur le serveur https://discord.gg/cx9vJJpVm4\n")
    
    Title("Discord Token Status Changer")
    check_token() 

    headers = {'Authorization': TOKEN, 'Content-Type': 'application/json'}

    ## Ici une ligne sur 4 est expliquer, vous devez faire la meme avec tous

    statuses = [
        {"text": "Le text que tu veut mettre", "emoji_name": "Ici le nom de ton emoji", "emoji_id": "ID de ton emoji"},
        {"text": "", "emoji_name": "", "emoji_id": ""},
        {"text": "", "emoji_name": "", "emoji_id": ""},
        {"text": "", "emoji_name": "", "emoji_id": ""}
    ]

    while True:
        for status in statuses:
            payload = {
                "custom_status": {
                    "text": status["text"],
                    "emoji_name": status["emoji_name"],
                    "emoji_id": status["emoji_id"]
                }
            }

            try:
                response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
                
                if response.status_code == 200:
                    print(f"[{current_time_hour()}] ✅ Statut changé : {status['text']} avec l'emoji {status['emoji_name']}")
                elif response.status_code == 429:
                    retry_after = response.json().get("retry_after", 4)
                    print(f"[{current_time_hour()}] ⚠️ Rate limit atteint ! Attente de {retry_after} secondes...")
                    time.sleep(retry_after)
                else:
                    print(f"[{current_time_hour()}] ❌ Erreur ({response.status_code}) : {response.text}")

                time.sleep(4)  
            except Exception as e:
                print(f"[{current_time_hour()}] ❌ Erreur : {e}")
                time.sleep(4)

if __name__ == "__main__":
    main()
