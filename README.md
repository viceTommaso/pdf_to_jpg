# pdf_to_jpg


## Prerequisites
[python 3](https://www.python.org/downloads/)

## Library
[pdf2image](https://pypi.org/project/pdf2image/), [poppler](https://github.com/oschwartz10612/poppler-windows/releases/)

## Installation
Per l'installazione si procede con il comando da terminale per youtube-dl: `pip install pdf2image` oppure eseguendo il file [setup.bat](\etc\setup.bat).

Successivamente per la libreria poppler, dopo aver scaricato la libreria da questo [link](https://github.com/oschwartz10612/poppler-windows/releases/), oppure eseguendo il file [poppler.bat](\etc\poppler.bat), si scarica la release, si estrae e si sposta dove si vuole. Ora bisogna (come amministratori) andare su `Pannello di controllo>Sistema e sicurezza>Sistema` > `Impostazioni di sistema avanzate` > `Variabili d'ambiente`, premere su `Path` e fare `Modifica...`. Ora fate `Nuovo` ed incollate la path della cartella release fino alla cartella bin (la cartella può essere messa dove si vuole, l'importante è che se si vuole spostare la cartella si modifichi anche la variabile d'ambiente)

Il risulatato dovrà essere simile a questo:

	C:\*\Release-\poppler\Library\bin

Per verificare l'installazione eseguire da linea comando:

	C:\>pdfimages

## Program
Il programma converte i file .pdf in immagini .jpg

Tutti i file presenti nella cartella `pdf` verranno processati e convertiti in immagini che saranno poi presenti nella cartella `jpg`

***SI CONSIGLIA DI ESEGUIRE IL PROGRAMMA A VUOTO PRIMA DELL'USO***

### Funzioni attivabili/disattivabili:

- Creazione di una cartella contenente le immagini convertite se il pdf presenta più pagine, è disattivabile cambiando nella variabile globale `mkdir` da True a False

- Eliminazione dei file pdf processati, è attivabile cambiando nella variabile globale `del_pdf` da False a True

- È poi possibile modificare la cartella sorgente e di destinazione sempre dalle variabili globali `source` e `destination`


## Problems
Se si riscontrano problemi probabilmente bisogna aggiornare le librerie con il comando: `pip install --upgrade pdf2image` oppure eseguendo il file [setup.bat](\etc\setup.bat).

Mentre per la libreria poppler: riscaricare la release e sostituirla a quella precedente dal [sito](https://github.com/oschwartz10612/poppler-windows/releases/) od esguendo il file [poppler.bat](\etc\poppler.bat).

## Author
Vicentini Tommaso
