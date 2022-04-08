
/**
 * Write a description of Part3 here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Part3 {
    public boolean twoOccurrences(String stringa, String stringb){
        int counter = 0;
        if(stringb.contains(stringa)){
            int position = stringb.indexOf(stringa);
            int len = stringb.length();
            String stringc = stringb.substring(position,len);
            if(stringc.contains(stringa)){
                return true;
            }
            else{
             return false;   
            } 
        }
        else{
            return false;
        }
    }
    
    public String lastPart(String stringa, String stringb){
        if(stringb.contains(stringa)){
        int lena = stringa.length();
        int lenb = stringb.length();
        int stringaEndPosition = stringb.indexOf(stringa) + lena;
        return  stringb.substring(stringaEndPosition, lenb);
        }
        else{
            return stringb;
        }
    
    }
    
    
    public void testing(){
        System.out.println(twoOccurrences("a","banana"));
        System.out.println(twoOccurrences("zoo","forest"));
        
        String resultLastPart = lastPart("an","banana");
        System.out.println(resultLastPart);
        
        resultLastPart = lastPart("zoo","forest");
        System.out.println(resultLastPart);
    }
}

