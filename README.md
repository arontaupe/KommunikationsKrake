# Kommunikationskrake

Inklusiver Chatbot, zukünftiges Maskottchen.

Hier wird die Website zum Testen der Bots gehostet, Materialien dazu in /docs, das Ganze läuft als Static Websites über
jekyll undGithub Pages

requirements:

```sh
docker
docker-compose
ngrok # nur für lokales hosting
```

Die restlichen Requirements befinden sich im requirements.txt und werden automatisch installiert

Um den Code im Image zu aktualisieren benutze ich:

```shell
docker-compose build
docker push arontaupe/allei
```

Zum Starten des Containers:

```shell
docker-compose up
```

Ich habe eine eigene docker-compose.yml angelegt, sie ist identisch zu docker-compose-obfuscated.yml

Zum Starten wird ein dockerfile und die docker-compose.yml benötigt.
Zum Starten müsste die Datei umbenannt werden zu docker-compose.yml, und alle Secrets entsprechend in die Environment
Variables eingetragen werden
In /backend wird der Server entwickelt, er ist in python geschrieben, wird mittels flask und ngrok gehostet

Alle Materialien zur Sommerblut Datenbank API finden sich in /database

Docker erstellt dann einen Container, der lokal auf port 5003 erscheint.

mit ngrok lässt sich dann mit dem kommando

```sh
ngrok http 5003
```
eine weiterleitung an eine https:// adresse erstellen:

Eine Beispieladresse:

```http request
https://3c85-2a02-908-3030-3be0-ac72-30cf-da75-f890.ngrok.io/webhook
```

wichtig ist das /webhook am Ende, ohne geht nicht, da das die entsprechende App route ist,
über die API Antworten ausgewertet werden.
Auf der Index Page findet sich eine Simple Hello world Message, erscheint diese, Ist der Container Korrekt gestartet.

Die /webhook route ist mit basic auth abgesichert, die entsprechenden Daten müssen in der Dialogflow Console eingetragen
werden.

Wahlweise die Ngrok https Adresse oder die URL des Docker Containers muss dann in der Dialogflow Konsole unter
dem tab Fulfillment eingefügt und **gesaved** werden.

Die Dialogflow Bot Console ist erreichbar unter:

```http request
https://dialogflow.cloud.google.com/#/agent/kommkrake-pcsi/fulfillment
```

Hat das funktioniert, kann in dem Bot "webhook" oder "test" als test command gesendet werden.
Ist der Webhook erfolgreich verbunden, werden 3 Buttons mit "Der Webhook funktioniert" gesendet.

Hier testet Jens