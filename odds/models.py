from django.db import models
from django.db.models import Q

class Match(models.Model):
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    match_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('upcoming', 'Upcoming'), ('live', 'Live'), ('finished', 'Finished')])
    external_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.match_date}"
    

class Bookmaker(models.Model):
    name = models.CharField(max_length=100, unique=True)
    external_id = models.CharField(max_length=100, unique=True)
    website = models.URLField()

    def __str__(self):
        return self.name
    


class CurrentOdds(models.Model):
    match = models.ForeignKey(
        Match,
        on_delete=models.CASCADE,
        related_name="current_odds"
    )

    bookmaker = models.ForeignKey(
        Bookmaker,
        on_delete=models.CASCADE,
        related_name="current_odds"
    )

    market = models.CharField(max_length=50)
    outcome = models.CharField(max_length=100)

    value = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["match", "bookmaker", "market", "outcome"],
                name="unique_current_odds"
            ),
            models.CheckConstraint(
                condition=models.Q(value__gt=0),
                name="current_odds_must_be_positive"
            ),
        ]

    def __str__(self):
        return f"{self.bookmaker} - {self.outcome}: {self.value}"


class OddsHistory(models.Model):
    match = models.ForeignKey(
        Match,
        on_delete=models.CASCADE,
        related_name="odds_history"
    )

    bookmaker = models.ForeignKey(
        Bookmaker,
        on_delete=models.CASCADE,
        related_name="odds_history"
    )

    market = models.CharField(max_length=50)
    outcome = models.CharField(max_length=100)

    value = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(value__gt=0),
                name="history_odds_must_be_positive"
            ),
        ]

    def __str__(self):
        return f"{self.bookmaker} - {self.outcome}: {self.value}"
