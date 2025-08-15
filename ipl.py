import pandas as pd
import os

# CSV ka full path banate hain
file_path = os.path.join(os.path.dirname(__file__), "data", "ipl-matches.csv")

matches = pd.read_csv(file_path)
print(matches.head())

def teamaAPI():
    teams = list(set(list(matches["Team1"]) + list(matches["Team2"])))  # remove duplicates
    team_dict = {
        "teams": teams
    }
    return team_dict


def teamVteamAPI(team1, team2):
    temp_df = matches[
        ((matches["Team1"] == team1) & (matches["Team2"] == team2)) |
        ((matches["Team1"] == team2) & (matches["Team2"] == team1))
        ]

    total_matches = temp_df.shape[0]

    matches_won_team1 = temp_df["WinningTeam"].value_counts().get(team1, 0)
    matches_won_team2 = temp_df["WinningTeam"].value_counts().get(team2, 0)

    draws = total_matches - (matches_won_team1 + matches_won_team2)

    response = {
        "total_matches": str(total_matches),
        team1: str(matches_won_team1),
        team2: str(matches_won_team2),
        "draws": str(draws)
    }
    return response
