from utils import convert_data_to_data_frame, \
    get_first_index_of_consecutive_positives, \
    get_indexes_of_consecutive_positives


def search_continuity_above_value(data, index_begin, index_end, threshold, win_length):
    results = {}
    data_frame = convert_data_to_data_frame(data)
    data_frame = data_frame.loc[index_begin: index_end]
    data_frame = data_frame[data_frame >= threshold]

    for column in data_frame.columns:
        index = get_first_index_of_consecutive_positives(data_frame[column], win_length)
        results[column] = data_frame.index[index] if index else None

    return results


def back_search_continuity_within_range(data, index_begin, index_end, threshold_lo, threshold_hi, win_length):
    results = {}
    data_frame = convert_data_to_data_frame(data)
    data_frame = data_frame.loc[index_begin: index_end]
    data_frame = data_frame[data_frame >= threshold_lo][data_frame <= threshold_hi]

    for column in data_frame.columns:
        index = get_first_index_of_consecutive_positives(data_frame[column][::-1],
                                                         win_length)
        results[column] = data_frame.index[-index] if index else None

    return results


def search_continuity_above_value_two_signals(data1, data2, index_begin, index_end, threshold1, threshold2, win_length):
    return {
        'data1': search_continuity_above_value(data1, index_begin, index_end, threshold1, win_length),
        'data2': search_continuity_above_value(data2, index_begin, index_end, threshold2, win_length)
    }


def search_multi_continuity_within_range(data, index_begin, index_end, threshold_lo, threshold_hi, win_length):
    results = {}
    data_frame = convert_data_to_data_frame(data)
    data_frame = data_frame.loc[index_begin: index_end]
    data_frame = data_frame[data_frame >= threshold_lo][data_frame <= threshold_hi]

    for column in data_frame.columns:
        indexes = get_indexes_of_consecutive_positives(data_frame[column], win_length)
        results[column] = map(lambda x: (data_frame.index[x[0]], data_frame.index[x[1]]), indexes)

    return results
