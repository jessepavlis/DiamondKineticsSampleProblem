import numpy as np
import pandas as pd


def convert_data_to_data_frame(data):
    return pd.read_csv(data, names=['timestamp', 'ax', 'ay', 'az', 'wx', 'wy', 'wz'], index_col='timestamp')


def get_first_index_of_consecutive_positives(data, limit):
    counter = 0
    for i, value in enumerate(data):
        if np.isnan(value):
            counter = 0
            continue
        if counter == limit - 1:
            return i - counter
        counter += 1
    return None


def get_indexes_of_consecutive_positives(data, limit):
    indexes = []
    counter = 0
    for i, value in enumerate(data):
        if np.isnan(value):
            if counter >= limit:
                indexes.append((i - counter, i - 1))
            counter = 0
        else:
            counter += 1
    if counter >= limit:
        data_length = len(data)
        indexes.append((data_length - counter, data_length - 1))
    return indexes