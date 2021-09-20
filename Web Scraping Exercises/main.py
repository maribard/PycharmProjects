import requests
import bs4
import lxml


base_url = 'https://quotes.toscrape.com/page/{}/'
i = 0
list_authors = []
while True:
    i += 1
    res = requests.get( base_url.format(i))

    soup = bs4.BeautifulSoup( res.text, 'lxml' )

    pages = soup.select( ".col-md-8" )
    if "No quotes found" in str( pages ):
        break

    authors = soup.select( "small" )
    for n in range( 0, len( authors ) ):
        author = authors[n].getText()
        if author not in list_authors:
            list_authors.append( author )




print(list_authors)






list_quotes = []
quotes = soup.select(".text")
for n in range(0, len(quotes)):
    quote = quotes[n].getText()
    if quote not in  list_quotes:
        list_quotes.append(quote)

#print(list_quotes)



list_tags = []
tags = soup.select(".tag-item")
for n in range(0, len(tags)):
    tag = tags[n].text
    new_tag = tag.replace("\n", "")
    if new_tag not in  list_tags:
        list_tags.append(new_tag)

#tags = soup.select(".tag-item")[0].text
#print(list_tags)

