import Parameters as P
import Classes as Cls
import SupportTransientState as Support

# create multiple cohorts for when the drug is not available
multiCohortFairCoin = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_COHORTS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    n_games_in_a_set=[P.REAL_POP_SIZE] * P.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    prob_head=[P.prob_head]*P.NUM_SIM_COHORTS  # [p, p, ...]
)
# simulate all cohorts
multiCohortFairCoin.simulation()

# create multiple cohorts for when the fair coin
multiCohortWithDrug = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_COHORTS, 2*P.NUM_SIM_COHORTS),   # [NUM_SIM_COHORTS, NUM_SIM_COHORTS+1, NUM_SIM_COHORTS+2, ...]
    n_games_in_a_set=[P.REAL_POP_SIZE] * P.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    prob_head=[P.prob_head_unfair*P.NUM_SIM_COHORTS]*P.NUM_SIM_COHORTS
)
# simulate all cohorts
multiCohortFairCoin.simulation()

# create multiple cohorts for when the drug is available
multiCohortWithUnFairCoin = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_COHORTS, 2*P.NUM_SIM_COHORTS),   # [NUM_SIM_COHORTS, NUM_SIM_COHORTS+1, NUM_SIM_COHORTS+2, ...]
    n_games_in_a_set=[P.REAL_POP_SIZE] * P.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    prob_head=[P.prob_head_unfair*P.NUM_SIM_COHORTS]*P.NUM_SIM_COHORTS)

# simulate all cohorts
multiCohortWithUnFairCoin.simulation()
print("Question 2 Answer")

# print outcomes
Support.print_outcomes(multiCohortFairCoin, 'with the fair coin')
Support.print_outcomes(multiCohortWithUnFairCoin, 'when the unfair coin')


# print comparative outcomes
Support.print_comparative_outcomes(multiCohortFairCoin, multiCohortWithUnFairCoin)