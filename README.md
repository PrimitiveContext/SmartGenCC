# SmartGenCCs
# Overview
# The CCs_from_BINs.py script is designed to generate valid credit card numbers based on provided BIN (Bank Identification Number) values. The script can process individual BINs or a list of BINs from a file and outputs the generated card numbers to CSV files. It ensures the generated numbers are valid by using the Luhn algorithm.

# --Features--
#	Generates valid credit card numbers using the Luhn algorithm.
#	Processes both single BIN values and lists of BIN values from text or CSV files.
#	Supports batch processing, with the ability to specify the number of card numbers per CSV file.
#	Displays progress using a progress bar.
#	Handles both 15-digit and 16-digit BIN values.

# --Usage--
To run the script, use the following command format:< br / >
  \npython3 CCs_from_BINs.py <bin_value_or_file> [--batch <batch_size>]< br / >
  <bin_value_or_file> (required)< br / >
    The BIN value or the path to a file containing BIN values. The BIN value should contain asterisks (*) representing the variable digits.
#			Example: '372395*********' (American Express: 15 digits total)
#			Example: '423456**********' (other cards: 16 digits total)
#			Example: 'bin_values.txt' (text file with multiple wildcard BINs)

#	--batch, -b: (optional)
#		Maximum number of credit card numbers per CSV file (default is 100,000).

# --Examples--
#	python CCs_from_BINs.py 423456**********		# Generate credit card numbers for a single BIN value with the default batch size
#	python CCs_from_BINs.py bin_values.txt --batch 50000	# Generate credit card numbers for multiple BIN values from a file with a specified batch size

# --BIN_cc_collision_odds.csv--
#	Contains data on credit card BINs (Bank Identification Numbers) and their associated odds of credit card number collisions.
#		cc_brand: The brand of the card (e.g., American Express, Visa, MasterCard).
#		cc_name: The name of the credit card or the issuing bank (e.g., American Express American Express Blue Cash Everyday).
#		cc_odds_of_collision: The calculated odds of a credit card number collision for the BIN (e.g., 0.040).
#		total_luhn_cc_numbers: The total number of potential credit card numbers conforming to the Luhn algorithm for the BIN (e.g., 100000000).
#		cc_est_global_active: An estimate of the active cards associated with the BIN (e.g., 4000000).
#		bin_list: A list of BINs represented with masked digits (e.g., ['372395*********']).
