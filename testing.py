from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# if bisa distem
kata = 'dijakarta'
out = stemmer.stem(kata)

fixed = kata[:2] + ' ' + kata[2:]

print(
    fixed
)