from bs4 import BeautifulSoup
from word import Word

class DaumDicParser(object):
    def __init__(self):
        pass

    def parse(self, content):
        soup = BeautifulSoup(content)

        # get word
        print 'word'
        text = soup.find('span', attrs = {'class' : 'inner_tit'})
        w = text.get_text()
        print w

        # get meaning
        print 'meanings'
        meanings = []
        for p in soup.find_all('p', attrs = {'class' : 'txt_sense'}):
            #print p.contents
            for daum_w in p('daum:word'):
                daum_w.unwrap()

            for daum_i in p('daum:important'):
                daum_i.unwrap()

            print p.get_text()
            meanings.append(p.get_text())

        print meanings

        # get synonyms
        print 'synonyms'
        synonyms = []
        syn = soup.find('div', attrs = {'class' : 'mean_synonym  mean_basic'})
        if syn != None:
            div = syn.find('div', attrs = {'class' : 'desc'})
            for a in div.find_all('a'):
                print a.get_text()
                synonyms.append(a.get_text())

        print synonyms

        word = Word(w, meanings, synonyms, '', '')    
        return word



