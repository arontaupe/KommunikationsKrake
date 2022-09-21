from response_func import chip_response, button_response
from video_builder import make_video_array


def give_faq(intent_name):
    """
    The FAQ Module. Responsible for any intents with faq in their name.
    param intent_name: the name of the identified intent that needs a response
    :return: response for passing to google-DF in compliant json format
    """
    if intent_name == 'faq.sommerblut.team':
        return button_response(url='https://www.sommerblut.de/ls/ueber-uns/profil-team',
                               button_text='Das Team vom Sommerblut',
                               text=' Das Sommerblut hat ein ganz tolles Team. \r\n'
                                    ' Du kannst sie hier finden',
                               chips=['Ich habe eine andere Frage', 'Zurück zum Hauptmenü'],
                               dgs_videos_bot=make_video_array(['F4']),
                               dgs_videos_chips=make_video_array(['RC3', 'AC7']))

    elif intent_name == 'faq.contact.accessibility':
        return chip_response(text='Franziska hilft dir gerne bei Fragen zur Barrierefreiheit von Veranstaltungen.\r\n'
                                  'So kannst Du sie erreichen:\r\n'
                                  'franziska.lammers@sommerblut.de\r\n'
                                  'Oder per Telefon: 0221 – 29 49 91 34\r\n',
                             chips=['Zurück zu den Einzelheiten zur Veranstaltung'],
                             dgs_videos_bot=make_video_array(['A21']),
                             dgs_videos_chips=make_video_array(['RC34c'])
                             )

    elif intent_name == 'faq.sb.credo.next':
        return chip_response(text='Unser Motto für 2023 ist: \r\n'
                                  'Geh dahin, wo die Angst ist.\r\n',
                             chips=[],
                             # dgs_videos_bot=make_video_array(['A21']),
                             # dgs_videos_chips=make_video_array(['RC34c'])
                             )
    elif intent_name == 'faq.sommerblut.where':
        return chip_response(text='Das Festival findet dezentral statt. \r\n'
                                  'Die ganze Stadt ist Sommerblut! \r\n'
                                  'Wenn du persönlich mit jemandem aus dem Sommerblut Team reden willst,\r\n'
                                  ' komm doch gerne mal zu einer unserer Veranstaltungen! \r\n'
                                  'Du kannst auch im Büro anrufen oder eine Mail schreiben, \r\n'
                                  'wenn es schnell gehen muss.\r\n',
                             chips=['Wann ist die nächste Veranstaltung?',
                                    'Mit dem Team telefonieren',
                                    'Eine Mail schreiben'],
                             # dgs_videos_bot=make_video_array(['A21']),
                             # dgs_videos_chips=make_video_array(['RC34c'])
                             )
    elif intent_name == 'faq.sommerblut.where':
        return chip_response(text='Das Festival findet dezentral statt. \r\n'
                                  'Die ganze Stadt ist Sommerblut! \r\n'
                                  'Wenn du persönlich mit jemandem aus dem Sommerblut Team reden willst,\r\n'
                                  ' komm doch gerne mal zu einer unserer Veranstaltungen! \r\n'
                                  'Du kannst auch im Büro anrufen oder eine Mail schreiben, \r\n'
                                  'wenn es schnell gehen muss.\r\n',
                             chips=['Wann ist die nächste Veranstaltung?',
                                    'Mit dem Team telefonieren',
                                    'Eine Mail schreiben'],
                             # dgs_videos_bot=make_video_array(['A21']),
                             # dgs_videos_chips=make_video_array(['RC34c'])
                             )

    elif intent_name == 'faq.sommerblut.where - phone':
        return button_response(url='tel:+49 221 29499139',
                               button_text='Direkt anrufen',
                               text='Okay, die Telefonnummer ist: +49 221 29499139\r\n',
                               chips=['Wann ist die nächste Veranstaltung?'],
                               # dgs_videos_bot=make_video_array(['A21']),
                               # dgs_videos_chips=make_video_array(['RC34c'])
                               )

    elif intent_name == 'faq.sommerblut.where - mail':
        return button_response(url='mailto:info@sommerblut.de',
                               button_text='Direkt Mail schreiben',
                               text='Okay, die Email ist: info@sommerblut.de\r\n',
                               chips=['Wann ist die nächste Veranstaltung?'],
                               # dgs_videos_bot=make_video_array(['A21']),
                               # dgs_videos_chips=make_video_array(['RC34c'])
                               )
    elif intent_name == 'faq.sommerblut.gender_ratio':
        return chip_response(text='Das Sommerblut Festival thematisiert in seinen vielfältigen Produktionen \r\n'
                                  'immer wieder Genderrollen und Sexismus. \r\n'
                                  'Das Team vom Sommerblut bemüht sich um ein ausgewogenes Verhältnis\r\n'
                                  ' aller Geschlechter, hat jedoch dazu keine festgeschriebenen Regelungen. \r\n',
                             chips=['Was ist Gender?',
                                    'Welche Produktionen beschäftigen sich mit Geschlechterverhältnissen?',
                                    'Wer ist das Sommerblut Team?'],
                             # dgs_videos_bot=make_video_array(['A21']),
                             # dgs_videos_chips=make_video_array(['RC34c'])
                             )

    elif intent_name == 'faq.sommerblut.gender_ratio - which_events':
        return button_response(url='https://www.sommerblut.de/ls/veranstaltung/855-queertopolis',
                               button_text='Queertopolis anschauen',
                               text='Damit hat sich vor allem Queertopolis auseinander gesetzt.\r\n'
                                    'Schau dir das doch mal an!',
                               chips=[],
                               )

    elif intent_name == 'faq.sommerblut.newsletter':
        return button_response(url='mailto:info@sommerblut.de',
                               button_text='Mail senden',
                               text='Lass dich in unseren Newsletter eintragen: \r\n'
                                    'Schreib uns gerne eine Mail mit dem Betreff Newsletter an: \r\n'
                                    'info@sommerblut.de\r\n',
                               chips=[],
                               )

    elif intent_name == 'faq.sommerblut.name':
        return chip_response(text='Da muss ich dich vermutlich enttäuschen. \r\n'
                                  'Hinter diesem Namen verbirgt sich keine allzu spannende Geschichte.\r\n '
                                  'Das Kulturfestival Sommerblut ist ein Vorbote des Hochsommers,\r\n '
                                  'denn es findet immer im Mai statt. Und wir könnten nicht existieren, \r\n'
                                  'wenn nicht viele verschiedene Menschen mit viel Herzblut dabei wären. \r\n'
                                  'Möchtest du mehr über das Festival erfahren?\r\n',
                             chips=['Was gibt es für Veranstaltungen?',
                                    'Worum geht es beim Sommerblut Festival?',
                                    'Wie lautet das Festivalmotto?',
                                    'Nein, ich möchte einen Witz erzählen'
                                    ],
                             # dgs_videos_bot=make_video_array(['A21']),
                             # dgs_videos_chips=make_video_array(['RC34c'])
                             )

    elif intent_name == 'faq.assistance.onsite':
        return button_response(text='Das kommt auf die Veranstaltung an.'
                                    ' Wir möchten Sommerblut für alle Menschen so zugänglich wie möglich gestalten. '
                                    'Schicke uns einfach eine E-Mail und frag nach: info@sommerblut.de. \r\n'
                                    'Oder per Telefon: 0221 – 29 49 91 34\r\n',
                               url='mailto:info@sommerblut.de',
                               button_text='Anfrage per Email',
                               chips=['Hauptmenü'],
                               # dgs_videos_bot=make_video_array(['A21']),
                               # dgs_videos_chips=make_video_array(['RC34c'])
                               )

    elif intent_name == 'faq.finance.how':
        return button_response(url='https://www.sommerblut.de/de/ueber-uns/foerderer-und-sponsoren',
                               button_text='Unsere Sponsoren',
                               text='Zu unseren Sponsoren gehören das "Hostel Köln", '
                                    'das "Maritim Hotel Köln" und die "REWE Group". '
                                    'Alle aktuellen Sponsoren und Förderer findest du hier auf unserer Website:  '
                                    'https://www.sommerblut.de/de/ueber-uns/foerderer-und-sponsoren',
                               chips=['Ich habe eine andere Frage'],
                               dgs_videos_bot=make_video_array(['A21']),
                               dgs_videos_chips=make_video_array(['RC34c'])
                               )

    elif intent_name == 'faq.tickets.sale_location':
        return chip_response(text='An folgenden Orten können Tickets gekauft werden:\r\n'
                                  'Theater·kasse am Neumarkt\r\n'
                                  'Die Theater·kasse ist auf der Zwischen·ebene der U-Bahn-Station Neumarkt.\r\n '
                                  'Die genaue Adresse ist:\r\n'
                                  'Neumarkt, U-Bahn-Passage\r\n'
                                  'Laden 12\r\n'
                                  '50667 Köln, \r\n',
                             chips=['Zeig mir die Veranstaltung auf Sommerblut.de',
                                    'Zurück zu den Einzelheiten zur Veranstaltung'],
                             dgs_videos_bot=make_video_array(['A24']),
                             dgs_videos_chips=make_video_array(['RC34', 'RC34c'])
                             )

    elif intent_name == 'faq.covid':
        return chip_response(
            text='Wir möchten, dass sich auf unserem Festival alle Menschen gut und sicher fühlen. \r\n'
                 'Daher ist es wichtig, dass sich alle Besucher:innen an die geltenden Corona-Maßnahmen halten. \r\n'
                 'Da unser Festival an vielen verschiedenen Orten in der Stadt stattfindet, \r\n'
                 'können die Corona-Regeln je nach Ort unterschiedlich sein. \r\n'
                 'Bitte informiere dich vor deinem Besuch über die geltenden Coronaregeln \r\n'
                 'am jeweiligen Veranstaltungsort.\r\n',
            chips=['Ich habe eine andere Frage',
                   'Zurück zum Hauptmenü'],
            dgs_videos_chips=make_video_array(['RC34', 'RC34c'])
        )

    elif intent_name == 'faq.sommerblut.size':
        return chip_response(text='Vom 6. bis 22. Mai 2022 hat das Sommerblut Festival 17 Produktionen \r\n'
                                  'und Gastspiele mit 63 Aufführungen an 13 unterschiedlichen Spielorten '
                                  'realisiert.\r\n',
                             chips=['Ich habe eine andere Frage',
                                    'Zurück zum Hauptmenü'],
                             dgs_videos_chips=make_video_array(['RC34', 'RC34c'])
                             )

    elif intent_name == 'faq.assistance.bring_human':
        return button_response(button_text="Mail schreiben",
                               url='mailto:info@sommerblut.de',
                               text='Menschen mit Nachweis über eine Behinderung können '
                                    'eine Begleitperson mitbringen. \r\n'
                                    'Schicke uns einfach eine E-Mail und frag nach,'
                                    ' um ein solches Ticket zu erhalten: \r\n'
                                    'info@sommerblut.de.\r\n',
                               chips=['Ich habe eine andere Frage',
                                      'Zurück zum Hauptmenü'],
                               dgs_videos_chips=make_video_array(['RC34', 'RC34c'])
                               )

    elif intent_name == 'faq.need_human':
        return button_response(button_text="Ruf uns direkt hier an",
                               url='tel:+4922129499134',
                               text='Schreib uns an die info@sommerblut.de \r\n'
                                    'oder ruf unser Büro an unter: +49 (221) 29 49 91 – 34',
                               chips=['Ich habe eine andere Frage',
                                      'Zurück zum Hauptmenü'],
                               dgs_videos_chips=make_video_array(['RC34', 'RC34c'])
                               )

    elif intent_name == 'faq.assistance.bring_dog':
        return button_response(button_text="Mail schreiben",
                               url='mailto:info@sommerblut.de',
                               text='In der Regel kannst du mit einem Assistenzhund '
                                    'zu unseren Veranstaltungen kommen. \r\n'
                                    'Am besten fragst du aber für den spezifischen Standort '
                                    'bei unserem Team nach. \r\n'
                                    'Schicke uns einfach eine E-Mail an info@sommerblut.de',
                               chips=['Ich habe eine andere Frage',
                                      'Zurück zum Hauptmenü'],
                               dgs_videos_chips=make_video_array(['RC34', 'RC34c'])
                               )

    elif intent_name == 'faq.tickets.sale_phone':
        return button_response(url='tel:+4922142076000',
                               button_text='Direkt anrufen',
                               text='Du kannst die Tickets auch am Telefon bestellen.\r\n'
                                    'Unter der Telefonnummer 0221 42 07 6000.\r\n'
                                    'Aber Achtung:\r\n'
                                    'Am Telefon kann man die Tickets mit Kreditkarte bezahlen.\r\n',
                               chips=['Zeig mir die Veranstaltung auf Sommerblut.de',
                                      'Zurück zu den Einzelheiten zur Veranstaltung'],
                               dgs_videos_chips=make_video_array(['RC34', 'RC34c']),
                               dgs_videos_bot=make_video_array(['A23']),
                               )

    elif intent_name == 'faq.sommerblut.for-who':
        return chip_response(text='Das Sommerblut ist für alle da.',
                             chips=['Hauptmenü', 'Ich habe eine Frage', 'Team von Ällei kontaktieren'],
                             dgs_videos_chips=make_video_array(['AC7']),
                             )

    elif intent_name == 'faq.sommerblut.how-many-visitors':
        return chip_response(text='2022 kamen im Mai über 7000 Besucher*innen zum Sommerblut Festival.',
                             chips=['Hauptmenü', 'Ich habe eine Frage', 'Team von Ällei kontaktieren'],
                             dgs_videos_chips=make_video_array(['AC7']),
                             )

    elif intent_name == 'faq.knowledge.chatbot':
        return chip_response(text='Ein Chatbot Ist eine Maschine, die sich mit dir unterhalten kann wie ein Mensch.',
                             chips=['Zurück zum Hauptmenü', 'Ich habe eine andere Frage'],
                             dgs_videos_chips=make_video_array(['AC7']),
                             )

    elif intent_name == 'faq.knowledge.whoami':
        return chip_response(text='Ich bin Ällei, ein Chatbot. \r\n'
                                  'Ich lebe auf der Website des Sommerblut Festivals. \r\n'
                                  'Komm mich gern besuchen!',
                             chips=['Zurück zum  Hauptmenü', 'Ich habe eine andere Frage'],
                             dgs_videos_chips=make_video_array(['AC7', 'RC3']),
                             )

    elif intent_name == 'faq.sommerblut.donate':
        return button_response(url='https://www.sommerblut.de/de/ueber-uns/unterstuetzen',
                               button_text='Spenden an Sommerblut',
                               text='Großartig. \r\n'
                                    'Das höre ich gern. \r\n'
                                    'Hier findest du alle Infos dazu: ',
                               chips=['Zurück zum  Hauptmenü',
                                      'Ich habe eine andere Frage'],
                               dgs_videos_chips=make_video_array(['AC7', 'RC3']),
                               )

    elif intent_name == 'faq.sommerblut.cooperation':
        return chip_response(text='Ja, oft sogar. \r\n'
                                  'Wir freuen uns immer, wenn wir andere arbeiten lassen können.',
                             chips=['Zurück zum  Hauptmenü',
                                    'Ich habe eine andere Frage'],
                             dgs_videos_chips=make_video_array(['AC7', 'RC3']),
                             )

    elif intent_name == 'faq.sommerblut.discount':
        return chip_response(text='Wir bieten ermäßigte Tickets für viele unterschiedliche Gruppen und Menschen:\r\n '
                                  'Schüler:innen, Studierende, Azubis und Freiwilligendienstleistende.\r\n'
                                  'Menschen mit Nachweis über eine Behinderung.\r\n'
                                  'Menschen, die Hartz IV oder andere Bezüge und soziale Hilfen erhalten. \r\n'
                                  'Auch mit Kölnpass gibt es Anspruch auf ermäßigte Tickets.\r\n'
                                  'Solltest Du dir unsicher sein, ob Du in eine dieser Kategorien fällst, \r\n'
                                  'schicke uns einfach eine E-Mail und frag nach. \r\n'
                                  'Wir möchten Sommerblut für alle Menschen so zugänglich wie möglich gestalten.',
                             chips=['Zurück zum  Hauptmenü',
                                    'Ich habe eine andere Frage'],
                             dgs_videos_chips=make_video_array(['AC7', 'RC3']),
                             )

    elif intent_name == 'faq.sommerblut.career':
        return button_response(url='mailto:info@sommerblut.de',
                               button_text='Schreib uns eine Mail',
                               text='Wir freuen uns immer, wenn das Sommerblut Team wächst. '
                                    'Schau doch einmal bei den Ausschreibungen vorbei. '
                                    'Oder du kannst meine Kolleg*innen fragen. '
                                    'Hier ist die Email Adresse:  info@sommerblut.de',
                               chips=['Zurück zum  Hauptmenü',
                                      'Ich habe eine andere Frage'],
                               dgs_videos_chips=make_video_array(['AC7', 'RC3']),
                               )

    elif intent_name == 'faq.sommerblut':
        return chip_response(text='Okay, was willst du über das Sommerblut wissen?',
                             chips=['Ich möchte mehr über das Motto 2022 wissen.',
                                    'Womit beschäftigt sich das Sommerblut?',
                                    # 'Frage zur Barrierefreiheit',
                                    'Wer steckt hinter dem Sommerblut?'],
                             dgs_videos_bot=make_video_array(['F3']),
                             dgs_videos_chips=make_video_array(['FA9', 'FA10', 'FA11'])
                             )

    elif intent_name == 'faq.start':
        return chip_response(text='Alles klar. Du kannst die Frage unten in das Textfeld schreiben. \r\n'
                                  'Oder du kannst aus einem Bereich auswählen:\r\n',
                             chips=['Ich habe eine Frage zu einer bestimmten Veranstaltung',
                                    'Frage zum Sommerblut allgemein',
                                    # 'Frage zur Barrierefreiheit',
                                    'Frage zu Ällei, dem Chatbot',
                                    'Das Fingeralphabet kennen lernen',
                                    'Begriff erklären'],
                             dgs_videos_bot=make_video_array(['F1']),
                             dgs_videos_chips=make_video_array(['FA1', 'FA2', 'FA4', 'FA5'])
                             )

    elif intent_name == 'faq.bot.cando':
        return chip_response(
            text='Ich bin noch am lernen. \r\n'
                 'Ich kann dir Veranstaltungen empfehlen und Fragen beantworten. \r\n'
                 'Hoffentlich bin ich bald so fit im Internet wie du.\r\n',
            chips=['Hauptmenü', 'Ich habe eine Frage', 'Team von Ällei kontaktieren'],
            dgs_videos_chips=make_video_array(['AC7']),
        )

    else:
        return chip_response(text='FAQ erkannt, für den es noch keine Antwort gibt.  \r\n',
                             chips=['Zurück zum Hauptmenü',
                                    'Team von Ällei kontaktieren'],
                             dgs_videos_chips=make_video_array(['AC7', 'Feedback1']),
                             )
