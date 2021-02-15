"""
Project for Week 2 of "Python Data Visualization".
Read World Bank GDP data and create some basic XY plots.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import pygal


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

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


def build_plot_values(gdpinfo, gdpdata):
    """
    Inputs:
      gdpinfo - GDP data information dictionary
      gdpdata - A single country's GDP stored in a dictionary whose
                keys are strings indicating a year and whose values
                are strings indicating the country's corresponding GDP
                for that year.

    Output: 
      Returns a list of tuples of the form (year, GDP) for the years
      between "min_year" and "max_year", inclusive, from gdpinfo that
      exist in gdpdata.  The year will be an integer and the GDP will
      be a float.
    """
    all_present_dic = dict()
    for year, gdp_val in gdpdata.items():
        if gdp_val != '':
            all_present_dic[year] = gdp_val
    
    results = []
    for year, gdp in zip(all_present_dic.keys(), all_present_dic.values()):
        try:
            result = int(year), float(gdp)
            results.append(result)
        except ValueError:
            continue
    
    results.sort(key=lambda pair: pair[0])

    checked_results = []
    for idx in results:
        if gdpinfo['min_year'] <= idx[0] <= gdpinfo['max_year']:
            checked_results.append(idx)

    return checked_results



def build_plot_dict(gdpinfo, country_list):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names

    Output:
      Returns a dictionary whose keys are the country names in
      country_list and whose values are lists of XY plot values 
      computed from the CSV file described by gdpinfo.

      Countries from country_list that do not appear in the
      CSV file should still be in the output dictionary, but
      with an empty XY plot value list.
    """
    final = {}
    for country in country_list:
        data = []
        country_info = read_csv_as_nested_dict(gdpinfo.get('gdpfile'), gdpinfo.get('country_name'),
                                               gdpinfo.get('separator'), gdpinfo.get('quote'))
        for year in range(gdpinfo.get('min_year'), gdpinfo.get('max_year')+1):
            try:
                print(year, country_info.get(country).get(str(year)))
                data.append((int(year), float(country_info.get(country).get(str(year)))))
            except ValueError:
                continue
            except AttributeError:
                continue
        final[country] = data
    
    return final


def render_xy_plot(gdpinfo, country_list, plot_file):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names
      plot_file    - String that is the output plot file name

    Output:
      Returns None.

    Action:
      Creates an SVG image of an XY plot for the GDP data
      specified by gdpinfo for the countries in country_list.
      The image will be stored in a file named by plot_file.
    """
    gdp_plot = pygal.XY()
    gdp_plot.title = 'Plot of GDP for select countries' + str(gdpinfo.get("min_year"))\
                     + ' to ' + str(gdpinfo.get("max_year"))
    gdp_plot.y_title = 'GDP in US dollars'

    for country in country_list:
        gdp_plot.add(country, build_plot_dict(gdpinfo, country_list).get(country))

    gdp_plot.render_to_file(plot_file)


def test_render_xy_plot():
    """
    Code to exercise render_xy_plot and generate plots from
    actual GDP data.
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    render_xy_plot(gdpinfo, [], "isp_gdp_xy_none.svg")
    render_xy_plot(gdpinfo, ["China"], "isp_gdp_xy_china.svg")
    render_xy_plot(gdpinfo, ["United Kingdom", "United States"],
                   "isp_gdp_xy_uk+usa.svg")


# Make sure the following call to test_render_xy_plot is commented out
# when submitting to OwlTest/CourseraTest.

# test_render_xy_plot()