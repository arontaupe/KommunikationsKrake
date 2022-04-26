# Kommunikationskrake

Inklusiver Chatbot, zukünftiges Maskottchen.

Hier wird die Website zum testen der Bots gehostet, Materialien dazu in /docs, das Ganze läuft als Static Websites über
jekyll/ghpages

requirements:

```sh
docker
docker-compose
ngrok
```

die restlichen requirements befinden sich im requirements.txt und werden automatisch installiert

Um den code im image zu aktualisieren benutze ich:

```shell
cd Kommunikationskrake
```

In /backend wird der Server entwickelt, er ist in python geschrieben, wird mittels flask und ngrok gehostet

Alle Materialien zur Sommerblut Datenbank API finden sich in /database

Zum Starten wird ein dockerfile und die docker-compose.yml benötigt.

Docker erstellt dann einen container, der lokal auf port 5003 erscheint.

mit ngrok installiert, lässt sich dann mit dem kommando

```sh
ngrok http 127.0.0.1:5003
```

eine weiterleitung an eine https:// adresse erstellen:

Eine Beispieladresse:

```http request
https://3c85-2a02-908-3030-3be0-ac72-30cf-da75-f890.ngrok.io/webhook
```

wichtig ist das /webhook am Ende, ohne geht nicht.

diese muss dann in der dialogflow konsole unter
dem tab Fulfillment eingefügt und **gesaved** werden.

Dialogflow Bot erreichbar unter:

```http request
https://dialogflow.cloud.google.com/#/agent/kommkrake-pcsi/fulfillment
```

Hat das funktioniert, kann in dem Bot "webhook" als test command gesendet werden.
Ist der Webhook erfolgreich verbunden, werden 3 Buttons mit "Der Webhook funktioniert" gesendet.
