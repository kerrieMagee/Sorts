def radix_sort(nums, wordlist):
    """
      A function that calls a stable count sort from LSD to MSD
       Input: an unsorted list of Ascii values of length N and a list of strings that contain the character represented in the Ascii list
       Output: a sorted list of Ascii representations of the current character within a list of strings
       Complexity:   O(N) where N is the length of nums array  """
    exp = 1
    max = c_max(nums)  #O(N) (length of nums)
    res = []
    while max//exp > 0:   #E size of the exponent is O(c) Because the size of the ascii number is bounded by a constant(loop will run a max of 3 times... 1,10,100 for {a-z} ascii == {97-122}
        nums, wordlist = count_sort(nums, exp, wordlist)   #O(N) where n is the size of Nums array
        exp *= 10
    return nums, wordlist

def count_sort(nums, exp, wordlist):
    """
      A function that stable sorts a list based on the desired place
       Input: an unsorted list of Ascii values of length N and an exponent of size E to determine digit to be stable sorted on, list of strings that are equivalent to the length of ASCII list
       Output: a sorted list of Ascii representation of the MSD of Strings in Wordlist and a sorted list of strings
       Complexity:   O(N) where N is the length of nums array
    """

    countArray = [0] * 10
    position = [0] * 10
    temp = [0] * len(nums)
    res = [0] * len(nums)

    for i in range(0, len(nums)):
        countArray[(nums[i]//exp) % 10] +=1  #formula to extract the current number place being sorted #O(N)

    position[0] = 0
    for j in range(1, len(position)):
        position[j] = position[j - 1] + countArray[j - 1] #counting occurrences and the previous occurrences and adding to the position array  #O(N)

    for k in range(len(nums)):
        temp[position[nums[k]//exp%10]] = k  #adding the sorted array positions to the temp array
        position[nums[k]//exp%10] += 1  #updating the position array as positions are filled so any other occurrence is added to the next position  #O(N)

    num = [0]*len(nums)
    for l in range(len(temp)):
        res[l] = wordlist[temp[l]]   #using the sorted array positions (temp) to add strings from wordlist to res array #O(N)
        num[l] = nums[temp[l]]       #using the sorted array positions (Temp) to add ASCII of current digit from nums to num array #O(N)
    return num, res

def c_max(nums):
    maxno = nums[0]
    for i in nums:
        if i > maxno:
            maxno = i
    return maxno