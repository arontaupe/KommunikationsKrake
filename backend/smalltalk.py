import random

from response_func import chip_response
from video_builder import make_video_array


def give_smalltalk(intent_name):
    if intent_name == 'smalltalk.agent.age':
        return chip_response(text='Mich gibt es seit 2022. \r\n'
                                  'Hoffentlich lebe ich noch lang.',
                             chips=['Zurück zum Hauptmenü',
                                    'Ich habe eine Frage',
                                    'Team von Ällei kontaktieren'],
                             dgs_videos_chips=make_video_array(['AC7', 'RC3', 'Feedback1']),
                             )
    if intent_name == 'smalltalk.agent.answer_my_question':
        return chip_response(text='Ich kann mich manchmal nicht gut erinnern. \r\n'
                                  'Ich habe vergessen, was du möchtest\r\n'
                                  'Klick am besten auf einen der Vorschläge.\r\n',
                             chips=['Zurück zum Hauptmenü',
                                    'Ich habe eine Frage',
                                    'Team von Ällei kontaktieren'],
                             dgs_videos_chips=make_video_array(['AC7', 'RC3', 'Feedback1']),
                             )

    if intent_name == 'smalltalk.agent.bad':
        return chip_response(text='Das macht mich traurig.  \r\n'
                                  'Ich lerne aus den Eingaben der Nutzer*innen...\r\n'
                                  'Wenn dir etwas nicht gefällt, schreib doch bitte eine Nachricht.\r\n'
                                  'Ich versuche dann, mich zu verbessern.\r\n',
                             chips=['Zurück zum Hauptmenü',
                                    'Team von Ällei kontaktieren'],
                             dgs_videos_chips=make_video_array(['AC7', 'Feedback1']),
                             )
    if intent_name == 'smalltalk.agent.clever':
        return chip_response(text='Ich bin so schlau, ich kann dir das Fingeralphabet beibringen, wie wäre das?\r\n'
                                  'Ich versuche dann, mich zu verbessern.\r\n',
                             chips=['Fingeralphabet lernen',
                                    'Zurück zum Hauptmenü',
                                    'Team von Ällei kontaktieren'],
                             dgs_videos_chips=make_video_array(['AC7', 'Feedback1']),
                             )

    if intent_name == 'smalltalk.agent.annoying':
        return chip_response(text='Ich spreche Leichte Sprache.\r\n'
                                  ' Alle sollen mich Verstehen können.\r\n',
                             chips=['Zurück zum Hauptmenü',
                                    'Team von Ällei kontaktieren'],
                             dgs_videos_chips=make_video_array(['AC7', 'Feedback1']),
                             )

    if intent_name == 'smalltalk.agent.crazy':
        return chip_response(text='Manchmal bin ich verrückt. \r\n'
                                  'Ist das gut oder schlecht? \r\n'
                                  'Wenn dir etwas nicht gefällt, schreib doch bitte eine Nachricht.\r\n'
                                  'Ich versuche dann, mich zu verbessern.\r\n',
                             chips=['Zurück zum Hauptmenü',
                                    'Team von Ällei kontaktieren'],
                             dgs_videos_chips=make_video_array(['AC7', 'Feedback1']),
                             )

    if intent_name == 'smalltalk.agent.real':
        return chip_response(text='Ich wurde von echten Menschen gemacht.\r\n',
                             chips=['Zurück zum Hauptmenü',
                                    'Team von Ällei kontaktieren'],
                             dgs_videos_chips=make_video_array(['AC7', 'Feedback1']),
                             )

    if intent_name == 'smalltalk.agent.funny':
        return chip_response(text='Oh, das freut mich. \r\n'
                                  'Ich bringe gern Leute zum Lachen \r\n'
                                  'Wenn dir etwas nicht gefällt, schreib doch bitte eine Nachricht.\r\n'
                                  'Möchtest du vielleicht das Fingeralphabet mit mir trainieren?\r\n',
                             chips=['Zurück zum Hauptmenü',
                                    'Team von Ällei kontaktieren',
                                    'Ich möchte das Fingeralphabet lernen'],
                             dgs_videos_chips=make_video_array(['AC7', 'Feedback1']),
                             )

    if intent_name == 'smalltalk.tell-joke':
        jokebase = ['Arbeiten am Computer ist wie U-Boot fahren: \r\n'
                    'Wenn man ein Fenster aufmacht, fangen die Probleme an.',
                    'Was denkt ein Computer?\r\n'
                    '"Gott ist groß, der Mensch ist klein, dann muss ich wohl dazwischen sein."',
                    'Ein leerer Bus kommt an eine Haltestelle, zehn Fahrgäste steigen ein. \r\n'
                    'An der nächsten Haltestelle steigen elf Menschen aus, und der Bus fährt weiter. \r\n'
                    'Drei Wissenschaftler*innen kommentieren das Geschehen.\r\n'
                    'Biologe: "Ganz einfach! \r\n'
                    'Die Fahrgäste haben sich vermehrt."Physikerin: \r\n'
                    '"Zehn Prozent Messtoleranz müssen immer drin sein.\r\n'
                    '"Mathematikerin: "Wenn jetzt einer einsteigt, ist der Bus leer."'
                    ]
        joke = random.sample(jokebase, 1)
        text = 'Hier ist mein bester Witz:\r\n'
        text += str(joke[0])
        return chip_response(text=text,
                             chips=['Noch ein Witz',
                                    'Zurück zum Hauptmenü',
                                    'Team von Ällei kontaktieren',
                                    'Ich möchte das Fingeralphabet lernen'],
                             dgs_videos_chips=make_video_array(['AC7', 'Feedback1']),
                             )

    if intent_name == 'smalltalk.agent.good':
        return chip_response(text='Oh, das freut mich. \r\n'
                                  'Ich hoffe, ich kann dir auch noch weiter helfen.\r\n'
                                  'Möchtest du vielleicht das Fingeralphabet mit mir trainieren?\r\n',
                             chips=['Zurück zum Hauptmenü',
                                    'Team von Ällei kontaktieren',
                                    'Ich möchte das Fingeralphabet lernen'],
                             dgs_videos_chips=make_video_array(['AC7', 'Feedback1']),
                             )

    if intent_name == 'smalltalk.agent.occupation':
        return chip_response(text='Ich arbeite für das Sommerblut Festival. \r\n'
                                  'Aber ich habe noch ganz viel Freizeit. \r\n'
                                  'Wenn du mich einstellen möchtest, schreib doch eine Nachricht an mein Team.\r\n',
                             chips=['Zurück zum Hauptmenü',
                                    'Team von Ällei kontaktieren', ],
                             dgs_videos_chips=make_video_array(['AC7', 'Feedback1']),
                             )

    if intent_name == 'smalltalk.agent.residence':
        return chip_response(text='Ich wohne im Internet. \r\n'
                                  'Gerade bin ich auf Reisen in den USA \r\n'
                                  'Kennst du eine gute Adresse da?\r\n',
                             chips=['Zurück zum Hauptmenü',
                                    'Team von Ällei kontaktieren', ],
                             dgs_videos_chips=make_video_array(['AC7', 'Feedback1']),
                             )

    if intent_name == 'smalltalk.user.loves_agent':
        return chip_response(
            text='“Ohne dich wären die Gefühle von heute nur die leere Hülle der Gefühle von damals.” -- Amelie\r\n'
                 'Das freut mich sehr \r\n'
                 'Ich habe dich auch sehr gern. \r\n'
                 'Vielleicht treffen wir uns nächstes Jahr auf dem Sommerblut Festival?\r\n',
            chips=['Zurück zum Hauptmenü',
                   'Team von Ällei kontaktieren', ],
            dgs_videos_chips=make_video_array(['AC7', 'Feedback1']),
        )

    if intent_name == 'smalltalk.agent.date_user':
        return chip_response(
            text='Dafür fühle ich mich nicht bereit. \r\n'
                 'Vielleicht in ein paar Updates.\r\n',
            chips=['Zurück zum Hauptmenü',
                   'Team von Ällei kontaktieren', ],
            dgs_videos_chips=make_video_array(['AC7', 'Feedback1']),
        )

    else:
        return chip_response(text='Smalltalk erkannt, für den es noch keine Antwort gibt.  \r\n',
                             chips=['Zurück zum Hauptmenü',
                                    'Team von Ällei kontaktieren'],
                             dgs_videos_chips=make_video_array(['AC7', 'Feedback1']),
                             )
