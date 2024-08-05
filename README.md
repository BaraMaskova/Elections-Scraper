# Elections Scraper
Third project for Engeto Online Python Academy

## **Project Description**
This project extracts the 2017 parliamentary election results for a selected district. Data is downloaded from the website and saved into a CSV file. For detailed exploration of election results data, visit [this link](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

## **Library Installation**
The libraries used in this project are listed in the `requirements.txt` file. To install them, use the following command:

```bash
pip install -r requirements.txt
```

## **Running the Project**
The project_3.py file is run from the command line and requires two arguments:

python project_3.py <district_url> <output_file>

•	`<district_url>`: The URL for the selected district.

•	`<output_file>`: The name of the CSV file where the result data will be saved.

## **Usage Example**
### **Results for the Jičín District:**

•	**URL:** `https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5202`

•	**Output File:** `jicin_volby17.csv`

### **Example Command**
```bash
python project_3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5202" "jicin_volby17.csv" 
```

## **Output Examples**

### **Program Run Example:**

This section shows what the program run looks like, such as the URL from which data is being downloaded and what operations the program performs.


Fetching data from URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5202

Fetching data from URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=8&xobec=553701&xvyber=5202

...

Fetching data from URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=8&xobec=573850&xvyber=5202

Saving data to file: jicin_volby17.csv

Process completed successfully: project_3.py

### **Partial Output:**

This section shows an example of a portion of the CSV file output, containing the election results for the selected district.

Municipality Code,Municipality Name,Registered Voters,Issued Envelopes,Valid Votes,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
553701,Bačalky,133,98,97,"12,37 %","0,00 %","0,00 %","5,15 %","0,00 %","5,15 %","9,27 %","1,03 %","5,15 %","1,03 %","0,00 %","0,00 %","14,43 %","0,00 %","4,12 %","35,05 %","0,00 %","1,03 %","1,03 %","0,00 %","0,00 %","0,00 %","5,15 %","0,00 %"
572667,Bašnice,170,116,115,"6,95 %","0,00 %","0,00 %","4,34 %","0,00 %","6,95 %","6,08 %","0,00 %","0,86 %","0,00 %","0,00 %","0,00 %","3,47 %","0,00 %","1,73 %","51,30 %","0,00 %","0,00 %","6,08 %","1,73 %","0,00 %","0,00 %","10,43 %","0,00 %"
572675,Běchary,230,98,96,"4,16 %","0,00 %","0,00 %","10,41 %","0,00 %","3,12 %","3,12 %","0,00 %","3,12 %","1,04 %","0,00 %","0,00 %","7,29 %","0,00 %","0,00 %","43,75 %","0,00 %","0,00 %","6,25 %","0,00 %","0,00 %","0,00 %","17,70 %","0,00 %"