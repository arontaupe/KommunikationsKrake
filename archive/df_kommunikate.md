---
title: Kommunikationskrake
layout: default
author: "Aron Petau"
permalink: /df-kommunikate/
---
## Dialogflow Prototyp mit Kommunikate 

Achtung, Baustelle!

Hier entsteht ein inklusiver Chatbot.

Er kann mit dir reden.

Er hat leider noch kein Gesicht.

Du kannst ihn schon Fragen, wer er ist.

<meta name="viewport" content="width-device-width, initial-scale=1">

<iframe
            style="border: none;"
            height="800px"
            width="500px"
            src="https://widget.kommunicate.io/chat?appId=1de87dab8813831be2ca348c605d99920"
            allow="microphone; geolocation;"
        >
</iframe>


<script type="text/javascript">
    (function(d, m){

    /*---------------- Kommunicate settings start ----------------*/

     var kommunicateSettings = {
      "appId": "1de87dab8813831be2ca348c605d99920",  
      "automaticChatOpenOnNavigation": true,
      "popupWidget": true,

      "emojilibrary": true,
      "openConversationOnNewMessage": true,
      "voiceInput": true,
      "voiceName":"Google Deutsch", 
      "voiceRate":1,
      "voiceOutput": true
      /*
      "onInit": function (){
        // paste your code here
      }
      */
      };

    /*----------------- Kommunicate settings end ------------------*/

     var s = document.createElement("script");
      s.type = "text/javascript";
      s.async = true;
      s.src = "https://widget.kommunicate.io/v2/kommunicate.app";
      var h = document.getElementsByTagName("head")[0];
      h.appendChild(s);
      window.kommunicate = m;
      m._globals = kommunicateSettings;
    })(document, window.kommunicate || {});
</script>
