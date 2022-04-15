SAMPLE_PAYLOAD_JSON = {
    "payload": {
        "google": {
            "expectUserResponse": True,
            "richResponse": {
                "items": [
                    {
                        "simpleResponse": {
                            "textToSpeech": "Wonderful, let's embark on a phantastic journey exploring the mind. Make sure you are comfortable and off we go!"
                        }
                    },
                    {
                        "mediaResponse": {
                            "mediaType": "AUDIO",
                            "mediaObjects": [
                                {
                                    "name": "3 Minute Meditation",
                                    "contentUrl": "http://www.freemindfulness.org/FreeMindfulness3MinuteBreathing.mp3",
                                    "description": "3 Minute Meditation",
                                    "largeImage": {
                                        "url": "https://storage.googleapis.com/automotive-media/album_art.jpg",
                                        "accessibilityText": "Album cover of an ocean view"
                                    }
                                }
                            ]
                        }
                    }
                ],
                "suggestions": [
                    {
                        "title": "Record final Sentiment"
                    },
                    {
                        "title": "Menu"
                    },
                    {
                        "title": "Exit"
                    },
                ]
            }
        }
    }
}

SAMPLE_TEXT_JSON = {
    "fulfillmentText": "Suggestion Chips",
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
