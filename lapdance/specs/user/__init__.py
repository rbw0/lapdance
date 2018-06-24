# -*- coding: utf-8 -*-

from functools import partial

from lapdance.settings import LAPDANCE_LDAP_USER
from lapdance.utils import generate_spec_def
from lapdance.specs.definitions import (
    op_success, op_success_def,
    op_ldap_error, op_ldap_error_def,
    op_error, op_error_def
)

tags = ['users']
user_id_path = {
    'name': 'user_id',
    'in': 'path',
    'type': 'string',
    'required': True,
}

user_body = {
    'type': 'object',
    'name': 'body',
    'required': True,
    'in': 'body',
    'schema': {
        '$ref': '#/definitions/User'
    },
}

get_user_def = partial(generate_spec_def, 'User', LAPDANCE_LDAP_USER)

ldap_operation_spec = {
    'tags': tags,
    'summary': '<Unknown>',
    'parameters': [user_id_path],
    'definitions': {
        **get_user_def(),
        **op_success_def,
        **op_ldap_error_def,
        **op_error_def,
    },
    'responses': {
        '201': op_success,
        '400': op_error,
        '500': op_ldap_error,
    }
}
