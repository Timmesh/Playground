Problem Statement 1: Check whether two strings are anagram of each other
An anagram of a string is another string that contains the same characters, only the order of characters can be different

Method 1 (Use Sorting) - CheckAnagramMain.java   
Time Complexity: O(nLogn)

1. Sort both strings
2. Compare the sorted strings


Method 2.1 (Count characters using array) - CheckAnagram1_1.java
Time Complexity: O(n) 

In the following implementation, it is assumed that the characters are stored using 8 bit and there can be 256 possible characters. 
1. Create count array of size 256.
2. Iterate through every character which are of same length and increment the value in count array for characters in str1 and decrement for characters in str2.
3. Finally, if all count values are 0, then the two strings are anagram of each other.

Method 2.2 (Count characters using HashMap) - CheckAnagram1_2.java
Time Complexity: O(n) 
 
In above implementation we are using extra space as we are creating array of 256 characters but we can optimise it using HashMap where we can store character and count of character in HashMap. 
Idea is to put all characters of one String in HashMap and reducing them as we encounter while looping over other String.

Problem Statement 2: Given a sequence of words, print all anagrams together
Given an array of words, print all anagrams together. For example, if the given array is {“cat”, “dog”, “tac”, “god”, “act”}, then output may be “cat tac act dog god”.
Let there be N words and each word has maximum M characters

Method 1 (Using hashmap) - PrintAnagramTogether1.java
Time Complexity: O(MNLogN) 
Sorting a word takes maximum O(MLogM) time. So sorting N words takes O(NMLogM) time

Here, we first sort each word, use sorted word as key and then put original word in a map. The value of the map will be a list containing all the words which have same word after sorting. 
Lastly, we will print all values from the hashmap where size of values will be greater than 1.

Method 2 (Using hashmap with O(NM) ) - PrintAnagramTogetherMain.java
Time Complexity: O(nm) 
Space Complexity: Let there be N words and each word has maximum M characters, therefore max. storage space for each word with at max. M characters will be O(M), therefore for max N words, it will be O(N*M). Therefore, the upper bound is O(NM).

In the previous approach, we were sorting every string in order to maintain a similar key, but that cost extra time in this approach will take the advantage of another hashmap to maintain the frequency of the characters which will generate the same hash function for different string having same frequency of characters.
Here, we will take HashMap<HashMap, ArrayList>, the inner hashmap will count the frequency of the characters of each string and the outer HashMap will check whether that hashmap is present or not if present then it will add that string to the corresponding list. 

A simple method is to create a Hash Table. Calculate the hash value of each word in such a way that all anagrams have the same hash value. Populate the Hash Table with these hash values. Finally, print those words together with same hash values. A simple hashing mechanism can be modulo sum of all characters. With modulo sum, two non-anagram words may have same hash value. This can be handled by matching individual characters.

