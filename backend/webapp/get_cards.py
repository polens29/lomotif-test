import requests
import json

from .models import CardSet, Card

r = requests.get('https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/Rastakhan%27s%20Rumble',
                         headers={'X-Mashape-Key': 'ZTMJtzbYvXmshPTFEZI4ztIy3I68p1nPwgHjsnIGukKZeJxGcs'})

if r.status_code == 200:
    cardSet_name = 'Rastakhan’s Rumble'
    cardSet, created = CardSet.objects.get_or_create(name=cardSet_name)
    cards = json.loads(r.text)

    for card in cards:
        newCard = Card.objects.create(
            name=card.get('name', None),
            dbfId=card.get('dbfId', None),
            text=card.get('text', None),
            locale=card.get('locale', None),
            type=card.get('type', None),
            playerClass=card.get('playerClass', None),
            cardId=card.get('cardId', None),
            health=card.get('health', None),
            cardSet_id=cardSet.id
        )