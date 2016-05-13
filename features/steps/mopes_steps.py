# -- FILE: features/steps/mopes_steps.py
from behave import given, when, then, step
# from mopes import Game, Team, Player, Ball
from mopes import Game, Team, Player, Ball


@given(u'we have an empty game')
def step_impl(context):
    context.game = Game()


@given(u'we have team {team_id:d} with players {player1_name} and {player2_name}')
def step_impl(context, team_id, player1_name, player2_name):
    p1 = Player(player1_name)
    p2 = Player(player2_name)
    if team_id == 1:
        context.team1 = Team(p1, p2)
    elif team_id == 2:
        context.team2 = Team(p1, p2)
    else:
        raise ValueError("Team id not valid")


@when(u'we add the team {team_id:d} to the game')
def step_impl(context, team_id):
    if team_id == 1:
        context.game.set_team1(context.team1)
    elif team_id == 2:
        context.game.set_team2(context.team2)
    else:
        raise ValueError("Team id not valid to add to the game")


@then(u'the team {team_id:d} should have a score of {score:d} points')
def step_impl(context, team_id, score):
    if team_id == 1:
        assert context.game.score.team1 == score
    elif team_id == 2:
        assert context.game.score.team2 == score
    else:
        raise ValueError("Team " + team_id + " hasn't " + score + " points")


@given(u'we have an initialized game with two teams')
def step_impl(context):
    team1 = Team(Player("Barça"), Player("Granada"))
    team2 = Team(Player("Real Madrid"), Player("Deportivo"))
    context.game = Game()
    context.game.set_team1(team1)
    context.game.set_team2(team2)


@given(u'the current ball color is {color}')
def step_impl(context, color):
    ball = Ball(color)
    context.game.set_ball(ball)


@when(u'the team {team_id:d} scores a goal')
def step_impl(context, team_id):
    context.game.goal(team_id)


@given(u'the next sequence of score actions')
def step_impl(context):
    for row in context.table:
        context.game.set_ball(row['ball'])
        context.game.goal(int(row['team']))


@given(u'the team {team_id:d} has a score of {score:d} points')
def step_impl(context, team_id, score):
    assert context.game.get_score().get_points(team_id) == score


@then(u'the game is over')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the game is over')


@then(u'the winner team is the team 1')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the winner team is the team 1')


@given(u'the team 2 has a score of 0 points')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the team 2 has a score of 0 points')


@when(u'the team 1 scores an autogoal')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the team 1 scores an autogoal')


@given(u'the team 1 has a score of 1 points')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the team 1 has a score of 1 points')
