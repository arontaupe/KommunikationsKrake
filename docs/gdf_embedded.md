---
title: Kommunikationskrake
layout: default
author: "Aron Petau"
permalink: /dialogflow/
---
# Dialogflow Version
## Ein Prototyp

Achtung, Baustelle!

Hier entsteht ein inklusiver Chatbot.

Er kann mit dir reden.

Er hat leider noch kein Gesicht.

Du kannst ihn schon Fragen, wer er ist.

<meta name="viewport" content="width-device-width, initial-scale=1">

<style>
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
  height: 300px;
  max-height: 90%;
  min-height: 30%;
  chat-icon="https:&#x2F;&#x2F;www.sommerblut.de&#x2F;wp-content&#x2F;uploads&#x2F;SB-Logo-weiss-tranzp-rgb-ohne-multip.png"
  intent="WELCOME"
  chat-title="Kommunikations Krake"
  agent-id="335d74f7-2449-431d-924a-db70d79d4f88"
  language-code="de"
  allow="microphone;"
></df-messenger>
