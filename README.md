# Python exam project - Bornholmer gruppen

### Vi forsøger os med at bruge machine learning algoritmer til at klassificere spil i forskellige genrer baseret på deres beskrivelse. Vi scraper data og forbereder fra steam og bruger det til at træne vores modeller. Vi analysere data fra steam og laver analyser på baggrund af det. 

## list over teknologier vi bruger
- Pandas
- Numpy
- Matplotlib
- Mtplotlib
- beautifulsoup4
- Tensorflow
- Keras
- Kaggle
- Scikit-learn
- nltk
- scipy

## Installation
#### Download kaggles dataset og pak det ud i roden af projektet, og navngiv det til `steam_games_dataset_kaggle.csv` 
#### Kør derefter jupyter notebooks i rækkefølge 3-7, 1 og 2 er mest af bare til at kigge på.
#### have fun 🏴‍☠️

## User guid 
#### jupyter notebooks 3-7 skal køres i rækkefølge, ellers kan de resterende notebooks beskues som ønskes.
#### notebook: Exam.ipynb kan køres fra starten af, du skal blot give den data som den spørger efter.


## Notebook status
### Notebook 1-2 
#### Webscraping

### Notebook 3
#### Data processing

### Notebook 4-6
#### Vi prøver flere machine learning modeller for at opnå bedre resultat

### Notebook 4-4a
#### Multi output model med vores scraped data (genrerne behandlet i gruppe)

### Notebook 4b
#### Multi output model med hentet kaggle dataset (genrerne behandlet i gruppe)

### Notebook 5
#### Multi output model med hentet kaggle dataset (genrerne behandlet hver for sig)

### Notebook 6
#### Neural machine learning model med hentet kaggle dataset (genrerne behandlet hver for sig)

### Notebook 7
#### Det samme som 6'eren, blev lavet imens vi havde baks med at få 6'eren til at virke.

### Notebook: Exam.ipynb
#### Her kan man ud fra et steamID finde brugerns posetive reviews og printer navn, genre og beskrivelse ud fra alle de forskellige spil. Derud over kan man også få anbefalet spil, ud fra et andet spil.

## liste af udfordringer
#### Vores største udfordringer har været at få det til at virke på alles maskiner, har løbet ind i flere; "it works on my machine" øjeblikke.
#### Har også haft store problemmer med opsætningen af selenium i docker miljøet. 
