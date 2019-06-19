from typing import List


class Activity:
    """
    Defining an activity by it's starting and ending time point
    """

    def __init__(self, start, end):
        self._start = start
        self._end = end

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    def __str__(self):
        return 'start={};end={}'.format(self.start, self.end)

    def __repr__(self):
        return str(self)


def get_activities(acts: List[Activity]) -> List[Activity]:
    """
    In Activity selection problem (ASP), we need to maximize number
    of non overlapping activities where an activity is defined by
    it's starting and ending time point.

    To do so, we observe that earliest ending activity (say S) can be
    safely put into desired optimal set (sey U). This greedy selection
    has no disadvantage because in otherwise case, an activity (say A)
    will start before and end after S making A overlapping with S.
    If we happen to choose A then S will have to be removed.
    Clearly choosing S over A has advantage as S ends before A.

    Now this strategy can be repeated to find next activity which
    don't overlap with the earlier selected activity until we
    have examined all activities.


    :param acts: Activities defined by starting and ending time.
    :return: maximal non overlapping list of activities.
    """

    output = []

    if acts:
        itr_acts = iter(sorted(acts, key=lambda act: act.end))

        curr = next(itr_acts)

        output.append(curr)

        for act in itr_acts:
            if curr.end <= act.start:
                output.append(act)
                curr = act

    return output


if __name__ == '__main__':
    activity = [Activity(1, 3), Activity(0, 4), Activity(1, 2),
                Activity(4, 6), Activity(2, 9, ), Activity(5, 8),
                Activity(3, 5), Activity(4, 5)]
    print(get_activities(activity))
