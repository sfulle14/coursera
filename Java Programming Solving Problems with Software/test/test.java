package test;


/**
 * Write a description of test here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class test {
    public void findAbc(String input) {
    int index = input.indexOf("abc");
    while (true) {
        if (index == -1 || index >= input.length() - 3) {
            break;
        }
        //System.out.println(index+1);
        //System.out.println(index+4);
        //System.out.println("index: " + index);
        String found = input.substring(index+1, index+4);
        System.out.println(found);
        index = input.indexOf("abc", index+3);
        //System.out.println("Index after updating: " + index);
    }
}
   public void test() {
    //Part 1
    //findAbc("abcd");
    //findAbc("abcdabc");
    //findAbc("yabcyabc");
    //findAbc("abcbbbabcdddabc");
    
    //Part 2
    //findAbc("abcdkfjsksioehgjfhsdjfhksdfhuwabcabcajfieowj");
    findAbc("abcabcabcabca");
}
}
