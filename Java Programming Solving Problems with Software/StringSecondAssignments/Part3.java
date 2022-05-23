package StringSecondAssignments;


/**
 * Write a description of Part3 here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Part3 {
    public int findStopCodon(String dna, int startIndex, String stopCodon) {
        startIndex = dna.indexOf("ATG");
        int currIndex = dna.indexOf(stopCodon, startIndex + 3);
        while (currIndex != -1) {
            int diff = (currIndex - startIndex) % 3;
            if (diff == 0) {
                return currIndex;
            }
            else {
                currIndex = dna.indexOf(stopCodon, currIndex +1);
            }
        }
        return dna.length();
    }
    
    public String findGene(String dna){
        int atgCodon = dna.indexOf("ATG");
        
        if (atgCodon == -1) {
            return "NO ATG CODON FOUND";
        }
        int taaCodon = findStopCodon(dna, atgCodon, "TAA");
        int tagCodon = findStopCodon(dna, atgCodon, "TAG");
        int tgaCodon = findStopCodon(dna, atgCodon, "TGA");
        int tempCodon = Math.min(taaCodon, tagCodon);
        int dnaFin = Math.min(tempCodon, tgaCodon);
        if (dnaFin == dna.length()) {
            return "NO GENE FOUND";
        }
        return dna.substring(atgCodon, dnaFin+3);
    }
    
    public void testFindGene(){
        String dna= "AGDEGAASZZATAAAAA";
        System.out.println("The dna string is :" + dna);
        String gene = findGene(dna);
        System.out.println("Gene found is :" + gene);
        
        dna= "AAAAAAATGAAAAAAAAATAGAAAA";
        System.out.println("The dna string is :" + dna);
        gene = findGene(dna);
        System.out.println("Gene found is :" + gene);
        
        dna= "AAAAAAATGAAAAAAAAATAGTTATGAAAA";
        System.out.println("The dna string is :" + dna);
        gene = findGene(dna);
        System.out.println("Gene found is :" + gene);
        
        dna= "AAAAAAATGAAAAAAAAAAAAAAAA";
        System.out.println("The dna string is :" + dna);
        gene = findGene(dna);
        System.out.println("Gene found is :" + gene);
    }
    
    public int countGenes(String dna){
        int count = 0;
        
        int firstOccur = dna.indexOf(findGene(dna));
        String wholeGene = findGene(dna);
        if (firstOccur > -1) {
            count = count+1;
        System.out.println("count 1 =" + count + " firstOccur= " +firstOccur + " gene string is: " + wholeGene + " this is the lenght: " +wholeGene.length() );
        
        while (dna.indexOf(wholeGene, firstOccur) != -1 && firstOccur != -1) {
            count = count +1;
            firstOccur = dna.indexOf(wholeGene, firstOccur)+wholeGene.length();
            System.out.println(dna +"count 2 =" + count + " firstOccur= " +firstOccur + " this is the lenght: " +wholeGene.length() );
            System.out.println("gene: " +wholeGene);
        }
        count = count -1;
        }
        else {
            count=0;
        }
        return count;
    }
}
