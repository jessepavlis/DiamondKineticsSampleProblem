import unittest

from data_set_functions import search_continuity_above_value, \
    back_search_continuity_within_range, \
    search_continuity_above_value_two_signals, \
    search_multi_continuity_within_range


class TestDataSetFunctions(unittest.TestCase):

    def test_search_continuity_above_value(self):
        results = search_continuity_above_value('tests/test.csv', 2, 8, .2, 2)
        self.assertEqual(len(results), 6)
        self.assertEqual(results['ax'], None)
        self.assertEqual(results['wz'], 5)

    def test_back_search_continuity_within_range(self):
        results = back_search_continuity_within_range('tests/test.csv', 2, 8,
                                                      .2, .8, 2)
        self.assertEqual(len(results), 6)
        self.assertEqual(results['ax'], None)
        self.assertEqual(results['az'], 4)

    def test_search_continuity_above_value_two_signals(self):
        results = search_continuity_above_value_two_signals(
            'tests/test.csv', 'tests/test.csv', 2, 8, .1, .4, 2
        )
        self.assertEqual(len(results), 2)
        self.assertIn('data1', results)
        self.assertIn('data2', results)
        self.assertEqual(len(results['data1']), 6)
        self.assertEqual(len(results['data2']), 6)
        self.assertEqual(results['data1']['ax'], 6)
        self.assertEqual(results['data1']['wz'], 5)
        self.assertEqual(results['data2']['ay'], 4)
        self.assertEqual(results['data2']['wy'], None)

    def test_search_multi_continuity_within_range(self):
        results = search_multi_continuity_within_range('tests/test.csv', 2, 8,
                                                       -.1, 1, 2)
        self.assertEqual(len(results), 6)
        self.assertEqual(len(results['ax']), 1)
        self.assertIn((6, 7), results['ax'])
        self.assertEqual(len(results['wy']), 1)
        self.assertIn((2, 3), results['wy'])
        self.assertEqual(len(results['wx']), 0)
