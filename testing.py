from morphin import imbuhan

awalan = imbuhan.perbaiki_awalan
perbaiki_kalimat = imbuhan.kalimat_awalan

kalimat = 'aku disuruh ibu untuk pergi mensapu halaman'

hasil = perbaiki_kalimat(kalimat)
print(hasil)