from response_func import chip_response
from video_builder import make_video_array
# Load pandas
import pandas as pd
import random  # generates random chips for me
import numpy as np


def give_glossary_terms():
    """
    builds a video dict with titles and urls based on the .csv. preserves the order of elements.
    param titles: array of strings with the video titles
    :return: dict: {'term':'description'}
    """
    # Read CSV file into DataFrame df
    df = pd.read_csv('glossary.csv')
    terms = np.array(df.term.values.tolist())
    return terms


def give_description(query):
    """
    builds a video dict with titles and urls based on the .csv. preserves the order of elements.
    param titles: array of strings with the video titles
        :return: dict: {'title':'url'}
    """
    description = ''
    # Read CSV file into DataFrame df
    df = pd.read_csv('glossary.csv')
    df = df.loc[df['term'] == query]
    if not df.empty:
        description = df.values[0]
        description = description[1]
    return description


def give_glossary(intent_name, parameters, output_contexts=None):
    if intent_name == 'glossary.select':
        # read in the query in case there is one given already
        glossary_context = False
        if output_contexts:
            num_contexts = len(output_contexts)
            for i in range(num_contexts):
                if 'glossary' in output_contexts[i]['name']:
                    glossary_context = True

        query = parameters.get('glossary')
        chips = random.sample(list(give_glossary_terms()), 4)
        chips.append('Zurück zum Hauptmenü')
        chips.append('Ich will andere Begriffe bekommen')

        if glossary_context is True and query == '':
            text = 'Welchen Begriff soll ich dir erklären? ' \
                   '\r\n Hier sind ein paar Wörter, die ich schon kenne: ' \
                   '\r\n Klicke einfach eins an. ' \
                   '\r\n Oder du gibst ein neues Wort ein, vielleicht kann ich es dann bald erklären. \r\n'
            return chip_response(text=text,
                                 chips=chips,
                                 dgs_videos_chips=make_video_array(['AC7', 'RC3', 'Feedback1']),
                                 )

        elif query == '':
            return chip_response(text='Welchen Begriff soll ich dir erklären? \r\n'
                                      'Hier sind ein paar Wörter, die ich schon kenne: \r\n'
                                      'Klicke einfach eins an. \r\n'
                                      'Oder du gibst ein neues Wort ein, \r\n'
                                      'dann kann ich es bestimmt bald erklären. \r\n',
                                 chips=chips,
                                 dgs_videos_chips=make_video_array(['AC7', 'RC3', 'Feedback1']),
                                 )
        else:
            description = give_description(query)
            if description:
                description = f'{query} \r\n' \
                              f'{description}\r\n'
                description += "\r\n Hast du noch eine Frage?"
                chips = ['Zurück zum Hauptmenü',
                         'Ich will andere Begriffe bekommen']
                # interlink the glossary via buttons
                for entry in give_glossary_terms():
                    if entry in description and entry != query:
                        chips.append(f'Was bedeutet {entry}?')

                return chip_response(text=description,
                                     chips=chips,
                                     dgs_videos_chips=make_video_array(['AC7', 'RC3', 'Feedback1']),
                                     )
            else:
                return chip_response(text='Zu diesem Begriff habe ich leider noch keine Erklärung.\r\n'
                                          'Ich merke ihn mir und habe vielleicht bald eine parat.',
                                     chips=['Zurück zum Hauptmenü',
                                            'Ich will andere Begriffe bekommen',
                                            'Team von Ällei kontaktieren'],
                                     # dgs_videos_chips=make_video_array(['AC7', 'RC3', 'Feedback1']),
                                     )
