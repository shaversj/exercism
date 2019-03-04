from operator import attrgetter
from collections import namedtuple
from itertools import groupby

team_results = []
Team = namedtuple("Team", "Name MP W D L P")


def tally(tournament_results):
    multiple_results = tournament_results.split("\n")

    if tournament_results == "":
        return "Team                           | MP |  W |  D |  L |  P"

    else:
        for match in multiple_results:
            match_results = match.split(";")
            first_team, second_team, result = (
                match_results[0],
                match_results[1],
                match_results[2],
            )

            if result == "win":
                first_team = Team(Name=first_team, MP=1, W=1, D=0, L=0, P=3)
                second_team = Team(Name=second_team, MP=1, W=0, D=0, L=1, P=0)
                team_results.append(first_team)
                team_results.append(second_team)

            if result == "loss":
                first_team = Team(Name=first_team, MP=1, W=0, D=0, L=1, P=0)
                second_team = Team(Name=second_team, MP=1, W=1, D=0, L=0, P=3)
                team_results.append(first_team)
                team_results.append(second_team)

            if result == "draw":
                first_team = Team(Name=first_team, MP=1, W=0, D=1, L=0, P=1)
                second_team = Team(Name=first_team, MP=1, W=0, D=1, L=0, P=1)
                team_results.append(first_team)
                team_results.append(second_team)

        new = sorted(team_results, key=attrgetter("Name"))

        dic = {}
        for key, group in groupby(new, key=lambda x: x.Name):
            for x in group:
                if key not in dic:
                    dic[key] = {"MP": x.MP, "W": x.W, "D": x.D, "L": x.L, "P": x.P}
                else:
                    new_MP_value = dic[key]["MP"] + x.MP
                    new_W_value = dic[key]["W"] + x.W
                    new_D_value = dic[key]["D"] + x.D
                    new_L_value = dic[key]["L"] + x.L
                    new_P_value = dic[key]["P"] + x.P

                    dic[key] = {
                        "MP": new_MP_value,
                        "W": new_W_value,
                        "D": new_D_value,
                        "L": new_L_value,
                        "P": new_P_value,
                    }

    title_str()
    return "\n".join(
        [
            repr(f"{k:30} |  {v['MP']} |  {v['W']} |  {v['D']} |  {v['L']} |  {v['P']}")
            for k, v in dic.items()
        ]
    )


def title_str():
    print(repr("Team                           | MP |  W |  D |  L |  P"))
