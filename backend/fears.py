from response_func import chip_response
from video_builder import make_video_array
import pandas as pd  # Load pandas
import random  # generates random chips for me
import numpy as np
import logging as log


def fears_module(intent_name, parameters, output_contexts, text):
	if intent_name == 'fears.start':
		try:
			fear = random.choice(give_curated_fears())
			return chip_response(text=f'Es ist immer gut über Ängste zu reden! \r\n'
			                          f'Jemand hat mir neulich erzählt, \r\n'
			                          f'ihre größte Angst ist {fear}\r\n'
			                          f'Magst du mir erzählen, wovor du Angst hast?\r\n',
			                     chips=['Ja', 'Nein', 'Vor was haben Leute noch so Angst?'],
			                     dgs_videos_bot=make_video_array(['F4']),
			                     dgs_videos_chips=make_video_array(['RC3', 'AC7'])
			                     )
		except Exception as e:
			print("Exception when accessing curated_fears %s\n" % e)
			return chip_response(text='Ich hatte einen internen Fehler. \r\n'
			                          'Ich kann Nicht über Ängste reden. \r\n'
			                          'Was möchtest du nun tun?',
			                     chips=['Ich habe eine andere Frage',
			                            'Zurück zum Hauptmenü']
			                     )

	elif intent_name == 'fears.start - more':
		fear1 = random.choice(give_curated_fears())
		fear2 = random.choice(give_curated_fears())
		return chip_response(
				text=f'Also, eine andere Person meinte ihre größte Angst ist \r\n'
				     f'{fear1}\r\n'
				     f' und noch wer meinte {fear2}\r\n\r\n'
				     f'Magst du mir nun erzählen, wovor du Angst hast?\r\n',
				chips=['Ja',
				       'Nein']
		)

	elif intent_name == 'fears.start - no':
		return chip_response(text='Das kann ich sehr gut nachempfinden.  \r\n'
		                          'Kann ich dir anvertrauen, was meine größte Angst ist?',
		                     chips=['Ja', 'Lieber nicht']
		                     )

	elif intent_name == 'fears.start - yes':
		fear = parameters.get('fear')
		while fear == '':
			return chip_response(text='Was ist deine größte Angst?\r\n'
			                          'Du kannst direkt tippen.\r\n'
			                          'Meine Angst ist...\r\n',
			                     chips=['Ich will doch nicht antworten']
			                     )

		log.info(f'Recognized {fear}')
		print(f'Recognized {fear}')
		if fear == 'Ich will doch nicht antworten' or fear == 'Ich mag doch nicht antworten':
			return chip_response(text='Das kann ich sehr gut nachempfinden.  \r\n'
			                          'Kann ich dir anvertrauen, was meine größte Angst ist?',
			                     chips=['Ja', 'Lieber nicht']
			                     )

		else:
			add_fear(fear)
			log.info(f'Added {fear}')
			print(f'Added {fear}')
			return chip_response(text=f'Das kann ich sehr gut nachempfinden. \r\n'
			                          f'Kann ich dir anvertrauen, was meine größte Angst ist?',
			                     chips=['Ja', 'Lieber nicht']
			                     )

	elif intent_name == 'fears.start - yes - withdrawal':
		return chip_response(text='Das kann ich sehr gut nachempfinden. '
		                          'Kann ich dir anvertrauen, was meine größte Angst ist?',
		                     chips=['Ja', 'Lieber nicht']
		                     )

	elif intent_name == 'fears.tell-own-fears - no':
		curated_resolution = random.choice(give_curated_resolutions())
		return chip_response(text=f'Jemand hat mir gesagt gegen Angst hilft folgendes:\r\n'
		                          f' {curated_resolution} \r\n'
		                          f'Was hilft dir mit deiner Angst umzugehen?\r\n',
		                     chips=['Ich will nicht antworten', 'Hast du mehr Tipps, was gegen Angst hilft?']
		                     )

	elif intent_name == 'fears.tell-own-fears - yes':
		resolution = parameters.get('resolution')
		while resolution == '':
			curated_resolution = random.choice(give_curated_resolutions())

			return chip_response(text=['Meine größte Angst ist es, \r\n'
			                           'dass sich ganz plötzlich niemand mehr für mich interessiert, \r\n'
			                           'niemand mehr mit mir redet und ich ewige Zeit \r\n'
			                           'ganz einsam bis zu meiner endgültigen Löschung\r\n'
			                           ' verbringen muss.',
			                           f'Jemand hat mir gesagt, gegen Angst hilft folgendes:\r\n'
			                           f' {curated_resolution} \r\n'
			                           f'Was hilft dir mit deiner Angst umzugehen?\r\n'],
			                     chips=['Ich will nicht antworten', 'Hast du mehr Tipps, was gegen Angst hilft?']
			                     )
		print(f'Recognized {resolution}')
		text = f'Mir hilft dieses Jahr auf jeden fall auch das Sommerblut Festival, \r\n' \
		       f'mehr von meiner Angst zu verstehen. \r\n' \
		       f'Soll ich dir eine Veranstaltung empfehlen?\r\n'
		if resolution != 'Ich will doch nicht antworten':
			add_resolution(resolution)
			log.info(f'Added {resolution}')
			print(f'Added {resolution}')
			text = f'Ich merke mir, dass {resolution} gegen Angst hilft.\r\n' + text

		return chip_response(text=text,
		                     chips=['Ja, schlag eine Veranstaltung vor', 'Nein, erzähl lieber einen Witz']
		                     )

	elif intent_name == 'fears.give-resolutions - more':
		resolution1 = random.choice(give_curated_resolutions())
		resolution2 = random.choice(give_curated_resolutions())
		return chip_response(
				text=f'Ähm..  dann hat mir noch jemand gesagt:  \r\n'
				     f'{resolution1}\r\n'
				     f' und noch wer anders: \r\n{resolution2}\r\n\r\n'
				     f'Was hilft dir mit deiner Angst umzugehen?\r\n',
				chips=['Ich will nicht antworten']
		)
	
	else:
		return chip_response(text='Frage zu Angst erkannt, für die es noch keine Antwort gibt.  \r\n',
		                     chips=['Zurück zum Hauptmenü',
		                            'Team von Ällei kontaktieren'],
		                     dgs_videos_chips=make_video_array(['AC7', 'Feedback1']),
		                     )


def give_curated_fears():
	df = pd.read_csv('fears_curated.csv')
	fears_curated = np.array(df.fears_curated.values.tolist())
	return fears_curated


def give_curated_resolutions():
	df = pd.read_csv('fears_curated.csv')
	resolutions_curated = np.array(df.resolutions_curated.values.tolist())
	return resolutions_curated


def add_fear(fear):
	df = pd.DataFrame({'fears_collected'      : [fear],
	                   'resolutions_collected': [None]}
	                  )
	df.to_csv("fears_collected.csv", mode='a', index=False, header=False)


def add_fear_and_resolution(fear, resolution):
	df = pd.DataFrame({'fears_collected'      : [fear],
	                   'resolutions_collected': [resolution]}
	                  )
	df.to_csv("fears_collected.csv", mode='a', index=False, header=False)


def add_resolution(resolution):
	df = pd.DataFrame({'fears_collected'      : [None],
	                   'resolutions_collected': [resolution]}
	                  )
	df.to_csv("fears_collected.csv", mode='a', index=False, header=False)
