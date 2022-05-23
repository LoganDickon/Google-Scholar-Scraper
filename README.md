# Google Scholar Scraper
This repository will contain an updated version of "Volker Strobel's - Google Scholar" scraper

# Historic word occurrence in academic papers

## Summary

This script extracts the historic word occurrence of a search term in
academic papers from "Google Scholar". It allows for spotting trends
in research and analyzing the relevance of a topic over time.

## Usage

`Activate VPN (for best results)`
`Python Scholar_Scraper.py <Start Date> <End Date>`
`Search: <Keyword>`
`Enter an Excel file name: <Keyword2>`

This command lists the number of publications for every year using
this keyword. The script just searches for articles and excludes
patents and citations.

## Example

- Activate VPN (for best results)
- Search term: `CO2 Scrubbing`
- Desired time span: `2000` to `2022`
- Command Prompt: `Python Scholar_Scraper.py <Start Date> <End Date>`
- input: `Search: <Keyword>`
- input: `Enter an Excel file name: <Keyword2>`
- Output: `Keyword2.csv`, with the following contents saved to a directory of your choosing:
- Output:

  year,results
  2000,842
  2001,939
  2002,1010
  2003,1020
  2004,1210
  2005,1370
  2006,1370
  2007,1470
  2008,1770
  2009,2220
  2010,2000
  2011,2780
  2012,3130
  2013,3650
  2014,3640
  2015,3780
  2016,4000
  2017,4350
  2018,4280
  2019,4480
  2020,4820
  2021,4740
  2022,2120

![GitHub Logo](\Files\Graph.png)

## Credits
Created by Volker Strobel - volker.strobel87@gmail.com

If you use this code in academic papers, please cite this repository via Zenodo (http://doi.org/10.5281/zenodo.1218409):

Volker Strobel. (2018, April 14). Pold87/academic-keyword-occurrence: First release (Version v1.0.0). Zenodo. http://doi.org/10.5281/zenodo.1218409
