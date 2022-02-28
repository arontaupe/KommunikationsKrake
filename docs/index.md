---
title: Kommunikationskrake
layout: default
author: "Aron Petau"
---
## Ein Prototyp

Achtung, Baustelle!

Hier entsteht ein inklusiver Chatbot.

Er kann mit dir reden.

Er hat leider noch kein Gesicht.

Du kannst ihn schon Fragen, wer er ist.

{% include youtube.html id='iv4Sa2ZjjgM' %}

<meta name="viewport" content="width-device-width, initial-scale=1">

<div class="container">

<style>

.container {
  background-image: url("https://datenbank.sommerblut.de/media/images/normal/0e8a31d19e9a9d0a93156d958cea14e6fa26f6a7d737b9ce1ff18c528278da0d.jpg");
  background-repeat: no-repeat;
  min-height: 940px;
  height: 100%;
  margin: 10px 30px;
}

  df-messenger {
   --df-messenger-bot-message: #e20079;
   --df-messenger-button-titlebar-color: #e20079;
   --df-messenger-chat-background-color: #fafafa;
   --df-messenger-font-color: white;
   --df-messenger-send-icon: #e20079;
   --df-messenger-user-message: orange;
   --df-messenger-chip-border-color:#0041C2;
  }
</style>

<script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
<df-messenger
  chat-icon="https:&#x2F;&#x2F;www.sommerblut.de&#x2F;wp-content&#x2F;uploads&#x2F;SB-Logo-weiss-tranzp-rgb-ohne-multip.png"
  intent="WELCOME"
  chat-title="Kommunikations Krake"
  agent-id="335d74f7-2449-431d-924a-db70d79d4f88"
  language-code="de"
  allow="microphone;"
></df-messenger>

</div>

<iframe
    allow="microphone;"
    width="500"
    height="700"
    src="https://console.dialogflow.com/api-client/demo/embedded/335d74f7-2449-431d-924a-db70d79d4f88">
</iframe>
