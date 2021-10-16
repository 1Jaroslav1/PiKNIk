import csv

def remakeCsv(fileCsv):
    
    with open('faktura.csv', 'w', newline='') as outcsv:

        fieldnames = ["Nazwa_produktu", "Cena_netto_bez_przecinka*", "Podatek_VAT", "Narzut", "Cena_sklepowa"]
        writer = csv.DictWriter(outcsv, fieldnames = fieldnames)
        writer.writeheader()

        with open('faktura_do_zad_Python_15.10_21.00.csv', newline='') as file_handle: 
            csv_reader = csv.DictReader(file_handle, fieldnames=['Płatki drożdżowe nieaktywne BIO g;1500;8;40'])
    
            for row in csv_reader:
                line = row['Płatki drożdżowe nieaktywne BIO g;1500;8;40']
            
                productName = line[0:line.find(';')]
                line = line[line.find(';')+1:]
                
                priceNetto = line[0:line.find(';')]
                line = line[line.find(';')+1:]

                priceVat = line[0:line.find(';')]
                line = line[line.find(';')+1:]

                overheads = line[0:line.find(';')]

                productPrice = (int(priceNetto) * 0.01)
                productPrice *= (1 + int(priceVat) *0.01)
                productPrice *= (1 + int(overheads) * 0.01)
                productPrice = round(productPrice, 2)

                writer.writerow({'Nazwa_produktu': productName,
                                 'Cena_netto_bez_przecinka*': priceNetto,
                                 'Podatek_VAT': priceVat, 'Narzut': overheads,
                                 'Cena_sklepowa': productPrice
                                })




remakeCsv('faktura_do_zad_Python_15.10_21.00.csv')