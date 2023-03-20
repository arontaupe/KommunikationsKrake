from response_func import chip_response, button_response
from video_builder import make_video_array
import random  # generates random chips for me


def give_faq(intent_name):
    """
    The FAQ Module. Responsible for any intents with faq in their name.
    param intent_name: the name of the identified intent that needs a response
    :return: response for passing to google-DF in compliant json format
    """
    if intent_name == 'faq.sommerblut.team':
        return button_response(url='https://www.sommerblut.de/ls/ueber-uns/profil-team',
                               button_text='Team vom Sommerblut in externen Tab öffnen',
                               text=' Das Sommerblut hat ein ganz tolles Team. \r\n'
                                    ' Du kannst sie hier finden',
                               chips=['Ich habe eine andere Frage zum Sommerblut',
                                      'Ansprechpartner*in bei Sommerblut finden',
                                      'Ich habe eine Frage zu einem anderen Thema'],
                               dgs_videos_bot=make_video_array(['F4']),
                               dgs_videos_chips=make_video_array(['RC3', 'AC7']))

    elif intent_name == 'faq.contact.accessibility':
        return chip_response(text='Katharina hilft dir gerne bei Fragen zur Barrierefreiheit von Veranstaltungen.\r\n'
                                  'So kannst Du sie erreichen:\r\n'
                                  'katharina.wuerzberg@sommerblut.de\r\n'
                                  'Oder per Telefon: 0221 – 29 49 91 34\r\n',
                             chips=['Zurück zu den Einzelheiten zur Veranstaltung'],
                             dgs_videos_bot=make_video_array(['A21']),
                             dgs_videos_chips=make_video_array(['RC34c'])
                             )

    elif intent_name == 'faq.accessibility':
        return chip_response(text='Unsere Produktionen sollen für möglichst viele Menschen\r\n'
                                  'zugänglich sein.\r\n'
                                  'Bei einigen Aufführungen gibt es Angebote wie:\r\n'
                                  'Deutsche Gebärdensprache. Oder Leichte Sprache.\r\n'
                                  'Oder Audiodeskriptionen.\r\n',
                             chips=['Ich will einen Kontakt für persönliche Unterstützung',
                                    'Welche Veranstaltungen sind Barrierefrei?'],
                             #dgs_videos_bot=make_video_array([]),
                             #dgs_videos_chips=make_video_array(['RC34c'])
                             )

    elif intent_name == 'faq.sb.credo.next':
        return chip_response(text='Unser Motto für 2023 ist: \r\n'
                                  'Geh dahin, wo die Angst ist.\r\n',
                             chips=['Ich habe eine andere Frage'],
                             # dgs_videos_bot=make_video_array(['A21']),
                             # dgs_videos_chips=make_video_array(['RC34c'])
                             )
    elif intent_name == 'faq.sommerblut.where':
        return chip_response(text='Das Festival findet dezentral statt. \r\n'
                                  'Die ganze Stadt ist Sommerblut! \r\n'
                                  'Wenn du persönlich mit jemandem aus dem Sommerblut Team reden willst,\r\n'
                                  'komm doch gerne mal zu einer unserer Veranstaltungen! \r\n'
                                  'Du kannst auch im Büro anrufen oder eine Mail schreiben, \r\n'
                                  'wenn es schnell gehen muss.\r\n',
                             chips=['Wann ist die nächste Veranstaltung?',
                                    'Mit dem Team telefonieren',
                                    'Eine Mail schreiben'],
                             # dgs_videos_bot=make_video_array(['A21']),
                             # dgs_videos_chips=make_video_array(['RC34c'])
                             )
    elif intent_name == 'faq.sommerblut.when':
        return chip_response(text='Das Festival findet jedes Jahr im Mai statt. \r\n'
                                  '2023 beginnt das Festival am 6. Mai \r\n'
                                  'und geht bis zum 25. Mai\r\n',
                             chips=['Wann ist die nächste Veranstaltung?',
                                    'Ich will eine Veranstaltungsberatung',
                                    'Wo gibt es Tickets?'],
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
    #                                'Welche Produktionen beschäftigen sich mit Geschlechterverhältnissen?',
                                    'Wer ist das Sommerblut Team?'],
                             # dgs_videos_bot=make_video_array(['A21']),
                             # dgs_videos_chips=make_video_array(['RC34c'])
                             )

    # Solch eine Antwort geht leider nur über ein Tagfilter system, zu spezifisch um sowas in zukunft pflegen
    # zu können.
    #
    # elif intent_name == 'faq.sommerblut.gender_ratio - which_events':
    #     return button_response(url='https://www.sommerblut.de/ls/veranstaltung/855-queertopolis',
    #                            button_text='Queertopolis anschauen',
    #                            text='Damit hat sich vor allem Queertopolis auseinander gesetzt.\r\n'
    #                                 'Schau dir das doch mal an!',
    #                            chips=[],
    #                            )

    elif intent_name == 'faq.sommerblut.newsletter':
        return button_response(url='mailto:info@sommerblut.de',
                               button_text='Mail senden',
                               text='Lass dich in unseren Newsletter eintragen: \r\n'
                                    'Schreib uns gerne eine Mail mit dem Betreff Newsletter an: \r\n'
                                    'info@sommerblut.de\r\n',
                               chips=['Ich habe eine andere Frage zum Sommerblut',
                                      'Ich habe eine Frage zu einem anderen Thema'],
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
                                    'Ich habe eine andere Frage zum Sommerblut'],
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

    elif intent_name == 'faq.tickets.price':
        return chip_response(text='Der Preis für ein Ticket ist unterschiedlich.\r\n'
                                  'Manche Aufführungen sind kostenlos.\r\n'
                                  'Maximal kosten Tickets 20 Euro.\r\n ',
                             chips=['Wer kann eine ermäßigung bekommen?',
                                    'Wo werden tickets verkauft?'],
                             #dgs_videos_bot=make_video_array(['A24']),
                             #dgs_videos_chips=make_video_array(['RC34', 'RC34c'])
                             )

    elif intent_name == 'faq.tickets.opnv':
        return chip_response(text='Die Eintrittskarten können nicht als Fahrkarte genutzt werden.\r\n',
                             chips = ['Wer kann eine ermäßigung bekommen?',
                                      'Wo werden tickets verkauft?'],
                             # dgs_videos_bot=make_video_array(['A24']),
                             # dgs_videos_chips=make_video_array(['RC34', 'RC34c'])
                             )
    elif intent_name == 'faq.tickets.soldout':
        return button_response(url='https://t.rausgegangen.de/tickets/shop/sommerblut-2022',
                               button_text='Externer Link zum Ticketshop',
                               text='Es passiert häufig, dass Veranstaltungen ausverkaft sind.\r\n'
                                    'Ob noch Karten verfügbar sind, kannst du online sehen.\r\n'
                                    'Oder du kannst uns anrufen.',
                               chips=['Wo werden tickets verkauft?',
                                      'Karten am Telefon bestellen'])


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
                             chips=['Ich habe eine andere Frage zum Sommerblut',
                                      'Ich habe eine Frage zu einem anderen Thema'],
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
        return chip_response(text='2022 kamen im Mai über 7000 Besucher:innen zum Sommerblut Festival.',
                             chips=['Ich habe eine andere Frage zum Sommerblut',
                                    'Ich habe eine Frage zu einem anderen Thema',
                                    'Ich möchte mehr über Ällei erfahren.'],
                             dgs_videos_chips=make_video_array(['AC7']),
                             )

    elif intent_name == 'faq.knowledge.chatbot':
        return chip_response(text='Ein Chatbot Ist eine Maschine, \r\n'
                                  'die sich mit dir unterhalten kann wie ein Mensch.',
                             chips=['Zurück zum Hauptmenü',
                                    'Mehr über Ällei erfahren',
                                    'Ich habe eine andere Frage'],
                             dgs_videos_chips=make_video_array(['AC7']),
                             )

    elif intent_name == 'faq.knowledge.whoami':
        return chip_response(text='Ich bin Ällei, ein Chatbot. \r\n'
                                  'Ich lebe auf der Website des Sommerblut Festivals. \r\n'
                                  'Komm mich gern besuchen!',
                             chips=['Zurück zum  Hauptmenü',
                                    'Mehr über Ällei erfahren',
                                    'Ich habe eine andere Frage'],
                             dgs_videos_chips=make_video_array(['AC7', 'RC3']),
                             )

    elif intent_name == 'faq.sommerblut.donate':
        return button_response(url='https://www.sommerblut.de/de/ueber-uns/unterstuetzen',
                               button_text='Spenden an Sommerblut',
                               text='Großartig. \r\n'
                                    'Das höre ich gern. \r\n'
                                    'Hier findest du alle Infos dazu: ',
                               chips=['Ich habe eine andere Frage zum Sommerblut',
                                      'Ich habe eine Frage zu einem anderen Thema'],
                               dgs_videos_chips=make_video_array(['AC7', 'RC3']),
                               )

    elif intent_name == 'faq.sommerblut.cooperation':
        return chip_response(text='Ja, oft sogar. \r\n'
                                  'Wir freuen uns immer, wenn wir andere arbeiten lassen können.',
                             chips=['Ich habe eine andere Frage zum Sommerblut',
                                    'Ich habe eine Frage zu einem anderen Thema'],
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
                             chips=['Ich habe eine andere Frage zum Sommerblut',
                                    'Wo kann ich Tickets kaufen?',
                                    'Ich habe eine Frage zu einem anderen Thema'],
                             dgs_videos_chips=make_video_array(['AC7', 'RC3']),
                             )

    elif intent_name == 'faq.sommerblut.career':
        return chip_response(text='Wir freuen uns immer, wenn das Sommerblut Team wächst.\r\n '
                                    'Auf unserer Internetseite findest du aktuelle Ausschreibungen. \r\n'
                                    'Oder du kannst meine Kolleg:innen fragen.\r\n '
                                    'Hier ist die Email Adresse: \r\n'
                                    ' info@sommerblut.de',
                               chips=['Ich habe eine andere Frage zum Sommerblut',
                                      'Wer macht was beim Sommerblut?',
                                      'Ich habe eine Frage zu einem anderen Thema'],
                               dgs_videos_chips=make_video_array(['AC7', 'RC3']),
                               )

    elif intent_name == 'faq.sommerblut':
        faq_sb_pool = ['Ich möchte mehr über das Motto 2023 wissen.',
                       'Wie funktioniert Barrierefreiheit beim Festival?',
                       'Womit beschäftigt sich das Sommerblut?',
                       'Wer steckt hinter dem Sommerblut?',
                       'Für wen ist Sommerblut?',
                       'Was bedeutet Sommerblut?',
                       'Wo findet das Festival statt?',
                       'Wie viele Besucher:innen habt Ihr?',
                       'Was ist euer Genderschnitt?',
                       'Wie finanziert sich das Sommerblut?',
                       'Wie spende Ich?',
                       'Kann ich beim Sommerblut arbeiten?',
                       'Gibt einen Newsletter?',
                       'Bekomme Ich eine Ermäßigung?',
                       'Gibt es Informationen zu Corona?',
                       ]
        chips = random.sample(faq_sb_pool, 4)
        chips.append('Andere Frage zum Sommerblut')
        return chip_response(text='Okay, was willst du über das Sommerblut wissen?',
                             chips=chips,
                             dgs_videos_bot=make_video_array(['F3']),
                             dgs_videos_chips=make_video_array(['FA9', 'FA10', 'FA11'])
                             )

    elif intent_name == 'faq.chatbot':
        faq_chatbot_pool = ['Was bedeutet Ällei?',
                            'Bist du ein Spion?',
                            'Wieso gibt es dich?',
                            ]
        chips = random.sample(faq_chatbot_pool, 2)
        chips.append('Andere Frage zum Chatbot', 'Ich verstehe ein Wort nicht')
        return chip_response(text='Okay, was willst du über mich wissen?',
                             chips=chips,
                             dgs_videos_bot=make_video_array(['F3']),
                             )

    elif intent_name == 'faq.start':
        return chip_response(text='Alles klar. Du kannst die Frage unten in das Textfeld schreiben. \r\n'
                                  'Oder du kannst aus einem Bereich auswählen:\r\n',
                             chips=['Ich habe eine Frage zu einer bestimmten Veranstaltung',
                                    'Frage zum Sommerblut allgemein',
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
            chips=['Ich möchte eine Veranstaltungsberatung',
                   'Ich habe eine Frage',
                   'Team von Ällei kontaktieren'],
            dgs_videos_chips=make_video_array(['AC7']),
        )

    elif intent_name == 'faq.bot.name':
        url = 'https://www.sommerblut.de/de/logbuch3'
        button_text = 'Artikel in einem neuen Fenster öffnen'
        return button_response(
				url=url,
				button_text=button_text,
                text='Hihi, nett, dass du nach mir fragst! Mein Name ÄLLEI  \r\n'
                 'leitet sich von dem Szene-Begriff #a11y ab.  \r\n' 
                 'Genauer wird das auf meinem Blog erklärt. \r\n',
                chips=['Ich möchte ein Wort erklärt bekommen',
                   'Ich habe eine Frage',
                   'Team von Ällei kontaktieren'],
                dgs_videos_chips=make_video_array(['AC7']),
        )

    elif intent_name == 'faq.bot.accessibility':
        url = 'https://www.sommerblut.de/de/logbuch3'
        button_text = 'Artikel in einem neuen Fenster öffnen'
        return button_response(
            url=url,
            button_text=button_text,
            text='Ällei macht verschiedene Dinge um barrierefrei zu sein.\r\n'
                 'Zum Beispiel nutzt Ällei einfache Sprache.  \r\n'
                 'Genauer wird das auf meinem Blog erklärt. \r\n',
            chips=['Ich möchte ein Wort erklärt bekommen',
                   'Ich habe eine Frage',
                   'Team von Ällei kontaktieren'],
            dgs_videos_chips=make_video_array(['AC7']),
        )

    else:
        return chip_response(text='FAQ erkannt, für den es noch keine Antwort gibt.  \r\n',
                             chips=['Zurück zum Hauptmenü',
                                    'Team von Ällei kontaktieren'],
                             dgs_videos_chips=make_video_array(['AC7', 'Feedback1']),
                             )
