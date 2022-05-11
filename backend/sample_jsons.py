# here are the prototypes of the response json files. I can then modify them on the fly to include my answers

SAMPLE_TEXT_JSON = {
    "fulfillmentText": "Text Message",
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
                "dgs_videos_bot": {},
                "content_videos": {}
            }
        }
    ]
}

SAMPLE_CONTEXT_JSON = {
    "fulfillmentText": "Setting Context",
    "outputContexts": [
        {
            "name": "projects/kommkrake-pcsi/locations/global/agent/sessions/session-id/contexts/context-name",
            "lifespanCount": 50,
            "parameters": {}
        }
    ]
}
SAMPLE_CHIP_W_CONTEXT_JSON = {
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
                "dgs_videos_bot": {},
                "dgs_videos_chips": {},
                "content_videos": {},
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
    ],
    "outputContexts": [
        {
            "name": "projects/kommkrake-pcsi/locations/global/agent/sessions/session-id/contexts/context-name",
            "lifespanCount": 50,
            "parameters": {}
        }
    ]
}
SAMPLE_CHIP_W_CONTEXT_JSON = {
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
                "dgs_videos_bot": {},
                "dgs_videos_chips": {},
                "content_videos": {},
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
    ],
    "outputContexts": [
        {
            "name": "projects/kommkrake-pcsi/locations/global/agent/sessions/session-id/contexts/context-name",
            "lifespanCount": 50,
            "parameters": {}
        }
    ]
}
SAMPLE_CHIP_W_TWO_CONTEXT_JSON = {
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
                "dgs_videos_bot": {},
                "dgs_videos_chips": {},
                "content_videos": {},
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
    ],
    "outputContexts": [
        {
            "name": "projects/kommkrake-pcsi/locations/global/agent/sessions/session-id/contexts/context-name",
            "lifespanCount": 50,
            "parameters": {}
        },
        {
            "name": "projects/kommkrake-pcsi/locations/global/agent/sessions/session-id/contexts/context-name",
            "lifespanCount": 50,
            "parameters": {}
        }
    ]
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
                "dgs_videos_bot": {},
                "dgs_videos_chips": {},
                "content_videos": {},
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
                "dgs_videos_bot": {},
                "dgs_videos_chips": {},
                "content_videos": {},
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
                            "subtitle": ""
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

SAMPLE_EVENT_DETAILS_JSON = {
    "fulfillmentText": "Event Details",
    "fulfillmentMessages": [
        {"text": {"text": [""]}},
        {
            "payload": {
                "dgs_videos_bot": {},
                "dgs_videos_chips": {},
                "content_videos": {},
                "richContent": [
                ],
                "event_details": {}
            }
        }
    ]
}
SAMPLE_EVENT_SCHEDULE_JSON = {
    "fulfillmentText": "Event Schedule",
    "fulfillmentMessages": [
        {"text": {"text": [""]}},
        {
            "payload": {
                "dgs_videos_bot": {},
                "dgs_videos_chips": {},
                "content_videos": {},
                "richContent": [
                ],
                "plays": {}
            }
        }
    ]
}
SAMPLE_EVENT_JSON_1 = {
    "fulfillmentText": "Event",
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
                "dgs_videos_bot": {},
                "dgs_videos_chips": {},
                "content_videos": {},
                "richContent": [
                    [
                        {
                            "type": "image",
                            "rawUrl": ""
                        },
                        {
                            "type": "info",
                            "title": "",
                            "subtitle": ""
                        },
                        {
                            "type": "accordion",
                            "title": "",
                            "subtitle": "",
                            "image": {
                                "src": {
                                    "rawUrl": ""
                                }
                            },
                            "text": ""
                        },
                        {
                            "type": "accordion",
                            "title": "",
                            "subtitle": "",
                            "image": {
                                "src": {
                                    "rawUrl": ""
                                }
                            },
                            "text": ""
                        }
                    ],
                    [
                        {
                            "type": "chips",
                            "options": [
                                {
                                    "text": "Chip1"
                                }
                            ]
                        }
                    ]
                ],
                "event": {}
            }
        }
    ],
    "outputContexts": [
        {
            "name": "projects/kommkrake-pcsi/locations/global/agent/sessions/session-id/contexts/context-name",
            "lifespanCount": 50,
            "parameters": {}
        }
    ]
}

SAMPLE_EVENT_W_BUTTON_JSON_1 = {
    "fulfillmentText": "Event",
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
                "dgs_videos_bot": {},
                "dgs_videos_chips": {},
                "content_videos": {},
                "richContent": [
                    [
                        {
                            "type": "image",
                            "rawUrl": ""
                        },
                        {
                            "type": "info",
                            "title": "",
                            "subtitle": ""
                        },
                        {
                            "type": "accordion",
                            "title": "",
                            "subtitle": "",
                            "image": {
                                "src": {
                                    "rawUrl": ""
                                }
                            },
                            "text": ""
                        },
                        {
                            "type": "accordion",
                            "title": "",
                            "subtitle": "",
                            "image": {
                                "src": {
                                    "rawUrl": ""
                                }
                            },
                            "text": ""
                        },
                        {
                            "type": "button",
                            "icon": {
                                "type": "chevron_right",
                                "color": "#FF9800"
                            },
                            "text": "Tickets kaufen",
                            "link": "https://sommerblut.de"
                        }
                    ],
                    [
                        {
                            "type": "chips",
                            "options": [
                                {
                                    "text": "Chip1"
                                }
                            ]
                        }
                    ]
                ],
                "event": {}
            }
        }
    ],
    "outputContexts": [
        {
            "name": "projects/kommkrake-pcsi/locations/global/agent/sessions/session-id/contexts/context-name",
            "lifespanCount": 50,
            "parameters": {}
        }
    ]
}

SAMPLE_BUTTON_JSON = {
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
                "dgs_videos_bot": {},
                "dgs_videos_chips": {},
                "content_videos": {},
                "richContent": [
                    [
                        {
                            "type": "button",
                            "icon": {
                                "type": "chevron_right",
                                "color": "#FF9800"
                            },
                            "text": "Button text",
                            "link": "https://example.com",
                            "event": {
                                "name": "",
                                "languageCode": "",
                                "parameters": {}
                            }
                        },
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
