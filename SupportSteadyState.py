import scr.FormatFunctions as Format
import scr.StatisticalClasses as Stat
import Parameters as P


def print_outcomes(sim_output, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param sim_output: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and confidence interval text of patient survival time
    reward_mean_CI_text = Format.format_estimate_interval(
        estimate=sim_output.get_ave_reward(),
        interval=sim_output.get_CI_reward(alpha=P.ALPHA),
        deci=1)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of mean reward and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          reward_mean_CI_text)

def print_comparative_outcomes(sim_output_faircoin, sim_output_unfaircoin):
    """ prints expected and percentage increase in survival time when drug is available
    :param sim_output_faircoin: output of a cohort simulated with a fair coin
    :param sim_output_unfaircoin: output of a cohort simulated with an unfair coin
    """

    # increase in rewards
    increase = Stat.DifferenceStatIndp(
        name='Increase in rewards for owner using an unfair coin',
        x=sim_output_unfaircoin.get_rewards(),
        y_ref=sim_output_faircoin.get_rewards())

    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_t_CI(alpha=P.ALPHA),
        deci=1)

    print("Average increase in rewards and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

