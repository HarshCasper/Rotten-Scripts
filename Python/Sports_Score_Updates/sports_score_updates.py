import sports
import sys

sports_dict = {
    "baseball": sports.BASEBALL,
    "basketball": sports.BASKETBALL,
    "cricket": sports.CRICKET,
    "football": sports.FOOTBALL,
    "handball": sports.HANDBALL,
    "hockey": sports.HOCKEY,
    "rugby-league": sports.RUGBY_L,
    "rugby-union": sports.RUGBY_U,
    "soccer": sports.SOCCER,
    "tennis": sports.TENNIS,
    "volleyball": sports.VOLLEYBALL,
}

argumentList = sys.argv
if len(argumentList) < 2:
    print("Please enter a sport")
    sys.exit()

if len(argumentList) == 2:
    sport = argumentList[1].lower()
    if sport in sports_dict.keys():
        all_matches = sports.all_matches()[sport]
        for match in all_matches:
            print(match)
    else:
        print("This sport details are not supported yet")

if len(argumentList) == 3:
    sport = argumentList[1].lower()
    if (
        sport == "baseball"
        or sport == "basketball"
        or sport == "football"
        or sport == "hockey"
    ):
        sport = sports_dict.get(sport)
        team = argumentList[2].lower()
        team_info = sports.get_team(sport, team)
        print(team_info)
    else:
        print("This sport details are not supported yet")

if len(argumentList) == 4:
    sport = argumentList[1].lower()
    if sport in sports_dict.keys():
        sport = sports_dict.get(sport)
        team1 = argumentList[2].lower()
        team2 = argumentList[3].lower()
        match_info = sports.get_match(sport, team1, team2)
        print(match_info)
    else:
        print("This sport details are not supported yet")
