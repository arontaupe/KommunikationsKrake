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
    # opening the CSV file

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


def give_glossary(intent_name, parameters):
    if intent_name == 'glossary.select':
        # read in the query in case there is one given already
        query = parameters.get('glossary')

        if query == '':
            chips = random.sample(list(give_glossary_terms()), 2)
            print('no query was given yet')
            print(chips)
            chips.append('Zurück zum Hauptmenü')
            chips.append('Ich will andere Begriffe bekommen')
            chips.append('Ich habe eine Frage')
            chips.append('Team von Ällei kontaktieren')
            print(chips)
            return chip_response(text='Welchen Begriff soll ich dir erklären? \r\n'
                                      'Hier sind ein paar Wörter, die ich schon kenne: \r\n'
                                      'Klicke einfach eins an. \r\n'
                                      'Oder du gibst ein neues Wort ein, vielleicht kann ich es dann bald erklären. \r\n',
                                 chips=chips,
                                 dgs_videos_bot=make_video_array(['E2']),
                                 dgs_videos_chips=make_video_array(['AC7', 'RC3', 'Feedback1']),
                                 )
        else:
            description = give_description(query)
            print('got query')
            if description:
                return chip_response(text=description,
                                     chips=['Zurück zum Hauptmenü',
                                            'Ich will andere Begriffe bekommen',
                                            'Ich habe eine Frage',
                                            'Team von Ällei kontaktieren'],
                                     dgs_videos_bot=make_video_array(['E2']),
                                     dgs_videos_chips=make_video_array(['AC7', 'RC3', 'Feedback1']),
                                     )
            else:
                return chip_response(text='Zu diesem Begriff habe ich leider noch keine Erklärung.',
                                     chips=['Zurück zum Hauptmenü',
                                            'Ich will andere Begriffe bekommen'
                                            'Ich habe eine Frage',
                                            'Team von Ällei kontaktieren'],
                                     dgs_videos_bot=make_video_array(['E2']),
                                     dgs_videos_chips=make_video_array(['AC7', 'RC3', 'Feedback1']),
                                     )
