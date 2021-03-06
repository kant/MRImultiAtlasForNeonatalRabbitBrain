import pandas as pa

import benchmarking.test_retest_intra_rater.a_paths_intra_rater as ph


if __name__ == '__main__':
    # parameters
    print_all = True
    print_some = False

    # data collection:
    names_comparisons = ['Man 1, Man 2 comparison', 'Auto, Man1 comparison', 'Auto, Man 2 comparison']
    list_pa_series_mean = []
    list_pa_series_std = []

    for name_data, pfi_pickle_input in zip(names_comparisons,
        [ph.pfi_pickled_scoring_man1_man2_all, ph.pfi_pickled_scoring_auto_man1_all, ph.pfi_pickled_scoring_auto_man2_all]):

        df_all_labels_measures = pa.read_pickle(pfi_pickle_input)

        if print_all:
            print '======= {} ========='.format(name_data)
            print df_all_labels_measures
            print '\n------------------------'
            print 'Mean for all rows : '
            print df_all_labels_measures.mean()
            print 'Std for all rows : '
            print df_all_labels_measures.std()
            print '\n------------------------'
            print 'Rows with dice smaller than one'
            print df_all_labels_measures.loc[df_all_labels_measures['dice_score'] != 1.0]
            print '\n------------------------'
            print 'NUMBER of rows with dice smaller than one'
            print len(df_all_labels_measures.loc[df_all_labels_measures['dice_score'] != 1.0])
            print '\n------------------------'
            print 'Mean for rows  dice smaller than one: '
            print df_all_labels_measures.loc[df_all_labels_measures['dice_score'] != 1.0].mean()
            print 'Std for rows  dice smaller than one: '
            print df_all_labels_measures.loc[df_all_labels_measures['dice_score'] != 1.0].std()

        if print_some:
            # print only mean and std per group and for dice smaller than one.
            print '\n\n======= {} ========='.format(name_data)
            print '\n------------------------'
            print 'Mean for rows  dice smaller than one: '
            print df_all_labels_measures.loc[df_all_labels_measures['dice_score'] != 1.0].mean()
            print 'Std for rows  dice smaller than one: '
            print df_all_labels_measures.loc[df_all_labels_measures['dice_score'] != 1.0].std()

        list_pa_series_mean += [df_all_labels_measures.loc[df_all_labels_measures['dice_score'] != 1.0].mean()]
        list_pa_series_std += [df_all_labels_measures.loc[df_all_labels_measures['dice_score'] != 1.0].std()]

    # generate latex tables:
    df_means = pa.DataFrame(list_pa_series_mean, names_comparisons)
    df_std = pa.DataFrame(list_pa_series_std, names_comparisons)

    df_means.to_latex(ph.pfi_table_average_all)
    df_std.to_latex(ph.pfi_table_std_all)
