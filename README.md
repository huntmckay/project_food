# Plate Scraper is a learning project

meal planning, shopping, cooking are so difficult. I want it to be easier for 
my family.

# Plan so far

## Recipe web scraper
From a few common websites I want to be able to plug in a URL and convert that 
data a more useful format then css and html. Perhaps Json or Yaml. It will also
require the data conversion to common decimal/float formats. '1/2 an onion' 
should be converted to '.5 onion' or even more structured: {'onion': 0.5}

The interface I am planning will allow a user to submit a list of URL's from
supported websites. Probably on the commandline, perhaps a web front end in the
future. 

<!--- I would like this to be a mermaid chart --->
exmaple:
$ Enter Url: < URL/recipe/scrambled-eggs.html >
1. validate input is url
2. validate the base URL is a supported website
3. scrape the page
4. distill important information for the recipe
5. convert datatypes to useful and mathematical values 
6. store data in a flat file

## Ingredients combined
After all shopping lists have been converted to flat files, combine the values.
If recipe1 has {'eggs': 1} and recipe2 has {'eggs': 6} then the final state
should display {'eggs': 7}. The data must be perfect from the first steps to
make this step seemless. The output should be an organized list of how much to
order / or purchase. I want to provide a few different outputs, because people 
tend to shop differently. I go asile to asile, my wife tends to shop by
department. We also go to different stores in person, or we order from a 
delivery app. It could also be broken down into the days of the meals, so 
user could print off M,T,W and get that exact amount. Ideally this shopping 
list will be appended by multiple URL's adding to it. i.e. eggs are a common 
ingredient, over the course of 3 days days, breakfast, lunch and dinner, my 
family might use 18 eggs. If We decide to change a recipe that calls for more 
eggs, the shopping list should reflect that.  

## Front end
In the future I would like this to have some kind of organization. Maybe a 
database back end with a website front end. That sounds pretty full-stack dev.
I think this part of the plan will have to wait because I am not sure if it 
needs to exist at all. The first two above will solve my problems in a real way
and I think instead of a pretty front end, just an emailed prettified list
would satisfy. I would also rather spend my time expanding support for more 
recipe websites, rather then support a website and db that maybe 3 people would
use.
