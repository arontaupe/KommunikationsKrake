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
      bottom: 128px;
      right: 128px;
      z-index: 9999;
      border: 4px solid #075cc2;
      padding: 1em;
      border-radius: 8px;
      margin: 0;
      text-decoration: none;
      background-color: #ffffff;
      color: #454545;
      font-family: sans-serif;
      font-size: 2rem;
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

  <button type="button" class="chatLauncher" style="display:none;">
      <strong>Hallo du!</strong> Hier kannst du mit dem Kommunikationskraken reden.
  </button>

<script>
  window.watsonAssistantChatOptions = {
    integrationID: "82fabbed-91f0-4b4b-a004-0e6e179efa29", // The ID of this integration.
    region: "eu-de", // The region your integration is hosted in.
    serviceInstanceID: "fcba3cc5-fcae-480b-a10b-49fb3646e064", // The ID of your service instance.

    // Config option to change Carbon themes.
    carbonTheme: 'g90',

    // Config option to hide the default launcher.
    showLauncher: false,

    // Make the window open by default.
    //openChatByDefault: true,
    //hideCloseButton: true,

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




![image tooltip here](/assets/avatar.jpg)
