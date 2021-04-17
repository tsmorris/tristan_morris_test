import re


def compare_versions(V1, V2) -> int:
    #Take a pair of strings representing versions and return 1 if V1 > V2, -1 if V1 < V2, 0 if equal/incomparable
    #split the strings into a set of ints for comparisons
    A = [int(s) for s in re.findall(r'\d+', V1)]
    B = [int(s) for s in re.findall(r'\d+', V2)]
    #Compare each value in V1 to V2, to see if either is higher
    for value in range(0, min(len(A), len(B))):
        if A[value] > B[value]:
            return 1
        if B[value] > A[value]:
            return -1
    #at this point, we've run out of values in one or both so either they're equal or we can't compare further
    return 0 

