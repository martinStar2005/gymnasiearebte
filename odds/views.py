
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

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

        team = request.query_params.get("team")
        status = request.query_params.get("status")

        if team:
            matches = matches.filter(
                home_team__icontains=team 
            ) | matches.filter(
                away_team__icontains=team
            )

        if status:
            matches = matches.filter(
                status__iexact=status
            )

        serializer = MatchSerializer(
            matches,
            many=True
        )

        return Response(serializer.data)


class MatchDetailView(RetrieveAPIView):

    # def get(self, request, match_id):
    #     match = get_object_or_404(Match, id=match_id)

    #     serializer = MatchSerializer(match)

    #     return Response(serializer.data)

    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    lookup_field = "id"
    lookup_url_kwarg = "match_id"


class MatchCreateView(CreateAPIView):

    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class BookmakerListView(ListAPIView):

    # def get(self, request):
    #     bookmakers = Bookmaker.objects.all()

    #     serializer = BookmakerSerializer(
    #         bookmakers,
    #         many=True
    #     )

    #     return Response(serializer.data)

    queryset = Bookmaker.objects.all()
    serializer_class = BookmakerSerializer


class CurrentOddsListView(ListAPIView):

    # def get(self, request):
    #     odds = CurrentOdds.objects.all()

    #     serializer = CurrentOddsSerializer(
    #         odds,
    #         many=True
    #     )

    #     return Response(serializer.data)

    queryset = CurrentOdds.objects.all()
    serializer_class = CurrentOddsSerializer


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


class OddsHistoryListView(ListAPIView):

    # def get(self, request):
    #     history = OddsHistory.objects.all()

    #     serializer = OddsHistorySerializer(
    #         history,
    #         many=True
    #     )

    #     return Response(serializer.data)
    
    queryset = OddsHistory.objects.all()
    serializer_class = OddsHistorySerializer