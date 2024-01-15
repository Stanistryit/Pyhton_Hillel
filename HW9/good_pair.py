
def good_pair(list1, list2):
    good_pairs_count = 0

    for i in range(len(list1)):
        for j in range(i + 1, len(list2)):
            if list1[i] == list2[j]:
                good_pairs_count += 1

    return good_pairs_count

assert good_pair([1,2,3], [1,2,7,3]) == 1
assert good_pair([1,2,3], [2,4,7,3]) == 1



