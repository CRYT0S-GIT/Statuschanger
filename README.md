# 💬 Discord Status Changer (avec Token Utilisateur)

Ce projet est un **script Python** permettant de changer automatiquement le **statut personnalisé** de votre compte Discord à intervalles réguliers.  
Il utilise directement l’API Discord via un token utilisateur (⚠️ à ne jamais partager).

---

## 🛠️ Fonctionnalités

- 🔄 Change automatiquement le statut personnalisé (texte + emoji)
- ✅ Vérifie la validité du token Discord
- 🕒 Affiche l’heure de chaque changement
- ⚠️ Gère les limitations d’API (rate limits)

---

## 🧪 Exemple de statut configuré

```python
statuses = [
    {
        "text": "Le text que tu veut mettre",      # Le message affiché dans ton statut
        "emoji_name": "Ici le nom de ton emoji",   # Exemple : "🔥"
        "emoji_id": "ID de ton emoji"              # Facultatif (nécessaire pour les emojis de serveurs)
    },
    {
        "text": "", "emoji_name": "", "emoji_id": ""
    },
    ...
]
