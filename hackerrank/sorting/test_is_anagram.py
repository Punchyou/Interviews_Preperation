from collections import defaultdict

def is_anagram(str1):

    lookup = []
    count = 0
    for i in range(len(str1)):
        for j in range(i, len(str1)):
            sorted_sub_str = "".join(sorted(str1[i:j+1]))
            if sorted_sub_str not in lookup:
                lookup.append(sorted_sub_str)
            else:
                count += 1
    return count

print(is_anagram("kkkk"))