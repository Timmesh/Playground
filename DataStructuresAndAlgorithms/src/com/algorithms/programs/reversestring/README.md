https://www.geeksforgeeks.org/reverse-a-string-in-java/
Problem Statement 1: Reverse a string in Java


Method 1 - ReverseStringMain.java   
1. The idea is to traverse the length of the string 
2. Extract each character while traversing 
3. Add each character in front of the existing string

Method 2.1: Using built in reverse() method of the StringBuilder class - ReverseString2_1.java
String class does not have reverse() method, we need to convert the input string to StringBuilder, which is achieved by using the append method of StringBuilder. After that, print out the characters of the reversed string by scanning from the first till the last index.

Method 2.2: Using built in reverse() method of the StringBuilder class - ReverseString2_2.java
String class does not have reverse() method, we need to convert the input string to StringBuffer, which is achieved by using the reverse method of StringBuffer.

Method 3: Converting String to character array - ReverseString3.java
1. First, convert String to character array by using the built in Java String class method toCharArray().
2. Then, scan the string from end  to start, and print the character one by one.

Method 4: Using ArrayList object - ReverseString4.java
Convert the input string into the character array by using toCharArray() built in method. Then, add the characters of the array into the ArrayList object. Java also has built in reverse() method for the Collections class. Since Collections class reverse() method takes a list object, to reverse the list, we will pass the ArrayList object which is a type of list of characters.

1. We copy String contents to an object of ArrayList.
1. We create a ListIterator object by using the listIterator() method on the ArrayList  object.
2. ListIterator object is used to iterate over the list.
3. ListIterator object helps us to iterate over the reversed list and print it one by one to the output screen.

 