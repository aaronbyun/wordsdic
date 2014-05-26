from bs4 import BeautifulSoup
from word import Word
from textutils import replace

class DaumDicParser(object):
    def __init__(self):
        pass

    def getWord(self, soup):
        text = soup.find('span', attrs = {'class' : 'inner_tit'})
        w = text.get_text()
        return w

    def getMeanings(self, soup):
        meanings = []
        for p in soup.find_all('p', attrs = {'class' : 'txt_sense'}):
            #print p.contents
            for daum_w in p('daum:word'):
                daum_w.unwrap()

            for daum_i in p('daum:important'):
                daum_i.unwrap()

            meanings.append(replace(p.get_text(), '\n\r'))
        return meanings

    def getSynonyms(self, soup):
        synonyms = []
        syn = soup.find('div', attrs = {'class' : 'mean_synonym  mean_basic'})
        if syn != None:
            for div in syn.find_all('div', attrs = {'class' : 'desc'}):
                for a in div.find_all('a'):
                    synonyms.append(replace(a.get_text(), '\n\r'))
        return synonyms

    def getExpressions(self, soup):
        expressions = []
        idiom = soup.find('div', attrs = {'class' : 'section_idiom'})
        
        if idiom != None:
            list_idiom = idiom.find('div', attrs={'class' : 'list_idiom'})
            if list_idiom != None:
                for div_idiom in list_idiom.find_all('div'):
                    txt_div = div_idiom.find('div', attrs={'class' : 'txt'})
                    if txt_div != None:
                        a = txt_div.span.a
                        a.em.unwrap()
                        exp = replace(a.get_text(), '\"\n\r')
                        expressions.append(exp)

                    trans_div = div_idiom.find('div', attrs={'class' : 'trans'})
                    if trans_div != None:
                        expressions.append(replace(trans_div.span.get_text(), '\n\r'))
                    
        return expressions

    def getSetences(self, soup):
        sentences = []
        list_exam = soup.find('div', attrs = {'class' : 'list_exam'})

        if list_exam != None:
            for example in list_exam.find_all('div'):
                txt_div = example.find('div', attrs={'class' : 'txt'})
                if txt_div != None:
                    for daum_w in txt_div.span('daum:word'):
                        daum_w.unwrap()
                    sentences.append(replace(txt_div.span.get_text(), ['\"', '<br>', '</br>', '\n', '\r']))

                trans_div = example.find('div', attrs={'class' : 'trans'})
                if trans_div != None: 
                    for daum_w in trans_div.span('daum:word'):
                        daum_w.unwrap()
                    sentences.append(replace(trans_div.span.get_text(), '\"\n\r'))
                
        return sentences


    def parse(self, content):
        soup = BeautifulSoup(content)

        w           = self.getWord(soup)
        meanings    = self.getMeanings(soup)
        synonyms    = self.getSynonyms(soup)
        expressions = self.getExpressions(soup)
        sentences   = self.getSetences(soup)

        word = Word(w, meanings, synonyms, expressions, sentences)    
        return word



