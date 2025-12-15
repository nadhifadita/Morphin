from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def perbaiki_kata_depan(kata):
    fixed = kata
    stem = stemmer.stem(kata)
    
    if stem == kata: # gabisa di-stem
        fixed = kata[:2] + ' ' + kata[2:]
    else:
        fixed = kata[:2] + ' ' + stem
    
    return fixed

print(perbaiki_kata_depan('didalam'))