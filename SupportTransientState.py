import scr.FormatFunctions as Format
import scr.StatisticalClasses as Stat
import Parameters as P


def print_outcomes(multi_cohort, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param multi_cohort: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and confidence interval text of patient survival time
    mean_reward_PI_text = Format.format_estimate_interval(
        estimate=multi_cohort.get_double_mean_of_rewards(),
        interval=multi_cohort.get_PI_mean_of_rewards(alpha=P.ALPHA),
        deci=1)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of mean reward and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          mean_reward_PI_text)



def print_comparative_outcomes(multi_cohort_with_faircoin, multi_cohort_with_unfaircoin):
    # this prints the expected and percentage increase in average reward
    """
    :param multi_cohort_with_faircoin: simulating multiple cohorts with a fair coin
    :param multi_cohort_with_unfaircoin: simulating multiple cohorts with an unfair coin
    :return:
    """

    # increase in survival time
    increase = Stat.DifferenceStatIndp(
        name='Increase in mean reward',
        x=multi_cohort_with_unfaircoin.get_mean_of_rewards(),
        y_ref=multi_cohort_with_faircoin.get_mean_of_rewards()
    )
    # estimate and prediction interval
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_PI(alpha=P.ALPHA),
        deci=1
    )
    print("Expected increase in mean rewards and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

