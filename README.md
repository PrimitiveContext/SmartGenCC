
# SmartGenCCs.py

## Overview
The `SmartGenCCs.py` script is designed to generate valid (Luhn-compliant) credit card numbers based on known BIN (Bank Identification Number) values. The script can process individual BINs or a list of BINs from a file and outputs the generated card numbers to CSV files.

## Features
- Generates valid credit card numbers using the Luhn algorithm.
- Processes both single BIN values and lists of BIN values from text or CSV files.
- Supports batch processing, with the ability to specify the number of card numbers per CSV file.
- Displays progress using a progress bar.
- Handles both 15-digit and 16-digit BIN values.

## Usage
To run the script, use the following command format:
    
    python3 CCs_from_BINs.py <bin_value_or_file> [--batch <batch_size>]

- `<bin_value_or_file>` (required):
  - The BIN value or the path to a file containing BIN values. The BIN value should contain asterisks (*) representing the variable digits.
  - Example: `372395*********` (American Express: 15 digits total)
  - Example: `423456**********` (other cards: 16 digits total)
  - Example: `bin_values.txt` (text file with multiple wildcard BINs)
    
- `--batch`, `-b`: (optional):
  - Maximum number of credit card numbers per CSV file (default is 100,000).

## Examples
- Generate credit card numbers for a single BIN value with the default batch size:
  ```
  python CCs_from_BINs.py 423456**********
  ```

- Generate credit card numbers for multiple BIN values from a file with a specified batch size:
  ```
  python CCs_from_BINs.py bin_values.txt --batch 50000
  ```

## Resources

The `BinStats.csv` contains data on BINs of specific cards and estimated odds of a card number collision.
```
| cc_brand        | cc_name                                                        | odds_of_collision | luhn_card_space | global_est | bin_list                                 |
|-----------------|----------------------------------------------------------------|-------------------|-----------------|------------|------------------------------------------|
| American Express| American Express American Express Blue Cash Express Card       | 0.04              | 100000000       | 4000000    | ['372395*********']                      |
| Visa            | VISA Bank of America, National Association Classic, Debit, Visa| 0.025             | 1000000000      | 25000000   | ['449533**********']                     |
| MasterCard      | Mastercard Wells Fargo                                         | 0.01              | 2000000000      | 20000000   | ['514019**********', '514020**********'] |
```

The `RegexWildcards.json` contains bin wildcard lists and cc regex for specific subsets of Discover, AMEX, VISA, and Master Card.
```
{      
        "type": "VISA",<br/>
        "cc_regex": "^4[0-9]{12}(?:[0-9]{3})?$|^4[0-9]{12}(?:[0-9]{3})?$",
        "cc_length": 16,
        "code_regex": "^\\d{3}$",
        "date_format": "MM/YY",
        "card_space": "10,000,000,000",
        "wildcards": 10000,
        "wildcard_list": [
                "4012040120******",
                "4012040121******",
                "4012040122******",
                "4012040123******"]
}
```
