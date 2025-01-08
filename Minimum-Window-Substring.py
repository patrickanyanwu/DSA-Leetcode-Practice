"""Initialize a hashmap with the frequency of all letters in the other string and initialise a need variable that is equal to the amount of correct frequencies we need.
l and r start at the beginning of first string,
as we increase our window (increment r) we count the frequency of the letters in a hashmap and as we increment the frequency of letters we check if it is equal to the frequency of the same letter in the other strings hashmap.
If the frequency is the same I increase the count of the number of correct frequencies we have.
Once we have the correct frequency’s for all letters in the other string (our have variable is equal to the need variable) essentially when all frequencies needed are equal, we calculate the length (r - l + 1) and store the indexes l and r then keep track of the minimum.
After this  we increment l and reduce the frequency of the letter at l until we have a false substring then the loop continues. 
We then return the string from the lower index to the higher index or we return an empty string. 
O(n) time O(n) space."""
