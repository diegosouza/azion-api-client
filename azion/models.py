import pendulum
import logging

import azion.exceptions as exceptions


def instance_from_data(model, data):
    if not data:
        return None
    return model(data)


def many_of(model, data):
    if not data:
        return []
    return [instance_from_data(model, resource) for
            resource in data]


def decode_json(response, excepted_status_code):
    """Decode a JSON response.
    """

    # Bad request is interpreted as a falsey value.
    # So we compare it with `None`.
    if response is None:
        return None

    status_code = response.status_code
    if status_code != excepted_status_code:
        if status_code >= 400:
            raise exceptions.handle_error(response)

    logging.debug("response body: %s", response.json())

    return response.json()


def as_boolean(response, expected_status_code):
    if response:
        if response.status_code == expected_status_code:
            return True
        if response.status_code >= 400:
            raise exceptions.handle_error(response)
    return False


def filter_none(data):
    return {key: value for key, value in list(data.items()) if value is not None}


def to_date(date):
    """Convert a string to a datetime object.
    """
    return pendulum.parse(date)


class Token(object):
    """Model representing the authorized token retrieved
    from the API.
    """

    def __init__(self, data):
        self.value = data['token']
        self.created_at = to_date(data['created_at'])
        self.expires_at = to_date(data['expires_at'])

    def __repr__(self):
        return '<TokenAuth [{}]>'.format(self.value[:6])


class Configuration(object):
    """Model representing the configuration retrieved
    from the API.
    """

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.domain_name = data['domain_name']
        self.active = data['active']
        self.delivery_protocol = data['delivery_protocol']
        self.digital_certificate = data['digital_certificate']
        self.cname = data['cname']
        self.cname_access_only = data['cname_access_only']
        self.rawlogs = data['rawlogs']
        try:
            self.application_aceleration = data['application_aceleration']
        except (NameError, KeyError):
            self.application_aceleration = None
            pass

    def __repr__(self):
        return '<Configuration [{} ({})]>'.format(self.name,
                                                  self.domain_name)


class ErrorResponses(object):
    """Model representing the error responses configuration
    retrieved from the API.
    """

    def __init__(self, data):
        self.configuration_id = data['id']
        self.cache_error_400 = data['cache_error_400']
        self.cache_error_403 = data['cache_error_403']
        self.cache_error_404 = data['cache_error_404']
        self.cache_error_405 = data['cache_error_405']
        self.cache_error_414 = data['cache_error_414']
        self.cache_error_416 = data['cache_error_416']
        self.cache_error_501 = data['cache_error_501']

    def __repr__(self):
        return '<ErrorResponses [{}]>'.format(self.configuration_id)


class CacheSettings(object):
    """Model representing the cache settings configuration
    retrieved from the API.
    """

    def __init__(self, data):
        self.name = data['name']
        self.browser_cache_settings = data['browser_cache_settings']
        self.browser_cache_settings_maximum_ttl = data['browser_cache_settings_maximum_ttl']
        self.cdn_cache_settings = data['cdn_cache_settings']
        self.cdn_cache_settings_maximum_ttl = data['cdn_cache_settings_maximum_ttl']
        self.cache_by_query_string = data['cache_by_query_string']
        self.query_string_fields = data['query_string_fields']
        self.enable_query_string_sort = data['enable_query_string_sort']
        self.cache_by_cookies = data['cache_by_cookies']
        self.cookie_names = data['cookie_names']
        self.adaptive_delivery_action = data['adaptive_delivery_action']
        self.device_group = data['device_group']
        try:
            self.id = data['id']
        except (NameError, KeyError):
            pass
        try:
            self.enable_caching_for_post = data['enable_caching_for_post']
        except (NameError, KeyError):
            pass

    def __repr__(self):
        return '<CacheSettings [{} ({})]>'.format(self.name,
                                                  self.id)


class Rule(object):
    """Model representing the rule from rules engine
    configuration retrieved from the API.
    """

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.phase = data['phase']
        self.criteria = data['criteria']
        self.behaviors = data['behaviors']
        self.order = data['order']

    def __repr__(self):
        return '<Rule [{} ({})]>'.format(self.name,
                                         self.id)

class Domain(object):
    """Model representing the domain
    retrieved from the API.
    """

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cnames = data['cnames']
        self.edge_application_id = data['edge_application_id']
        self.is_active = data['is_active']

    def __repr__(self):
        return '<Domain [{} ({})]>'.format(self.name,
                                         self.id)

class EdgeApplication(object):
    """Model representing the edge application
    retrieved from the API.
    """

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.active = data['active']
        # TODO: implement the rest
        # self.origins = []

    def __repr__(self):
        return '<EdgeApplication [{} ({})]>'.format(self.name,
                                         self.id)

class Origin(object):
    """Model representing the edge application origin
    retrieved from the API.
    """

    def __init__(self, data):
        self.id = data['origin_id']
        self.key = data['origin_key']
        self.name = data['name']
        self.addresses = data['addresses']
        self.host_header = data['host_header']

    def __repr__(self):
        return '<Origin [{} ({})]>'.format(self.name,
                                         self.key)

class EdgeFunction(object):
    """Model representing the edge function
    retrieved from the API.
    """

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.code = data['code']
        self.active = data['active']
        self.language = data['language']
        self.modified = data['modified']
        self.json_args = data['json_args']
        self.last_editor = data['last_editor']
        self.initiator_type = data['initiator_type']
        self.reference_count = data['reference_count']

    def __repr__(self):
        return '<EdgeFunction [{} ({})]>'.format(self.name,
                                         self.id)
