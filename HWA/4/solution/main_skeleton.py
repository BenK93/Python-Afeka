# import module as shortname
from module_skeleton import init_db, calc_group_means, calc_side_effects_frequencies, save_side_effect_freqs, \
    plot_side_effect_freqs


def main():
    # Q1 call init_db with "corona_demo.csv" file as input
    db = init_db("corona_demo.csv")
    # Q3 call 'calc_group_means'
    # with "antibodies level" as feature column
    # and "treatment group" as group column
    group_means = calc_group_means("antibodies level", "treatment group")
    # print the header of db for verification of the above two functions
    print(db.head())
    # Q4 call 'calc_side_effects_frequencies'
    side_effect_freqs = calc_side_effects_frequencies()

    print(side_effect_freqs.head())
    # Q5 call 'save_side_effect_freqs' with "side_effect_freqs.csv" as input file name
    #
    save_side_effect_freqs("side_effect_freqs.csv")
    # Q6 call 'validate_side_effect_freqs' function
    plot_side_effect_freqs()
    # Q7 Bonus
    # call 'validate_side_effect_freqs' to validate Q5 results

if __name__=="__main__":
    # evoke main
    main()