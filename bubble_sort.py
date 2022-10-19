unsorted = [4, 1, 5, 8, 3, 9, 7, 6]

def bubble_sort(li):
    # keep a flag for whether or not a swap was made
    has_swapped = True
    while has_swapped:
        # first thing -- set our flag to be False in case no swap is made
        has_swapped = False
        print(li)
        # loop over entire list
        for i in range(len(li) - 1):
            # check neighbor's values
            if li[i] > li[i + 1]:
                # swap them if i is bigger than i + 1
                li[i], li[i + 1] = li[i + 1], li[i]
                # since we made a swap, indicate that another iteration is needed
                has_swapped = True

bubble_sort(unsorted)

print(unsorted)