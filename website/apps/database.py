import json

from tinydb import TinyDB, Query

db = TinyDB('website/database/users.json')
User = Query()


def choose_identifier(original):
    def wrapper(**kwargs):
        if kwargs.get('slack_id'):
            kwargs['id_key'] = 'slack_id'
            kwargs['id_value'] = kwargs.get('slack_id')
            del kwargs['slack_id']
        elif kwargs.get('username'):
            kwargs['id_key'] = 'username'
            kwargs['id_value'] = kwargs.get('username')
            del kwargs['username']
        elif kwargs.get('email'):
            kwargs['id_key'] = 'email'
            kwargs['id_value'] = kwargs.get('email')
            del kwargs['email']
        else:
            return 'Please specify email, username or id'

        return original(**kwargs)
    return wrapper


def insert_user(skills='', github='', timezone='', email='', username='', slack_id='', points='0'):
    """ Only apps.invite.py should call it!

    apps.invite confirms email validity, and uniqueness
    """
    data = {"skills": skills, "github": github, "time": timezone, "email": email, "username": username,
            'slack_id': slack_id, "points": points}
    db.insert(data)
    return json.dumps(
        {'ok': True, 'response': db.get(User.email == email)}
    )


@choose_identifier
def update_user(params, id_key, id_value, **_):
    db.update(params, User[id_key] == id_value)
    return json.dumps(
        {'ok': True, 'response': {'id': id_value, 'value': db.get(User[id_key] == id_value)}}
    )


@choose_identifier
def get_user(id_key, id_value, **_):
    resp = db.get(User[id_key] == id_value)
    if resp:
        return json.dumps(
            {'ok': True, 'response': resp}
        )
    else:
        return json.dumps(
            {'ok': False, 'response': {'Error': 'User not found'}}
        )


def get_all_users():
    return json.dumps(
        {'ok': True, 'response': db.all()}
    )


@choose_identifier
def delete_user(id_key, id_value, **_):
    db.remove(User[id_key] == id_value)
    return json.dumps(
        {'ok': True, 'response': {'id': id_value}}
    )

if __name__ == '__main__':
    pass
