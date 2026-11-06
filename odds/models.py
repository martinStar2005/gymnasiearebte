from django.db import models

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
    

class Odds(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    bookmaker = models.ForeignKey(Bookmaker, on_delete=models.CASCADE)
    outcome = models.CharField(max_length=20)
    value = models.DecimalField(max_digits=5, decimal_places=2)

    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.match} - {self.bookmaker}: {self.outcome} at {self.value}"
