import random

from django.db.models import Max, Q
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.serializers import CardSerializer
from .models import Card

# Create your views here.
class CardView(APIView):

    def get(self, request, playerClass):
        playerClass = playerClass.title()
        max_id = Card.objects.all().aggregate(max_id=Max("id"))['max_id']
        cards = []
        while len(cards) < 30:
            pk = random.randint(1, max_id)
            try:
                card = Card.objects.filter(Q(playerClass=playerClass) | Q(playerClass='Neutral'), pk=pk).exclude(name="").first()
                if card:
                    serialized_card = CardSerializer(card).data
                    if cards.count(serialized_card) < 2:
                        cards.append(serialized_card)
            except:
                pass


        return Response(cards)