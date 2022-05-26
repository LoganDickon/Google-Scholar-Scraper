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
- Step 5: `Now the Command Prompt should be open and ready for commands`
- On `steps 5 - 9` if you receive a `"pip: command not found"` message then jump to `Pip Help` section
- Step 6: `Type: pip install bs4`
- Step 7: `Type: pip install matplotlib`
- Step 8: `Type: pip install pandas`
- Step 9: `Type: pip install requests`
- Step 10: `Type: pip freeze`
- Step 11: Now look for the following inside the List: `beautifulsoup4` , `matplotlib`, `pandas`, `requests`
- Step 12: If the `libraries` were found in your List, then you have successfully installed all needed files to run the program w/o error
- Step 13: If the `libraries` were not found in the List, then check to see if you are in `adminstrator mode`, then start back a `step 6`

## Pip Help -

Did you receive the "pip: command not found" error?

If yes, 
- Step 1: `Make sure pip is lowercase and try again`
- Step 2: `On Windows Home right click on the Start button`
- Step 3: `Click: Apps and Features`
- Step 4: `Scroll until you find your Python Installation (Ex. Python 3.10.4 (64-bit)`
- Step 5: `Click 3 dots on right side of Python (not the Python Launcher)`
- Step 6: `Click: Modify`
- Step 7: `A pop-up installer for Python should open`
- Step 8: `Click: Modify`
- Step 9: `Check Box: "pip"`
- Step 10: `Click: Next`
- Step 11: `Check Box: "Add Python to enviroment variables"`
- Step 12: `Click: Install`
- Step 13: `Click: Close`
- Step 14: `pip Should be properly installed now. Try & redownload the dependencies`

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
