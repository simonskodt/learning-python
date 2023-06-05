from collections import Counter

def main():
    _, K = map(int, input().split())
    A = list(map(int, input().split()))
    dict = initilize_dict_of_occurences(A)

    while K != 0:
        key_with_max_val = find_most_common_occurence(dict)
        dict[key_with_max_val] -= 1
        K -= 1
    
    key = find_most_common_occurence(dict)
    print(dict[key]) # largest value

# Create dictionary with amount of occurences for each element
def initilize_dict_of_occurences(lst):
    return dict(Counter(lst))

# Finding the key for the largest value
def find_most_common_occurence(dict):
    return max(dict, key=dict.get)

if __name__ == "__main__":
    main()