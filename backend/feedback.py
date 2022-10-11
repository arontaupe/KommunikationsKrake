from response_func import chip_response, button_response
from video_builder import make_video_array


def give_feedback(intent_name):
    """
    The Feedback Module. Responsible for any intents with feedback in their name
    :param intent_name: the name of the identified intent that needs a response
    :return: response for passing to google-DF in compliant json format
    """
    if intent_name == 'mail.feedback':
        return button_response(text='Du kannst uns eine Email schreiben: ',
                               button_text='Email an Ällei',
                               url='mailto:chatbot@sommerblut.de',
                               chips=['Tschüss',
                                      'Hauptmenü'],
                               dgs_videos_bot=make_video_array(['Feedback2']),
                               dgs_videos_chips=make_video_array(['E1', 'AC7'])
                               )

    elif intent_name == 'feedback.sb.good':
        return chip_response(text='Danke! Ich leite es weiter.\r\n '
                                  'Wir finden dich auch super! \r\n',
                             chips=['Veranstaltungsberatung'
                                    'Fingeralphabet lernen',
                                    'Hauptmenü'],
                             # dgs_videos_bot=make_video_array(['Feedback2']),
                             # dgs_videos_chips=make_video_array(['E1', 'AC7'])
                             )

    elif intent_name == 'feedback.sb.bad':
        return button_response(text='Wenn du dich über etwas beschweren oder \r\n'
                                    'konstruktive Kritik äußern möchtest: \r\n'
                                    'Schreib mir gerne eine Mail. \r\n'
                                    'Ich versuche dann, dir weiterzuhelfen. \r\n',
                               button_text='Kritik in einer Mail schreiben',
                               url='mailto:chatbot@sommerblut.de',
                               chips=['Kritik telefonisch äußern',
                                      'Direkter Kontakt zum Team',
                                      'Weiter chatten',
                                      'Tschüss',
                                      'Hauptmenü'],
                               # dgs_videos_bot=make_video_array(['Feedback2']),
                               # dgs_videos_chips=make_video_array(['E1', 'AC7'])
                               )

    elif intent_name == 'feedback.sb.bad - phone':
        return button_response(text='Okay, hier ist unsere Telefonnummer für Anregungen und Kritik: \r\n'
                                    '+49 221 29499139\r\n',
                               button_text='Direkt anrufen',
                               url='tel:+49 221 29499139',
                               chips=['Weiter chatten',
                                      'Tschüss',
                                      'Hauptmenü'],
                               # dgs_videos_bot=make_video_array(['Feedback2']),
                               # dgs_videos_chips=make_video_array(['E1', 'AC7'])
                               )

    elif intent_name == 'feedback.sb.bad - team':
        return button_response(text='Okay, hier findest du das gesamte Team vom Sommerblut. \r\n'
                                    'Kontaktiere uns gern direkt.\r\n',
                               button_text='Das Team anschauen',
                               url='https://www.sommerblut.de/ls/ueber-uns/profil-team',
                               chips=['Weiter chatten',
                                      'Tschüss',
                                      'Hauptmenü'],
                               # dgs_videos_bot=make_video_array(['Feedback2']),
                               # dgs_videos_chips=make_video_array(['E1', 'AC7'])
                               )

    elif intent_name == 'feedback.sb.bad - continue':
        return chip_response(text='Okay, soll ich dir vielleicht einen Witz erzählen? \r\n',
                             chips=['Ja, Witz erzählen',
                                    'Fingeralphabet lernen',
                                    'Hauptmenü'],
                             # dgs_videos_bot=make_video_array(['Feedback2']),
                             # dgs_videos_chips=make_video_array(['E1', 'AC7'])
                             )

    elif intent_name == 'feedback.sb.bad - fallback':
        return button_response(text='Ich habe nicht verstanden, wie du deine Kritik äussern möchtest. \r\n'
                                    'Schreib mir am besten eine Mail. \r\n'
                                    'Ich versuche dann, dir weiterzuhelfen. \r\n',
                               button_text='Kritik in einer Mail schreiben',
                               url='mailto:chatbot@sommerblut.de',
                               chips=['Weiter chatten',
                                      'Hauptmenü'],
                               # dgs_videos_bot=make_video_array(['Feedback2']),
                               # dgs_videos_chips=make_video_array(['E1', 'AC7'])
                               )
