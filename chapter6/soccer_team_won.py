def final_score(home, away):
    home = int(home)
    away = int(away)
    if home > away:
        print("Team1 won the Game")
    else:
        print("Team2 won the Game")    


team1 = input("Enter team1 score: ")
team2 = input("Enter team2 score: ")

final_score(team1, team2)