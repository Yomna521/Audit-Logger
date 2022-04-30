"""
    For testing purposes:
        Defining a basic user key for authentication
"""
import base64


class User:

    key = ''

    def set_auth(self, username, password):
        """
        Creates a key based on username and password
        :param username: str
        :param password: str
        :return: None
        """
        self.key = base64.b64encode(
            bytes('%s:%s' % (username, password), 'utf-8')).decode('ascii')

    def get_auth_key(self):
        """
        Returns user's key
        :return: key
        """
        return self.key


def user_key():
    """
    Creates a user's key for a user with username: "yomna" and password: "auditlogger"
    :return: key
    :rtype: str
    """
    user = User()
    # username and password
    user.set_auth('yomna', 'auditlogger')
    return user.get_auth_key()
