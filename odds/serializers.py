from rest_framework import serializers
from .models import Match, Bookmaker, CurrentOdds, OddsHistory

class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = ['id', 'home_team', 'away_team', 'match_date','status', 'external_id']


class BookmakerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookmaker
        fields = [
            "id",
            "name",
            "website",
        ]

class CurrentOddsSerializer(serializers.ModelSerializer):
    bookmaker = BookmakerSerializer(read_only=True)
    match = MatchSerializer(read_only=True)

    class Meta:
        model = CurrentOdds
        fields = ['id', 'match', 'bookmaker', 'market', 'outcome', 'value', 'updated_at']    
        read_only_fields = ['id', 'updated_at']

    


class OddsHistorySerializer(serializers.ModelSerializer):

    bookmaker = BookmakerSerializer(read_only=True)
    match = MatchSerializer(read_only=True)

    class Meta:
        model = OddsHistory
        fields = [
            "id",
            "match",
            "bookmaker",
            "market",
            "outcome",
            "value",
            "recorded_at",
        ]

        read_only_fields = ["id", "recorded_at"]   