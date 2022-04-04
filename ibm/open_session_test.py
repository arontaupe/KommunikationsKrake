import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('iudr9lu-TJAnpiAfK00vVfni2rkTi38sT37hFtyjpmbG')
assistant = AssistantV2(
    version='2021-06-14',
    authenticator = authenticator
)

assistant.set_service_url(
    'https://api.eu-de.assistant.watson.cloud.ibm.com/instances/fcba3cc5-fcae-480b-a10b-49fb3646e064/v2/assistants/19e4f366-5bfb-4c9c-a54c-83ee3d607abe/sessions'
)

response = assistant.create_session(assistant_id='19e4f366-5bfb-4c9c-a54c-83ee3d607abe').get_result()

print(json.dumps(response, indent=2))