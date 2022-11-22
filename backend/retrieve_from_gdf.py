def retrieve_bedarf(output_contexts=None):
    # print('retrieving Bedarf')
    accessibilities = []

    if output_contexts:
        num_contexts = len(output_contexts)
        for i in range(num_contexts):
            if 'final_accessibility' in output_contexts[i]['name']:
                accessibilities = output_contexts[i]['parameters']['final_accessibility']

    return accessibilities


def retrieve_found_events(output_contexts=None):
    titles = []
    ids = []

    event_count = events = None
    if output_contexts:
        num_contexts = len(output_contexts)
        for i in range(num_contexts):
            if 'events_found' in output_contexts[i]['name']:
                events = output_contexts[i]['parameters']['events_found']
                event_count = len(events)
        if events:
            for i in events:
                titles.append(events[i].get('title'))
                ids.append(events[i].get('id'))
    return event_count, events, titles, ids


def whether_searched_events(output_contexts=None):
    if output_contexts:
        num_contexts = len(output_contexts)
        for i in range(num_contexts):
            if 'searched_for_events' in output_contexts[i]['name']:
                return True
        return False
    return False


def retrieve_event_index(output_contexts=None):
    event_index = None
    if output_contexts:
        num_contexts = len(output_contexts)
        for i in range(num_contexts):
            if 'event_index' in output_contexts[i]['name']:
                event_index = output_contexts[i]['parameters']['event_index']
    if event_index is None:
        event_index = 0
    return event_index


def retrieve_event_id(output_contexts=None):
    event_id = None
    if output_contexts:
        num_contexts = len(output_contexts)
        for i in range(num_contexts):
            if 'event_id' in output_contexts[i]['name']:
                event_id = output_contexts[i]['parameters']['event_id']
    if event_id is not None:
        return int(event_id)
    return


def retrieve_page_cache(output_contexts=None):
    page_cache = 1
    if output_contexts:
        num_contexts = len(output_contexts)
        for i in range(num_contexts):
            if 'page_cache' in output_contexts[i]['name']:
                page_cache = output_contexts[i]['parameters']['page_cache']
        return int(page_cache)
    return page_cache


def retrieve_interests(output_contexts=None):
    interest_1 = interest_2 = interest_3 = interest_4 = interest_5 = \
        interest_6 = interest_7 = interest_8 = interest_9 = None

    for i in range(len(output_contexts)):
        if 'interest_1' in output_contexts[i]['name']:
            interest_1 = output_contexts[i]['parameters']['interest_1']
        if 'interest_2' in output_contexts[i]['name']:
            interest_2 = output_contexts[i]['parameters']['interest_2']
        if 'interest_3' in output_contexts[i]['name']:
            interest_3 = output_contexts[i]['parameters']['interest_3']
        if 'interest_4' in output_contexts[i]['name']:
            interest_4 = output_contexts[i]['parameters']['interest_4']
        if 'interest_5' in output_contexts[i]['name']:
            interest_5 = output_contexts[i]['parameters']['interest_5']
        if 'interest_6' in output_contexts[i]['name']:
            interest_6 = output_contexts[i]['parameters']['interest_6']
        if 'interest_7' in output_contexts[i]['name']:
            interest_7 = output_contexts[i]['parameters']['interest_7']
        if 'interest_8' in output_contexts[i]['name']:
            interest_8 = output_contexts[i]['parameters']['interest_8']
        if 'interest_9' in output_contexts[i]['name']:
            interest_9 = output_contexts[i]['parameters']['interest_9']
    return [interest_1, interest_2, interest_3, interest_4, interest_5,
            interest_6, interest_7, interest_8, interest_9]
