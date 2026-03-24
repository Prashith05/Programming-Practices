# WAP to sort a given list WITHOUT ANY IN-BUILT FUNCTIONS
# Bubble Sort/ Sinking Sort

# * Start the iteration using 2 variable 'i' and 'j'
# * Compare 2 adjacent elements
# * If 1st element > 2nd elements:
#       * Swap the elements

l = [3,1,8,7,2]
print(f"Original List: {l}")
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
print(f"Sorted List: {l}")