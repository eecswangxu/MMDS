import math

TOTAL_CT = 101
TOTAL_SLOT = 3

budget = [1, 2, 3, 4, 5]
bid = [0.1, 0.09, 0.08, 0.07, 0.06]
max_ct = [math.floor(budget[i] / bid[i]) for i in range(5)]

CTR = [[.015, .016, .017, .018, .019],
       [.01, .012, .014, .015, .016],
       [.005, .006, .007, .008, .010]]


num_ct = [0, 0, 0, 0, 0]
ended = [False, False, False, False, False]
i = 1
TOTAL_CT_reached = False

while True:
    #print "Round {0}".format(i)
    #num_ct

    # no advertiser has budget any more
    if not (False in ended):
        print "no advertiser has budget any more"
        break

    if TOTAL_CT_reached:
        print "the total number of click-throughs reaches the limit"
        break

    ignore = [False, False, False, False, False]
    for slot in range(TOTAL_SLOT):
        print "slot {0}".format(slot)
        max_expected_yield = -1
        advertiser_chosen = -1
        for advertiser in range(5):
            if not ended[advertiser] and not ignore[advertiser]:
                expected_yield = bid[advertiser] * CTR[slot][advertiser]
                if expected_yield > max_expected_yield:
                    max_expected_yield = expected_yield
                    advertiser_chosen = advertiser

        print "advertiser_chosen {0}".format(advertiser_chosen)
        ignore[advertiser_chosen] = True
        num_ct[advertiser_chosen] += CTR[slot][advertiser_chosen]
        print num_ct

        # if the total number of click-throughs reaches the limit
        if sum([round(x) for x in num_ct]) == TOTAL_CT:
            print "the total number of click-throughs reaches the limit"
            TOTAL_CT_reached = True
            break
        if round(num_ct[advertiser_chosen]) == max_ct[advertiser_chosen]:
            ended[advertiser_chosen] = True

    i += 1

print num_ct
