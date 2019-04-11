Problem Statement
```
I want to analyse the spreads between exchange rates and tried to write a program which calculates all combinations of possible exchange rates. It is in a way calculating the possibilities of an array, but that the numbers are exchange rates.

I have attached an Excel file with my previous code and a table which probably explains most of it. 

e.g 1: EUR to USD to...; 2. EUR to JPY to ... and so on. So, from EUR to USD until the maximum of combinations EUR to USD to JPY to GBP to CHF to CAD to AUD to HKD to EUR. Maximum combinations should be from 1 to 7 currencies e.g EUR - USD - EUR up to EUR - JPY - USD - GBP - CHF - CAD - AUD - HKD -
EUR (conversion to original currency not included). To make it comparable, the starting currency should always be the ending currency e.g USD to EUR to USD, GBP to EUR to USD to GBP and so on.

Every exchange rate should be converted to the starting exchange rate to see how big the loss was e.g EUR to USD to EUR = 0.9987 etc. 

I would like to have the output in the following way, if possible or you have better ideas:

EUR - USD - ..... = 0.9846
EUR to JPY - GBP... = 0.9975

Furthermore it would be nice to be able to filter the output so that it only shows for instance value between 0,95 - 0,99. An if statement should be fine to adjust it in the code if I have to.
```

Status
```
Completed. 
Flow:
1. For base pairs, generally calculate all permutations of combinations
2. You can edit the base pair inputs
3. For each chain in this set of permutations, calculate PNL in base currency
4. Add an if statement that outputs all PNL in 0.95 to 0.99
```

Instructions
```
0. Install Python 3.5
1. In the project director, open command prompt and type 'python main.py'
2. Your results will be in results.csv
3. Contact Hitesh if you have issues.
```