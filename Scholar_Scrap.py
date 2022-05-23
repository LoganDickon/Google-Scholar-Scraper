#-------#
# Tags: |
#-------#----------------------#
# Created By: Volker Strobel   |
# Improved By: Patrick Hofmann |
# Customized By: Logan Dickon  |
#------------------------------#

#------------------#
# Console Control: |
#------------------#--------------------------------------------#
# Ex1: Python File-path-to-Scholar_Scrap.py Start-Year End-Year |
# Ex2: Python C:\WebScrap\Scholar_Scrap.py 2000 2022            |
#---------------------------------------------------------------#

#----------------------#
# Program Description: |
#----------------------#-------------------------------------------------------------#
# This program uses a  bot to mask as a user-client. (EX. Google Chrome Web Browser) |
# The web bot does customized searches on Google Scholar and stores the results in a |
# comma-seperated values file. Then using Pandas & MatPlotLib the results are turned |
# into a Bar Graph and persented to the user to Save, Edit, & View.                  |
#------------------------------------------------------------------------------------#

#---------------------------#
# Pre-processor Directives: |
#---------------------------#
from bs4 import BeautifulSoup                                          
from urllib.request import Request, build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
from http.cookiejar import MozillaCookieJar
import re, time, sys, urllib
import matplotlib.pyplot as Plot
import pandas as pd

#---------------------#
# Method Description: |
#---------------------#---------------------------------------------------------------------------#
# This method creates a link to a csv file then writes each year and result together to the file. |
# Then, a pop-up window appears with a Bar Graph of the results.                                  |
#-------------------------------------------------------------------------------------------------#
def get_range(search_term, start_date, end_date):

    # Establish Connection to csv file:
    Conn = open("C:/WebScrap/CSV/" + CSV_Name + ".csv", 'w')

    # Print string to csv file:
    Conn.write("year,results\n") 
    
    # Console Log:
    print("year,results")

    # Empty X-axis & Y-axis Lists:
    x_axis = [] 
    y_axis = []

    #-------------------#
    # Loop Description: |
    #-------------------#--------------------------------------------------#
    # This loop, continues until it has parsed to the user-given End Year. |
    # while formating the data into comma-seperated values:                |
    #----------------------------------------------------------------------#
    for date in range(start_date, end_date + 1):

        # Get the number of search results:
        num_results, success = get_num_results(search_term, date, date)
        
        # Inform user to change their IP Address via VPN:
        if not (success == True):
            
            # Console Log:
            print("It seems that you made to many requests to Google Scholar. Change your location on your VPN to give you more searches.")
            
            # Break Loop:
            break

        # Format data into comma-seperated values:
        year_results = "{0},{1}".format(date, num_results)
        
        # Console Log:
        print(year_results)

        # Write data to csv file:
        Conn.write(year_results + '\n')
        
        # Append data to lists for use in the Bar Graph later:
        x_axis.append(int(date))
        y_axis.append(int(num_results))
        
        # Sleep timer to slow down HTTP requests:
        time.sleep(.8)

    # Close the Connection to csv file:
    Conn.close()
     
    # Create Blue Bar Graph:
    Plot.bar(x_axis, y_axis, color ='blue')

    # Name Bar Graph & Axis-Labels:
    Plot.xlabel("Years")
    Plot.ylabel("Number of Searches")
    Plot.title(search_term)
    
    # Bar Graph is displayed via a pop-up window:
    Plot.show()

#---------------------#
# Method Description: |
#---------------------#---------------------------------------------------------------------#
# This is a helper method. It uses the collected Search Term, Start Date, and an End Date.  |
# Then it sends an HTTP Request and returns it returns a data payload of data from the site |
#-------------------------------------------------------------------------------------------#
def get_num_results(search_term, start_date, end_date):

    # User-Agent Header To Trick Google Scholar:
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
    
    # Appending the parameters to the url:
    query_params = { 'q' : search_term, 'as_ylo' : start_date, 'as_yhi' : end_date}
    
    # Google Scholar url:
    url = "https://scholar.google.com/scholar?as_vis=1&hl=en&as_sdt=1,5&" + urllib.parse.urlencode(query_params)
    
    # Open HTTP client:
    opener = build_opener()

    # Send request to goto Google Scholar with the User-Agent header:
    request = Request(url = url, headers = {'User-Agent': user_agent})
    
    # Handle HTTP client:
    handler = opener.open(request)

    # Parse HTML and store it for later:
    html = handler.read() 

    # Create soup for parsing HTML and extracting the relevant information:
    soup = BeautifulSoup(html, 'html.parser')

    # find line About x results (y sec):
    div_results = soup.find("div", {"id": "gs_ab_md"}) 

    # Extract search results:
    if div_results != None:

        # Extract number of search results:
        res = re.findall(r'(\d+).?(\d+)?.?(\d+)?\s', div_results.text)
        
        # If a result was not found set to 0 & append result to a variable:
        if res == []:
            
            # Set result value to '0':
            num_results = '0'

            # True, because site successfully was scraped:
            success = True
        
        # If a result was found append result to a variable:
        else:
            
            # convert string to number:
            num_results = ''.join(res[0])
            
            # True, because site successfully was scraped:
            success = True

    # Return non-success & set default value for result:
    else:

        # False, because site was un-succesfully scraped:
        success = False
        
        # Set result value to 0:
        num_results = 0

    return num_results, success


# If program is ran directly from this file:
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("#--------------------------#")
        print("| Academic Word Relevance: |")
        print("#--------------------------#-------------------------#")
        print("| Usage: Python Scholar_Scrap.py Start_Date End_Date |")
        print("#----------------------------------------------------#")
        print("")
        
    search_term = input("Search: ")
    CSV_Name = input("Enter an Excel file name: ")
    start_date = int(sys.argv[1])
    end_date = int(sys.argv[2])
    html = get_range(search_term, start_date, end_date)