package StringSecondAssignments;


/**
 * Write a description of Part2 here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Part2 {
    public int howMany(String stringa, String stringb){
        int count = 0;
        int firstIndex = stringb.indexOf(stringa);
        if(firstIndex > -1){
            count += 1;
            
            while(stringb.indexOf(stringa, firstIndex) != -1 && firstIndex != -1){
                count += 1;
                firstIndex = stringb.indexOf(stringa, firstIndex + stringa.length());
            }
            count = count -1;
        }
        else{
            count = 0;
        }
        return count;
    }
    
    public void testHowMany(){
        String stringa = "GAA";
        String stringb = "ATGAACGAATTGAATC";
        howMany(stringa,stringb);
        if (howMany(stringa,stringb) == 0) {
            System.out.println("no occurrence found");
        }
        else{
            System.out.println("Last Count is: " + howMany(stringa,stringb));
        }
        stringa = "AA";
        stringb = "ATAAAA";
        howMany(stringa,stringb);
        if (howMany(stringa,stringb) == 0) {
            System.out.println("no occurrence found");
        }
        else{
            System.out.println("Last Count is: " + howMany(stringa,stringb));
        }
        stringa = "AA";
        stringb = "ATABABAB";
        howMany(stringa,stringb);
        if (howMany(stringa,stringb) == 0) {
            System.out.println("no occurrence found");
        }
        else{
            System.out.println("Last Count is: " + howMany(stringa,stringb));
        }
        stringa = "ACAB";
        stringb = "AAAAACABACABAAAACABACABAA";
        howMany(stringa,stringb);
        if (howMany(stringa,stringb) == 0) {
            System.out.println("no occurrence found");
        }
        else{
            System.out.println("Last Count is: " + howMany(stringa,stringb));
        }
        }
}
