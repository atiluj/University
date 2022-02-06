import html.parser
import urllib.request
import re

class WordSearch(html.parser.HTMLParser):
    def __init__(self, word):
        html.parser.HTMLParser.__init__(self)
        self.regEx = re.compile(r'(\b' + word + r'\b|[A-Z][^\.]*?\b' + word + r'\b).*?[\.!?](?:\s|$)')
        self.sentencesContainingWord = []

    def handle_data(self, data):
        self.sentencesContainingWord.extend([sentence.group() for sentence in self.regEx.finditer(data)])

class Crawler(html.parser.HTMLParser):
    def __init__(self):
        html.parser.HTMLParser.__init__(self)
        self.refSet = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a': # oznaczenie linków w html
            for (atribute, val) in attrs:
                if atribute == 'href': # oznaczenie linku
                    if re.match(r'https?://([a-zA-Z]+\.)*[a-zA-Z]+', val):
                        self.refSet.add(val)

def searchForWord(wordToSearch):
    def aux(htmlPage):
        parser = WordSearch(wordToSearch)
        parser.feed(htmlPage)
        return parser.sentencesContainingWord
    return aux

def crawl(start_page, distance, action):
    visited = set()
    toVisit = [(start_page, 0)] #(strona, jak głeboko jesteśmy)
    parser = Crawler()

    while len(toVisit) != 0:
        if toVisit[0][1] > distance: #żeby nie wejść za głębko
            break
        try:
            req = urllib.request.urlopen(toVisit[0][0])
        except EnvironmentError as e:
            print(toVisit[0][0], e)
        else:
            htmlPage = req.read().decode('utf-8')
            parser.feed(htmlPage) #wszystkie odwołania do znaków zostaną przekonwertowane na ich odpowiedniki w Unicode
            yield (toVisit[0][0], action(htmlPage))
        finally:
            visited.add(toVisit[0][0]) #dodanie właśnie odwiedzonej strony do zbioru stron odwiedzonych
            toVisit.extend((url, toVisit[0][1]+1) for url in parser.refSet - visited) # dodanie nowych stron do listy stron do odwiedzenia
                                                                                      # pętla zawiera warunek, który uniknie dodania
                                                                                      # strony, która została już odwiedzona
            toVisit = toVisit[1:] #usunięcie odwiedzonej własnie strony z listy stron do odwiedzenia

def printf(result, max):
    i = 1
    for res in result:
        if i <= max:
            print(i, "\n", res,"\n")
            i += 1
        else: break

printf(crawl('https://www.python.org/', 1, searchForWord('Python')), 12)
# printf(crawl('https://www.python.org/', 1, searchForWord('Python')), 25)
