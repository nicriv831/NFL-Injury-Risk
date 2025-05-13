# NFL Missed Game Risk

Challenge - Create a model that can usefully predict the liklihood a player misses four or more games in the upcoming NFL Season

Roadblocks -

1. There is not a single unique ID associated to all datasets, need to find a way to make my own unique ID for merges and data integrity
2. Names are repetitive (ie one play has JR listed some years and not other) need to standardize bdays
3. How to best aggregate weekly data for a single season projection
4. Bday/age data has many NaNs. I am operating on assumption that age and injury risk are correlated. Need to find a good way to handle missing values
   
    a. Some of the data are repeat player who have bdays listed in one season but not another, can use these values to fill in missing
   
    b. Some of the data is missing because some rows have differing names (i.e Michael in certain years and Mike in others)
   
    c. None of the data is missing at random, every player has a birthday
   
    d. There are many plauyers with a cut status in the rosters. Need to look at these players to see if they've had meaningful action in a game. Might be able to drop these players and eliminate missing bdays
