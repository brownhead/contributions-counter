import requests

def get_user(user):
    """
    Returns the raw HTML of a user's profile as a unicode string.

    """

    r = requests.get("https://github.com/%s" % (user, ))
    if not isinstance(r.text, unicode):
        return unicode(r.text, r.encoding)
    else:
        return r.text
