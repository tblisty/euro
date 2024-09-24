import requests
from icecream import ic
# import sys
import datetime

def kurs_euro():
    # URL = "https://nbp.pl/statystyka-i-sprawozdawczosc/kursy/tabela-a/"
    # URL = "https://api.nbp.pl/api/exchangerates/tables/A/"
    # https://api.nbp.pl/api/exchangerates/rates/a/eur/2024-09-23
    euro_url = "https://api.nbp.pl/api/exchangerates/rates/a/eur/"
    
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    str_yesterday = yesterday.strftime("%Y-%m-%d")
    url = euro_url + str_yesterday
    
    resp = requests.get(url)
    # if not resp.ok:
    #     print("Błąd pobierania danych")
    #     sys.exit(1)
    
    tableA = resp.json()
    kurs_euro_ = tableA["rates"][0]['mid']
    numer_tabeli = tableA["rates"][0]['no']
    
    formula_w = [   ["1 EUR =", kurs_euro_, "PLN wg. Tabela nr", numer_tabeli, "z dnia", str_yesterday],
                    ["Kontoverbindung:  Firma Fistal     Kontonummer: 0020044208   Bankleitzahl: 17054040"],
                    ["IBAN DE32 1705 4040 0020 0442 08 Sparkasse Märkisch Oderland\n"],
                    ["Zgodnie z Art 42 ust.1 towar opodatkowuje Nabywca na terytorium państwa członkowskiego w którym posiada siedzibę"],
                    ["Odwrotne obciążenie."]
                ]
    
    for item in formula_w:
        for subitem in item:
            print(subitem, end=' ')
        print()
    
    # Wzór formuły:
    
    # 1 EUR = 4,2986 PLN wg. Tabela nr 178/A/NBP/2024 z dnia 2024-09-12
    # Kontoverbindung:  Firma Fistal     Kontonummer: 0020044208   Bankleitzahl: 17054040   
    # IBAN DE32 1705 4040 0020 0442 08 Sparkasse Märkisch Oderland 
    #
    # Zgodnie z Art 42 ust.1 towar opodatkowuje Nabywca na terytorium państwa członkowskiego w którym posiada siedzibę
    # Odwrotne obciążenie.
    

def main():
    kurs_euro()

if __name__ == "__main__":
    main()