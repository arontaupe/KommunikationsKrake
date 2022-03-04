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

![image tooltip here](/assets/avatar.jpg)

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
  chat-icon="https:&#x2F;&#x2F;www.sommerblut.de&#x2F;wp-content&#x2F;uploads&#x2F;SB-Logo-weiss-tranzp-rgb-ohne-multip.png"
  intent="WELCOME"
  chat-title="Kommunikations Krake"
  agent-id="335d74f7-2449-431d-924a-db70d79d4f88"
  language-code="de"
  allow="microphone;"
></df-messenger>



<style>
    @keyframes slideInRight {
      from {
        transform: translate3d(100%, 0, 0);
        visibility: visible;
      }

      to {
        transform: translate3d(0, 0, 0);
      }
    }

    button.chatLauncher {
      animation-duration: 0.5s;
      transition-duration: 0.5s;
      position: fixed;
      bottom: 32px;
      right: 32px;
      z-index: 9999;
      border: 4px solid #075cc2;
      padding: 1em;
      border-radius: 8px;
      margin: 0;
      text-decoration: none;
      background-color: #ffffff;
      color: #454545;
      font-family: sans-serif;
      font-size: 1rem;
      cursor: pointer;
      text-align: left;
      -webkit-appearance: none;
      -moz-appearance: none;
      width: 264px;
      opacity: 0;
    }

    button.chatLauncher.open {
      animation-name: slideInRight;
      opacity: 1;
    }

    button.chatLauncher:hover,
    button.chatLauncher:focus {
      background-color: rgb(225, 225, 254);
      border: 4px solid #0053ba;
    }

    button.chatLauncher:focus {
      outline: 1px solid #0053ba;
      outline-offset: -4px;
    }
  </style>

<!-- We want to hide this element initially, because web chat isn't ready yet. -->
<button type="button" class="chatLauncher" style="display:none;">
  <div>
    <strong>Have questions?</strong> Talk with Karen our Virtual Assistant.
  </div>
</button>

<script>
  window.watsonAssistantChatOptions = {
    integrationID: "82fabbed-91f0-4b4b-a004-0e6e179efa29", // The ID of this integration.
    region: "eu-de", // The region your integration is hosted in.
    serviceInstanceID: "fcba3cc5-fcae-480b-a10b-49fb3646e064", // The ID of your service instance.

    // Config option to hide the default launcher.
    showLauncher: false,

    onLoad: function(instance) {
          // Select the button element from the page.
            const button = document.querySelector('.chatLauncher');

            // Add the event listener to open your web chat.
            button.addEventListener('click', function clickListener() {
              instance.openWindow();
            });

            // Render the web chat. Nothing appears on the page, because the launcher is
            // hidden and the web chat window is closed by default.
            instance.render().then(function() {
              // Now that web chat has been rendered (but is still closed), we make the
              // custom launcher button visible.
              button.style.display = 'block';
              button.classList.add('open');
            });
          },

    carbonTheme: "white",
    enableFocusTrap: true
  };
  setTimeout(function(){
    const t=document.createElement('script');
    t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
    document.head.appendChild(t);
  });
</script>

<iframe
    allow="microphone;"
    width="500"
    height="700"
    src="https://console.dialogflow.com/api-client/demo/embedded/335d74f7-2449-431d-924a-db70d79d4f88">
</iframe>
