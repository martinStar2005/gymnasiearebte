
from django.urls import path
from . import views

urlpatterns = [
    path(
        "matches/",
        views.MatchListView.as_view(),
        name="match-list"
    ),

    path(
        "bookmakers/",
        views.BookmakerListView.as_view(),
        name="bookmaker-list"
    ),

    path(
        "odds/",
        views.CurrentOddsListView.as_view(),
        name="odds-list"
    ),

    path(
        "matches/<int:match_id>/odds/",
        views.MatchOddsView.as_view(),
        name="match-odds"
    ),

    path(
        "odds/history/",
        views.OddsHistoryListView.as_view(),
        name="odds-history"
    ),

    path(
        "matches/<int:match_id>/",
        views.MatchDetailView.as_view(),
        name="match-detail"
    ),

    path(
        "matches/create/",
        views.MatchCreateView.as_view(),
        name="match-create"
    )
]
