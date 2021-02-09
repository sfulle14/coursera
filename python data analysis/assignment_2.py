"""
By: Steven Fuller
"""

import csv


def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      A list of strings corresponding to the field names in 
      the given CSV file.
    """
    with open(filename, 'rt', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=separator, quotechar=quote)
        header = next(csvreader)
    return header
        

def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        lst = list(reader)
        return lst

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the 
      field values for that row.
    """
    with open(filename, mode='r') as csvfile:
        dict1 = {}
        reader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in reader:
            dict1[row[keyfield]] = row
        return dict1
    


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=separator,
                                quotechar=quote, quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        writer.writerows(table)