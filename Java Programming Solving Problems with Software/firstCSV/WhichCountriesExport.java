package firstCSV;


/**
 * Write a description of WhichCountriesExport here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */

import edu.duke.*;
import org.apache.commons.csv.*;
public class WhichCountriesExport {
    public void listExporters (CSVParser parser, String exportOfInterest){
        //for each row in the CSV file
        for (CSVRecord record : parser){          
            //look at the "Exports" column
            String export = record.get("Exports");
            //Check if it contains exportOFInterest
            if (export.contains(exportOfInterest)){
                //If so, write down the "Country"
                String country = record.get("Country");
                System.out.println(country);
                
            }
        }
    }
    public void whoExportsCoffee(){
        FileResource fr = new FileResource();
        CSVParser parser = fr.getCSVParser();
        listExporters(parser, "coffee");
    } 
    
    
    public String countryInfo(CSVParser parser, String country){
        String data = "";
        for (CSVRecord record : parser){
            String name = record.get("Country");
            if (name.contains(country)){    
                data = (country + ": " + record.get("Exports") + " " + record.get("Value (dollars)"));
                System.out.println(data);
                break;
            }
            else{
                data = "NOT FOUND";
            }
        }
        return data;
    }
    public String listExportersTwoProducts(CSVParser parser, String exportItem1, String exportItem2){
        String country = "";
        for (CSVRecord record : parser){          
            //look at the "Exports" column
            String export = record.get("Exports");
            //Check if it contains exportOFInterest
            if (export.contains(exportItem1) && export.contains(exportItem2)){
                //If so, write down the "Country"
                country = record.get("Country"); 
                System.out.println(country);
            }
        }
        return country;
    }
    public int numberOfExporters(CSVParser parser, String exportItem){
        int count = 0;
        for (CSVRecord record : parser){
            String export = record.get("Exports");
            
            if (export.contains(exportItem)){
                count+=1;
            }     
        }   
        return count;
    }
    public void bigExporters (CSVParser parser, String amount){
        for (CSVRecord record : parser){
            String money = record.get("Value (dollars)");
            
            if (money.length() > amount.length()){
                System.out.print(record.get("Country") + " ");
                System.out.println(money);
            }
        }
    }
    public void tester(){
        FileResource fr = new FileResource();
        CSVParser parser = fr.getCSVParser();
        countryInfo(parser, "Germany");
        parser = fr.getCSVParser();
        listExportersTwoProducts(parser, "gold", "diamonds");
        parser = fr.getCSVParser();
        numberOfExporters(parser, "gold");
        parser = fr.getCSVParser();
        bigExporters(parser, "$999,999,999,");
    }
    public void quiz(){
        FileResource fr = new FileResource();
        CSVParser parser = fr.getCSVParser();
        listExportersTwoProducts(parser, "fish", "nuts");
        parser = fr.getCSVParser();
        System.out.println(numberOfExporters(parser, "sugar"));
        parser = fr.getCSVParser();
        countryInfo(parser, "Nauru");
        parser = fr.getCSVParser();
        bigExporters(parser, "$999,999,999,999");
    }
}





