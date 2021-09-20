
import requests
import bs4


'''result = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")


soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup.select('.infobox-image'))


computer = soup.select('.infobox-image')[0]
print(computer)
#print(computer['src'])
image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg")

f = open('my_imagetttt.jpg', 'wb')
f.write(image_link.content)'''

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

two_star_titles = []

for n in range(1, 51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")

    for book in books:

        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)


print(two_star_titles)