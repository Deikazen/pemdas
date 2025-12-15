data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}


for k, v in data_panen.items():
    print(f'lokasi : {k}')
    print(f'Nama Lokasi : {v['nama_lokasi']} ')
    print(f'hasil panen :  {v['hasil_panen']}')
    print('===========================')
    print('')

jagung_lok_2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f'jagung lokasi 2 : {jagung_lok_2} ')
print('===========================')
print('')


nama_lok_3 = data_panen['lokasi3']['nama_lokasi']
print(f' nama lokasi 3 : {nama_lok_3}')
print('')


for key, val in data_panen.items():
    print(f"lokasi ke : {key} ")
    jumlah_padi = val['hasil_panen']['padi']
    jumlah_kedelai = val['hasil_panen']['kedelai']
    jumlah_jagung = val['hasil_panen']['jagung']

    if jumlah_padi > 1300 or jumlah_jagung > 800:
        print(f'{key} memerlukan perhatina khusus! ')
        print('===========================')

    else:
        print(f'{key} dalam kondisi baik. ')
        print('===========================')

print('===========================')
print('')
