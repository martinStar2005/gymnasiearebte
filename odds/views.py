
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Match, Bookmaker, CurrentOdds, OddsHistory

from .serializers import (
    MatchSerializer,
    BookmakerSerializer,
    CurrentOddsSerializer,
    OddsHistorySerializer,
)


class MatchListView(APIView):

    def get(self, request):
        matches = Match.objects.all()

        serializer = MatchSerializer(
            matches,
            many=True
        )

        return Response(serializer.data)


class MatchDetailView(APIView):

    def get(self, request, match_id):
        match = get_object_or_404(Match, id=match_id)

        serializer = MatchSerializer(match)

        return Response(serializer.data)


class BookmakerListView(APIView):

    def get(self, request):
        bookmakers = Bookmaker.objects.all()

        serializer = BookmakerSerializer(
            bookmakers,
            many=True
        )

        return Response(serializer.data)


class CurrentOddsListView(APIView):

    def get(self, request):
        odds = CurrentOdds.objects.all()

        serializer = CurrentOddsSerializer(
            odds,
            many=True
        )

        return Response(serializer.data)


class MatchOddsView(APIView):

    def get(self, request, match_id):
        match = get_object_or_404(Match, id=match_id)

        odds = CurrentOdds.objects.filter(
            match=match
        )

        serializer = CurrentOddsSerializer(
            odds,
            many=True
        )

        return Response(serializer.data)


class OddsHistoryListView(APIView):

    def get(self, request):
        history = OddsHistory.objects.all()

        serializer = OddsHistorySerializer(
            history,
            many=True
        )

        return Response(serializer.data)
