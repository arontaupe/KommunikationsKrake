# use pretty printing for json responses
from pprint import pprint

pprint('intent_logic')
# import the response functionality
from response_func import image_response, chip_response, chip_w_context_response, event_response, text_response, \
    context_response, button_response, event_schedule_response


def collect_accessibility_needs(parameters, num_contexts, output_contexts, session_id):
    """

    :param parameters:
    :param num_contexts:
    :param output_contexts:
    :param session_id:
    :return:
    """
    bedarf = parameters.get('bedarf')
    prev_selection_bedarf = None
    for i in range(num_contexts):
        if 'save_bedarf' in output_contexts[i]['name']:
            prev_selection_bedarf = output_contexts[i]['parameters']['prev_selection_bedarf']

    new_bedarf = [0, 0, 0, 0, 0, 0]
    if prev_selection_bedarf:
        new_bedarf = prev_selection_bedarf
        print('Stored on DF: ' + str(new_bedarf))
    if bedarf:
        if bedarf == 'kein Bedarf':
            new_bedarf[0] = 1
        elif bedarf == 'leichte Sprache':
            new_bedarf[1] = 1
        elif bedarf == 'Höreinschränkung':
            new_bedarf[2] = 1
        elif bedarf == 'Mobilitätseinschränkung':
            new_bedarf[3] = 1
        elif bedarf == 'Visuelle Einschränkung':
            new_bedarf[4] = 1
        elif bedarf == 'begrenzte Reize':
            new_bedarf[5] = 1
    print('Now Modified Bedarf: ' + str(new_bedarf))
    return chip_w_context_response(session_id=session_id,
                                   context='save_bedarf',
                                   variable_name='prev_selection_bedarf',
                                   variable=new_bedarf,
                                   text='Okay, ich habe deinen Bedarf ' + bedarf +
                                        ' abgespeichert.'' Willst du weitere Bedarfe angeben?',
                                   chips=["Ja", "Nein, weiter: Interessenselektor", "Menü"])
