class AliceRequest(object):
    def __init__(self, request_dict):
        self._request_dict = request_dict

    @property
    def version(self):
        return self._request_dict['version']

    @property
    def session(self):
        return self._request_dict['session']

    @property
    def user_id(self):
        return self.session['user_id']

    @property
    def is_new_session(self):
        return bool(self.session['new'])

    @property
    def command(self) -> str:
        return self._request_dict['request']['command']

    @property
    def original_utterance(self) -> str:
        return self._request_dict['request']['original_utterance']

    @property
    def session_state(self):
        return self._request_dict['state']['session']

    @property
    def user_state(self):
        return self._request_dict['state']['user']

    @property
    def application_state(self):
        return self._request_dict['state']['application']

    def __str__(self):
        return str(self._request_dict)


class AliceResponse(object):
    def __init__(self, alice_request):
        self._response_dict = {
            "version": alice_request.version,
            "session": alice_request.session,
            "response": {
                "end_session": False,

            }

        }

    # def dumps(self):
    #     return json.dumps(
    #         self._response_dict,
    #         ensure_ascii=False,
    #         indent=2
    #     )

    def bigcard(self, image_id, title, description):
        self._response_dict["response"]["card"] = {}
        self._response_dict["response"]["card"]["type"] = "BigImage"
        self._response_dict["response"]["card"]["image_id"] = image_id
        self._response_dict["response"]["card"]["title"] = title
        self._response_dict["response"]["card"]["description"] = description

    def set_text(self, text):
        self._response_dict['response']['text'] = text[:1024]

    def set_buttons(self, buttons):
        self._response_dict['response']['buttons'] = buttons

    def set_app_state(self, state):
        """В функцию подавать словарь значений без вложенности"""
        self._response_dict["application_state"] = state

    def set_session_state(self, state):
        """В функцию подавать словарь значений без вложенности"""
        self._response_dict["session_state"] = state

    def update_user_state(self, state):
        """В функцию подавать словарь значений без вложенности"""
        self._response_dict["user_state_update"] = state

    def end(self):
        self._response_dict["response"]["end_session"] = True

    @property
    def dictionary(self):
        return self._response_dict

    def __str__(self):
        return self.dumps()
