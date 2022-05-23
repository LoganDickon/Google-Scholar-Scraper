# Historic word occurrence in academic papers 

## Summary -

This script extracts the historic word occurrence of a search term in
academic papers from "Google Scholar". It allows for spotting trends
in research and analyzing the relevance of a topic over time.

## Preparing for Usage

This section will show you steps to follow in order to download all needed program dependencies on a Windows Operating System

- Step 1: `Click on Windows Home search bar`
- Step 2: `Search: Command Prompt`
- Step 3: `Right Click & Select "Run as Administrator"`
- Step 4: `Click "Yes" on the pop-up menu`
- Now the Command Prompt should be open and ready for commands
- Step 5: `pip install bs4`
- Step 6: `pip install matplotlib`
- Step 7: `pip install pandas`
- Step 8: `Pip install requests`
- Step 9: `pip freeze` Now look for the following on in the list: `beautifulsoup4` , `matplotlib`, `pandas`, `requests` 

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
