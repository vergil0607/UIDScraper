# VAT Number verification:

## What is required

*  An Excel-file or .csv file containing the VAT-numbers to be validated

## What is the source of validation

* To validate the VAT-numbers, the website https://ec.europa.eu/taxation_customs/vies/ is used
* The website allows the validation of VAT-numbers within the European Union, including Northern Ireland

## Possible settings

* The name of the input file
* The name of the output file
* The limit of numbers to be checked
* Whether a browser is used, or the task is performed headlessly


## Download and install

`git clone https://github.com/vergil0607/UIDScraper.git` <br>
`cd UIDScraper` <br>
`python -m venv venv` <br>
`venv\Scripts\activate` <br>
`pip install -r requirements.txt` <br>
`python UIDBOT\ValidateUIDs.py`
