from azion.__consts__ import (
    DEFAULT_PARAMS, PUBLIC_ENDPOINT, USER_AGENT, VERSION)

from azion.models import (
    Domain, EdgeApplication, EdgeFunction, ErrorResponses, CacheSettings, Rule, Token,
    as_boolean, decode_json, filter_none, instance_from_data, many_of)

import requests
import base64

class Client(requests.Session):

    def __init__(self, debug=False, **kwargs):
        requests.Session.__init__(self)
        self.base_url = PUBLIC_ENDPOINT
        self.session = requests.sessions.Session()
        self.headers = self.default_headers()

        self.debugIfEnabled(debug)

        username = kwargs.get('username')
        password = kwargs.get('password')
        token = kwargs.get('token')

        if token:
            self.use_token(token)
        elif username and password:
            token = self.generate_token(username, password)
            self.use_token(token)
        else:
            raise ValueError("Token or (username and password) must be provided")


    def default_headers(self):
        return {
            'Accept': 'application/json; version={}'.format(VERSION),
            'Accept-Charset': 'utf-8',
            'Content-Type': 'application/json',
            'User-Agent': '{}'.format(USER_AGENT)
        }


    def generate_token(self, username, password):
        raw = f'{username}:{password}'.encode('ascii')
        value = base64.b64encode(raw).decode('ascii')

        self.headers.update({
            'Authorization': 'Basic {}'.format(value)
        })

        url = self.build_url('tokens')
        response = self.post(url)
        json = decode_json(response, 201)

        return instance_from_data(Token, json).value


    def use_token(self, token):
        self.headers.update({
            'Authorization': 'Token {}'.format(token)
        })


    def build_url(self, *args, **kwargs):
        """Build a URL depending on the `base_url`
        attribute."""
        params = [kwargs.get('base_url') or self.base_url]
        params.extend(args)
        params = list(map(str, params))
        return '/'.join(params)


    def domains(self):
        payload = {'page_size': 100}
        url = self.build_url('domains')
        response = self.get(url, params = DEFAULT_PARAMS)
        json = decode_json(response, 200)

        return many_of(Domain, json['results'])


    def get_domain(self, domain_id):
        url = self.build_url('domains', domain_id)
        response = self.get(url)
        json = decode_json(response, 200)

        return instance_from_data(Domain, json['results'])


    def edge_applications(self):
        payload = {'page_size': 100}
        url = self.build_url('edge_applications')
        response = self.get(url, params = DEFAULT_PARAMS)
        json = decode_json(response, 200)

        return many_of(EdgeApplication, json['results'])


    def get_edge_application(self, edge_application_id):
        url = self.build_url('edge_applications', edge_application_id)
        response = self.get(url)
        json = decode_json(response, 200)

        return instance_from_data(EdgeApplication, json['results'])


    def edge_functions(self):
        payload = {'page_size': 100}
        url = self.build_url('edge_functions')
        response = self.get(url, params = DEFAULT_PARAMS)
        json = decode_json(response, 200)

        return many_of(EdgeFunction, json['results'])


    def get_edge_function(self, edge_function_id):
        url = self.build_url('edge_functions', edge_function_id)
        response = self.get(url)
        json = decode_json(response, 200)

        return instance_from_data(EdgeFunction, json['results'])


    def debugIfEnabled(self, flag):
        if flag:
            import logging
            logging.basicConfig(level=logging.DEBUG)
