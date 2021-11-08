import sys

def main():
    lst = sys.argv[0]
    target = sys.argv[1]
    def twoSum(lst, target):
        hm = {}
        for i, v in enumerate(lst):
            diff = target - lst[i]
            print("diff", diff, "list[i]", lst[i])
            if diff in hm:
                return [hm[v], i]
            hm[i] = diff


