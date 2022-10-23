# Election_Analysis
Python
# Overview of Election Audit
What is the purpose of doing the Election Audit.
---

Seth and Tom have been asked by the election committee to conduct an election audit.  The election commission has requested some additional data to complete the audit:

* The voter turnout for each county
* The percentage of votes from each county out of the total count
* The county with the highest turnout
* The voter turnout for each county
* The percentage of votes from each county out of the total count
* The county with the highest turnout

## Analysis of Election Audit

* How many votes were cast in this congressional election?
* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
* Which county had the largest number of votes?
* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

### 2017
![Election _Analysis](/resources/Election_Results.png)


### 2018
![Screen.Shot.2018](/Resources_VBA/Screen.Shot.2018.png)

In the charts it shows that there were many tickers with positive returns in 2017 ( colored in green).  In 2018 most tickers had negative returns ( colored in red).

### Execution times

Also shown in the charts above are the execution times for each years calculations.  The times were calculated by starting the timer at the beginning of the code, then stopped as the code ended.

## Refactoring the code

### 2017
![Screen.Shot.2017.Refactored](/Resources_VBA/Screen.Shot.2017.Refactored.png)


 ### 2018

![Screen.Shot.2018.Refactored](/Resources_VBA/Screen.Shot.2018.Refactored.png)

The refactoring of the code used arrays to capture the data as it ran through each line of the data, rather than running through all rows to capture data data for each ticker.  the Capturing of data this way saved almost half the time as shown in the message of the running time.  The underlying calculations after refactoring is seen to be the same.

## Summary

Refactoring has advantages and disadvantages
### Advantages

    If the purpose of the code is time sensitive, refactoring is necessary to make the time it takes to execute the code as quick as possible
    
### Disadvantages

    Refactoring can be quite time consuming. Writing code without a time constraint can be done more quickly, without a lot of reworking of the code to make small changes in the time. 
    
Refactoring of the VBA code in this exercise has advantages and disadvantages

### Advantages

    As stated above, the data is stored for each ticker and then the analysis can be done for each ticker at the same time.
    
### Disadvantages

    The amount of space this takes up, while executing, can be extensive.  Here we only used 12 tickers, but if someone wanted to run this for 100s, they would need a lot of short term storage space.

