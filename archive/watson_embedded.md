---
title: Kommunikationskrake
layout: default
author: "Aron Petau"
permalink: /watson-embedded/
---
# Watson Embedded
## Ein Prototyp

Achtung, Baustelle!

Hier entsteht ein inklusiver Chatbot.

Er kann mit dir reden.

Er hat leider noch kein Gesicht.

Du kannst ihn schon Fragen, wer er ist.

<meta name="viewport" content="width-device-width, initial-scale=1">


<script>
  const element = document.querySelector('.chatElement');
  window.watsonAssistantChatOptions = {
    integrationID: "82fabbed-91f0-4b4b-a004-0e6e179efa29", // The ID of this integration.
    region: "eu-de", // The region your integration is hosted in.
    serviceInstanceID: "fcba3cc5-fcae-480b-a10b-49fb3646e064", // The ID of your service instance.

    // Provide the custom element.
    element: element,
    // Hide the close button since we want it always open.
    hideCloseButton: true,
    // Hide the default launcher.
    showLauncher: false,
    // Make the window open by default.
    openChatByDefault: true,

    onLoad: function(instance) {
      instance.render();
    }
};
  setTimeout(function(){
    const t=document.createElement('script');
    t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
    document.head.appendChild(t);
  });
</script>


