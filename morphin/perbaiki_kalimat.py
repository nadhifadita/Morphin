from morphin import perbaiki_imbuhan

perbaiki_awalan = perbaiki_imbuhan.perbaiki_awalan

def perbaiki(kalimat):
    print(f'kalimat salah: {kalimat}')
    pecah = kalimat.split()
    for i in range(len(pecah)):
        if pecah[i].startswith('me'):
            pecah[i] = perbaiki_awalan(pecah[i])
            print(f'perbaikan (list): {pecah}, kata: {pecah[i]}')
        # elif pecah[i] == 'nya':
        #     pecah[i-1]
    fixed = " ".join(pecah)
    return fixed