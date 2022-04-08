
/**
 * Write a description of Part2 here.
 * 
 * @author Steven Fuller 
 * @version 4/4/22
 */
public class Part2 {
    public String findSimpleGene (String dna, String startCodon, String stopCodon) {
        int startIndex = dna.indexOf(startCodon);
        if(startIndex == -1){
            return ("");
        }
        int stopIndex = dna.indexOf(stopCodon,startIndex+3);
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
        String startCodon = "ATG";
        String stopCodon = "TAA";
        
        String aa = findSimpleGene(a, startCodon, stopCodon);
        System.out.println("String is: " + a);
        System.out.println("Gene is: " + aa);
        
        String bb = findSimpleGene(b, startCodon, stopCodon);
        System.out.println("String is: " + b);
        System.out.println("Gene is: " + bb);
        
        String cc = findSimpleGene(c, startCodon, stopCodon);
        System.out.println("String is: " + c);
        System.out.println("Gene is: " + cc);
        
        String dd = findSimpleGene(d, startCodon, stopCodon);
        System.out.println("String is: " + d);
        System.out.println("Gene is: " + dd);
        
        String ee = findSimpleGene(e, startCodon, stopCodon);
        System.out.println("String is: " + e);
        System.out.println("Gene is: " + ee);
    }
}
