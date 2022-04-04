from UnitTestr.helpers.Sessions.Site import Site
from UnitTestr.helpers.exceptions import SessionKeyTaken


class SessionManager:
    sessions: list[tuple[str, Site]]

    def __init__(self, url=None, key="first"):
        self.sessions = []
        self.new_session(url, key)

    def new_session(self, url=None, key="first"):
        # Appends a new session if the key does not exist, adds url if there is an inputted url
        if not self._session_exists(key):
            return self.sessions.append((key, Site(url if url is not None else None)))
        else:
            raise SessionKeyTaken(key)

    def getSession(self, key="first"):
        session = [session for session in self.sessions if session[0] == key]
        return session[0][1] if session.__len__() == 1 else None

    def _session_exists(self, key="first"):
        session = [session for session in self.sessions if session[0] == key]
        return session.__len__() == 1
