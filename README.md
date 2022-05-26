# Historic Word Occurrence in Academic Papers 

## Summary -

This script extracts the historic word occurrence of a search term in
academic papers from "Google Scholar". It allows for spotting trends
in research and analyzing the relevance of a topic over time.

## Preparing for Usage -

This section will show you steps to follow in order to download all needed program dependencies on a Windows Operating System

- Step 1: `Click on Windows Home search bar`
- Step 2: `Search: Command Prompt`
- Step 3: `Right Click & Select "Run as Administrator"`
- Step 4: `Click "Yes" on the pop-up menu`
- Now the Command Prompt should be open and ready for commands
- On `steps 5 - 8` if you receive a `"pip command not found"` message then jump to `Pip Help` section
- Step 5: `Type: pip install bs4`
- Step 6: `Type: pip install matplotlib`
- Step 7: `Type: pip install pandas`
- Step 8: `Type: Pip install requests`
- Step 9: `Type: pip freeze` Now look for the following inside the List: `beautifulsoup4` , `matplotlib`, `pandas`, `requests`
- If the dependencies were found in your List, then you have successfully installed all needed files to run the program w/o error
- Step 10: If the 4 were not found in the List, then check to see if you are in adminstrator mode, then try & redownload

## Pip Help -

Did you receive the 'pip command not found' error?

If yes, 
- Step 1: `On Windows Home right click on the Start button`
- Step 2: `Click: Apps and Features`
- Step 3: `Scroll until you find your Python Installation (Ex. Python 3.10.4 (64-bit)`
- Step 4: `Click 3 dots on right side of Python (not the Python Launcher)`
- Step 5: `Click: Modify`
- A pop-up installer for Python should open
- Step 6: `Click: Modify`
- Step 7: `Check Box: "pip"`
- Step 8: `Click: Next`
- Step 9: `Check Box: "Add Python to enviroment variables"`
- Step 10: `Click: Install`
- Step 11: `Click: Close`
- `pip` Should be properly installed now. Try & redownload the dependencies

## Example of Usage -

- Activate VPN (for best results)
- Search term: `CO2 Scrubbing`
- Desired time span: `2000` to `2022`
- Command Prompt: `Python Scholar_Scraper.py <Start Date> <End Date>`
- input: `Search: <Keyword>`
- input: `Enter an Excel file name: <Keyword2>`
- Output: `Keyword2.csv`
- Output: `Table Below`

![Output](/Files/CO2_Scrubbing.png)

## Output Graph -

![CO2 Scrubbing](/Files/Graph.png)

## Credits - 
Created By: Volker Strobel (owner of original GitHub) - volker.strobel87@gmail.com

Customized By: Logan Dickon (owner of this GitHub) - lad@atorlabs.com

Original Github Repository: https://github.com/Pold87/academic-keyword-occurrence

Volker Strobel. (2018, April 14). Pold87/academic-keyword-occurrence: First release (Version v1.0.0). Zenodo. http://doi.org/10.5281/zenodo.1218409
