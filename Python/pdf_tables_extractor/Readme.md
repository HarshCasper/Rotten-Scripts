# PDF tables extractor.

  - This script will convert the tables in the PDF file into CSV files.
  - For each tables in the PDF new CSV file will be generated.
  - Technology used: Tabula-py
 
 
## Setting up:

- Install the requirements

```sh
  $  pip install tabula-py 
```

## Running the script:

```sh
  $  # Specify the no. of pages to scan
  $ python3 pdf_to_csv.py <no. of pages>    
  $  # If you want all pages to scan
  $ python3 pdf_to_csv.py all 
```
