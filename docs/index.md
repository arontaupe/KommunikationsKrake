## Kommunikationskrake Prototyp

Achtung, Baustelle!

Hier entsteht ein inklusiver Chatbot.

Er kann mit dir reden.

Er hat leider noch kein Gesicht.

Du kannst ihn schon Fragen, wer er ist.

<meta name="viewport" content="width-device-width, initial-scale=1">

<script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
<df-messenger
  intent="WELCOME"
  chat-title="KommunikationsKrake"
  agent-id="fd541e13-0c7e-47dc-af6a-8c98c865399c"
  language-code="de"
  chat-icon=<i class="fa-brands fa-octopus deploy"></i>
  wait-open=FALSE
></df-messenger>

<style>
  df-messenger {
   --df-messenger-bot-message: #878fac;
   --df-messenger-button-titlebar-color: #df9b56;
   --df-messenger-chat-background-color: #fafafa;
   --df-messenger-font-color: white;
   --df-messenger-send-icon: #878fac;
   --df-messenger-user-message: #479b3d;

   margin: 0;
   padding: 0;
   position: fixed;
   right: 0;
   transform: translateX(50%) translateY(50%);
   bottom: -90px;
  }
</style>
