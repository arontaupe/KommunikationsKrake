from response_func import chip_response, button_response
from video_builder import make_video_array
import pandas as pd


def give_contact_by_role(role_query):
    """
    """
    email = name = role = ''
    # Read CSV file into DataFrame df
    df = pd.read_csv('team.csv')
    df = df.loc[df["role"] == role_query]
    if not df.empty:
        person = df.values[0]
        name = person[0]
        email = person[2]
        role = person[1]

    return name, email, role


def give_all_roles():
    role_list = ''
    # Read CSV file into DataFrame df
    df = pd.read_csv('team.csv')
    if not df.empty:
        role_list = df['role'].to_list()

    return role_list


def give_team(intent_name, parameters, output_contexts):
    if intent_name == 'team.sommerblut.referral':
        # read in the query in case there is one given already
        team_context = False
        if output_contexts:
            num_contexts = len(output_contexts)
            for i in range(num_contexts):
                if 'team' in output_contexts[i]['name']:
                    team_context = True

        query = parameters.get('sb_role')
        chips = give_all_roles()

        if team_context is True and query == '' or query == '':
            text = 'Kein Problem, ich rede auch gerne mit echten Menschen. \r\n' \
                   'Möchtest du mit jemandem aus dem Sommerblut Team Kontakt aufnehmen?' \
                   '\r\n Hier sind ein paar Kontakte, die dir vielleicht helfen können:' \
                   '\r\n Klicke einfach einen an. '
            return chip_response(text=text,
                                 chips=chips,
                                 # dgs_videos_chips=make_video_array(['AC7', 'RC3', 'Feedback1']),
                                 )

        else:
            name, email, role = give_contact_by_role(role_query=query)
            if name:
                text = f'{name} ist für {role} zuständig. \r\n' \
                       f'Die Person ist erreichbar unter {email}.\r\n' \
                       f'Möchtest du direkt eine E-Mail schreiben?'
                chips = ['Ich will eine andere Person erreichen']

                return button_response(text=text,
                                       chips=chips,
                                       button_text='Direkt E-mail schreiben',
                                       url=f'mailto:{email}'
                                       # dgs_videos_chips=make_video_array(['AC7', 'RC3', 'Feedback1']),
                                       )
            else:
                return chip_response(text='Da ist etwas schief gegangen. \r\n'
                                          f'Zur Abteilung {query} habe ich leider keinen Kontakt.',
                                     chips=['Zurück zum Hauptmenü',
                                            'Team von Ällei kontaktieren'],
                                     # dgs_videos_chips=make_video_array(['AC7', 'RC3', 'Feedback1']),
                                     )
