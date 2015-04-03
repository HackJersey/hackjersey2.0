# NJ Public Paychecker
##A project from the Hack Jersey 2.0 hackathon

New Jersey residents want to know how their tax money is being spent. Our project, [NJ Public Paychecker](www.thatguy.tv/clients/njsalarycompare/), will allow anyone to explore the salaries of local and state public employees and compare them to the median pay of residents in the immediate area.

People in NJ want to know where their tax dollars are going. Our web app tried to tackle this by looking at the salaries of government employees in different counties and comparing them to the salaries of the people who live there. We hoped that this could be a tool for both people and journalists to use as a starting point to examine public spending and public employee salaries.

Check out our [working prototype](http://www.thatguy.tv/clients/njsalarycompare/) and our [presentation](https://docs.google.com/presentation/d/1M48GIVej-KlTtPpIGaDOyiOVIHvNNgcpFc7SO5Jpa2c/edit?usp=sharing) for the judges.

###How we did it
Our primary source of data was [the csv of active employees in the state pension system](https://data.nj.gov/dataset/YourMoney-Active-Pension-Members/44xg-bswk) from the State of New Jersey's new-ish data site, [data.nj.gov](http://data.nj.gov).

Using [a Python script](https://github.com/tommeagher/njsalarycompare/blob/master/data/processing/public_medians.py), we calculated medians for state employees and for public employees, police, firefighters and teachers in each of the state's 21 counties.

We then compared those numbers in each county to median salaries for all occupations, from the Bureau of Labor Statistics' [Occupational Employment Statistics](http://www.bls.gov/oes/). Because those medians were for various metropolitan areas, we joined them with the counties that make up each area with another [Python script](https://github.com/tommeagher/njsalarycompare/blob/master/data/processing/median_salaries.py).

Finally, our web app made a request to Hack Jersey's [NJ Boundary Service API](http://boundary.hackjersey.com/#api) to geolocate each user and to grab the unique FIPS code for the data of the county to display.


###Contributors
* Clemence Hermano
* [Jonathan Kelly](http://www.twitter.com/jon723)
* Nicholas Knight
* Bill Lugo
* [Tom Meagher](http://www.github.com/tommeagher)



###Ideas for Further Development
In future iterations, we wanted to dice the public salary data to a more granular level, ideally to the municipal agency.  We'd also like to be able to integrate additional information on overall public spending.

Ideally, we could have the web app update itself, requiring little or no manual action to keep it updated on a quarterly basis for better scalability. This could be accomplished with a direct link to the dataset via its SODA API (found on data.nj.gov). The problem with that is the performance factor, especially if we're calculating the median, which the SODA API does not support (only average salaries is supported). The best solution would be to run a quarterly server chron job that pulls all the data into a quarterly-static JSON file to work off of. Then we could calculate medians based off of a pre-loaded data, freeing up other data pulls for just what's relevant.

Another factor to consider is what the data sources don't cover. Currently, our source data does not include: officials elected since 2007 (they're on a separate pension system), certain law enforcement officials, those on a judicial retirement system, part-time workers, and those that are on alternate benefit programs (which many universities have). In the future, perhaps other datasets could be imported to cover these data gaps.

Speaking of other datasets, we could add in new datasets that may be relevant to government salaries and tax dollar spending. Such supplemental information would make this app more useful to journalists and people researching it. Just for an example, datasets that track government wasteful spending by county in NJ. Or perhaps salary comparisons with other states or the national average.

See more details on our project on the [hackathon's hackpad](https://hackjersey2.hackpad.com/Public-Paychecker-wTi6GD1JgWi).
