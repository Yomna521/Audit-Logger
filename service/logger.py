from datetime import datetime

class AuditLogger:
    """
        AuditLogger class defines an audit logger service for client systems

        Attributes:
            http_request: dict
                Args:
                  <method> str: POST or GET methods
                  <client> tuple: Client address in the form of (host, port)
                  <query>str [OPTIONAL]: For GET methods to provide the query

            event: dict
                The event log sent by client system
    """

    def __init__(self) -> None:
        self.http_request: dict = None
        self.event: dict = ''

    def set_http_request(self, method: str, client: tuple, query: dict = None) -> 'AuditLogger':
        self.http_request = {
            'timestamp of request': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'method': method,
            'client address': client,
            'query': query
        }
        return self

    def set_event(self, event: json) -> 'AuditLogger':
        self.event = event
        return self
