class Score(object):
    def __init__(self):
        self.team1 = 0
        self.team2 = 0

    def inc(self, team_id, value):
        if (team_id == 1):
            self.team1 += value
        elif (team_id == 2):
            self.team2 += value

    def get_score(self,team_id):
        if (team_id == 1):
            return self.team1
        elif (team_id == 2):
            return self.team2


class Ball(object):
    WHITE = "white"
    BLUE = "blue"
    DISCONTINHA = "yellow"

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def get_points(self):
        points = 0
        if self.color == self.WHITE:
            points = 1
        elif self.color == self.BLUE:
            points = 2
        elif self.color == self.DISCONTINHA:
            points = -1

        return points


class Game(object):
    def __init__(self):
        self.score = Score()
        self.ball_color = "white"

    def set_team1(self, team1):
        self.team1 = team1

    def set_team2(self, team2):
        self.team2 = team2

    def set_ball(self, ball_color):
        self.ball = Ball(ball_color)

    def goal(self, team_number):
        self.score.inc(team_number, self.ball.get_points())


class Team(object):
    def __init__(self, player1, player2):
        self.score = 0
        self.player1 = player1
        self.player2 = player2


class Player(object):
    def __init__(self, player_name):
        self.name = player_name
