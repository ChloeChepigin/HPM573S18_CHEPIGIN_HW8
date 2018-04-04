import Parameters as P
import Classes as Cls
import SupportSteadyState as Support

# create a cohort of a game with a fair coin
cohortfaircoingame = Cls.SetOfGames(
    id=1,
    n_games=P.SIM_POP_SIZE,
    prob_head=P.prob_head)
# simulate the cohort
FairGame = cohortfaircoingame.simulation()

# create a cohort of a game with an unfair coin
cohortunfaircoingame = Cls.SetOfGames(
    id=2,
    n_games=P.SIM_POP_SIZE,
    prob_head=P.prob_head_unfair)
# simulate the cohort
UnfairGame = cohortunfaircoingame.simulation()

print("Question 1 answer")
Support.print_outcomes(FairGame, 'With a fair coin:')
Support.print_outcomes(UnfairGame, 'With an unfair coin:')


# print comparative outcomes
Support.print_comparative_outcomes(FairGame, UnfairGame)