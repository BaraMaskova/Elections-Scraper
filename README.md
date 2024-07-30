# Elections Scraper
Třetí projekt pro Engeto Online Python Academy

## **Popis projektu**
Tento projekt slouží k extrakci výsledků parlamentních voleb v roce 2017 pro vybraný okres. Data jsou stahována z webové stránky a ukládána do CSV souboru. Pro podrobné prozkoumání dat volebních výsledků navštivte [tento odkaz](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

## **Instalace knihoven**
Knihovny používané v projektu jsou uvedeny v souboru `requirements.txt`. Pro jejich instalaci použijte následující příkaz:

```bash
pip install -r requirements.txt
```

## **Spuštění projektu**
Soubor `project_3.py` se spouští z příkazového řádku a vyžaduje dva argumenty:

python project_3.py <odkaz_uzemniho_celku> <vystupni_soubor>

•	`<odkaz_uzemniho_celku> `: URL adresa pro vybraný okres.

•	`<vystupni_soubor>`: Název CSV souboru, do kterého budou uložena výsledná data.

## **Ukázka použití**
### **Výsledky pro okres Jičín:**

•	**Odkaz:** `https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5202`

•	**Výstupní soubor:** `jicin_volby17.csv`

### **Příklad příkazu**
```bash
python project_3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5202" "jicin_volby17.csv" 
```

## **Příklady výstupu**

### **Část běhu programu:**

Tato část ukazuje, jak vypadá průběh programu během jeho běhu, např. URL, ze které se data stahují, a jaké operace program provádí.


STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5202

STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=8&xobec=553701&xvyber=5202

...

STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=8&xobec=573850&xvyber=5202

UKLÁDÁM DATA DO SOUBORU: jicin_volby17.csv

UKONČUJI: project_3.py

### **Částečný výstup:**

Tato sekce ukazuje příklad části výstupu CSV souboru, který obsahuje výsledky voleb pro daný okres.

Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
553701,Bačalky,133,98,97,"12,37 %","0,00 %","0,00 %","5,15 %","0,00 %","5,15 %","9,27 %","1,03 %","5,15 %","1,03 %","0,00 %","0,00 %","14,43 %","0,00 %","4,12 %","35,05 %","0,00 %","1,03 %","1,03 %","0,00 %","0,00 %","0,00 %","5,15 %","0,00 %"
572667,Bašnice,170,116,115,"6,95 %","0,00 %","0,00 %","4,34 %","0,00 %","6,95 %","6,08 %","0,00 %","0,86 %","0,00 %","0,00 %","0,00 %","3,47 %","0,00 %","1,73 %","51,30 %","0,00 %","0,00 %","6,08 %","1,73 %","0,00 %","0,00 %","10,43 %","0,00 %"
572675,Běchary,230,98,96,"4,16 %","0,00 %","0,00 %","10,41 %","0,00 %","3,12 %","3,12 %","0,00 %","3,12 %","1,04 %","0,00 %","0,00 %","7,29 %","0,00 %","0,00 %","43,75 %","0,00 %","0,00 %","6,25 %","0,00 %","0,00 %","0,00 %","17,70 %","0,00 %"
