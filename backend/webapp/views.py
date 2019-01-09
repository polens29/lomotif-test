import random

from django.db.models import Max, Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.serializers import CardSerializer
from .models import Card


class CardView(APIView):

    def get(self, request, playerClass):
        playerClass = playerClass.title()

        # Get max ID from Card model
        max_id = Card.objects.all().aggregate(max_id=Max("id"))['max_id']
        cards = []

        # Get 30 cards
        while len(cards) < 30:
            # Pick random number from 1 to max ID
            pk = random.randint(1, max_id)

            # Filter card with random number and playerClass
            card = Card.objects.filter(Q(playerClass=playerClass) | Q(playerClass='Neutral'), pk=pk).first()
            if card:
                serialized_card = CardSerializer(card).data

                # Maximum of two same cards
                if cards.count(serialized_card) < 2:
                    cards.append(serialized_card)

        return Response(cards, status=status.HTTP_200_OK)
    