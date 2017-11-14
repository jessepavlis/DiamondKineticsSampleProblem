Our sensors record data from a three-axis accelerometer and a three-axis gyroscope. In order to appropriately use that data, we also need to record the timestamp at which the samples were taken. For any one swing, we'll have about a thousand such samples. I'd like you to put together a data structure that would represent all of this data. Attached to this email is a sample data file arranged in a CSV format. The columns are (in order) timestamp, ax, ay, az, wx, wy, wz. This is an actual data file from a real swing from our sensor - it's not something that we typically share outside of DK, so I'll ask that you keep it somewhat confidential.

To help inform your data structure choices, we typically operate on this data in a sequential fashion starting from either the first element or important indices in the swing data (swing start, impact, swing end, etc.). All of the operations described below will occur on only one (or two, in the case of searchContinuityAboveValueTwoSignals) of the columns.

Once you've got a good data structure in place, I'd like you to implement four of our typical operations on this data set:

* searchContinuityAboveValue(data, indexBegin, indexEnd, threshold, winLength) - from indexBegin to indexEnd, search data for values that are higher than threshold. Return the first index where data has values that meet this criteria for at least winLength samples.
* backSearchContinuityWithinRange(data, indexBegin, indexEnd, thresholdLo, thresholdHi, winLength) - from indexBegin to indexEnd (where indexBegin is larger than indexEnd), search data for values that are higher than thresholdLo and lower than thresholdHi. Return the first index where data has values that meet this criteria for at least winLength samples.
* searchContinuityAboveValueTwoSignals(data1, data2, indexBegin, indexEnd, threshold1, threshold2, winLength) - from indexBegin to indexEnd, search data1 for values that are higher than threshold1 and also search data2 for values that are higher than threshold2. Return the first index where both data1 and data2 have values that meet these criteria for at least winLength samples.
* searchMultiContinuityWithinRange(data, indexBegin, indexEnd, thresholdLo, thresholdHi, winLength) - from indexBegin to indexEnd, search data for values that are higher than thresholdLo and lower than thresholdHi. Return the the starting index and ending index of all continuous samples that meet this criteria for at least winLength data points.

Feel free to use any language of your choosing. I'm more than happy to answer any questions you have about this problem set - or Diamond Kinetics in general.

When you have a solution in place you'd like to share, feel free to upload it to GitHub or Bitbucket for us to take a look at.

As a bonus question, at what index do you think impact happens in this data file?