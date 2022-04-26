# here are the prototypes of the response json files. I can then modify them on the fly to include my answers

SAMPLE_TEXT_JSON = {
    "fulfillmentText": "Suggestion Chips"
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

SAMPLE_EVENT_JSON_3 = {
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
                            "text": "",
                            "link": ""
                        }
                    ],
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
                            "text": "",
                            "link": ""
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
SAMPLE_EVENT_JSON_2 = {
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
                            "text": "",
                            "link": ""
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
