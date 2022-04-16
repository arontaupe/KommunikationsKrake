# here are the prototypes of the response json files. I can then modify them on the fly to include my answers

SAMPLE_TEXT_JSON = {
    "fulfillmentText": "Suggestion Chips"
}
SAMPLE_CHIP_JSON = {
    "fulfillmentText": "Suggestion Chips",
    "fulfillmentMessages": [
        {
            "text": {
                "text": [
                    ""
                ]
            }
        },
        {
            "payload": {
                "richContent": [
                    [
                        {
                            "options": [
                                {
                                    "text": "Chip1"
                                }
                            ],
                            "type": "chips"
                        }
                    ]
                ]
            }
        }
    ]
}

SAMPLE_IMAGE_JSON = {
    "fulfillmentText": "Image",
    "fulfillmentMessages": [
        {
            "text": {
                "text": [
                    ""
                ]
            }
        },
        {
            "payload": {
                "richContent": [
                    [
                        {
                            "type": "image",
                            "rawUrl": "https://upload.wikimedia.org/wikipedia/commons/8/8c/DGS.svg",
                            "accessibilityText": "accessibilityText"
                        },
                        {
                            "type": "info",
                            "title": "",
                            "subtitle": "",
                        },
                        {
                            "type": "chips",
                            "options": [
                                {
                                    "text": "Chip1"
                                },
                            ]
                        }
                    ]
                ]
            }
        }
    ]
}
