package StringsFIrstAssignments;


/**
 * Write a description of Part1 here.
 * 
 * @author Steven Fuller 
 * @version 4/4/22
 */
public class Part1 {
    public String findSimpleGene (String dna) {
        int startIndex = dna.indexOf("ATG");
        if(startIndex == -1){
            return ("");
        }
        int stopIndex = dna.indexOf("TAA",startIndex+3);
        if(stopIndex == -1){
            return("");
        }
        if ((stopIndex-startIndex)%3 == 0){
            return dna.substring(startIndex, stopIndex+3);
        }
        else{
            return "";
        }
    }
    public void testSimpleGene(){
        String a = "GTATATATGTTGCTAA";
        String b = "GTAGTAAGTAAGAT";
        String c = "ATGGTAGTTAGGGAATGA";
        String d = "AGTCGATAGAT";
        String e = "ATGGTATTGAAGTTTGAATAA";
        
        String aa = findSimpleGene(a);
        System.out.println("String is: " + a);
        System.out.println("Gene is: " + aa);
        
        String bb = findSimpleGene(b);
        System.out.println("String is: " + b);
        System.out.println("Gene is: " + bb);
        
        String cc = findSimpleGene(c);
        System.out.println("String is: " + c);
        System.out.println("Gene is: " + cc);
        
        String dd = findSimpleGene(d);
        System.out.println("String is: " + d);
        System.out.println("Gene is: " + dd);
        
        String ee = findSimpleGene(e);
        System.out.println("String is: " + e);
        System.out.println("Gene is: " + ee);
    }
}
