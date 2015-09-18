import poplib
import email


class Mailbox():
    pop_conn = None
    user = None
    password = None
    server = None

    def __init__(self, user, password, server):
        self.user = user
        self.password = password
        self.server = server


    def connect(self):
        self.pop_conn = poplib.POP3_SSL(self.server)
        self.pop_conn.user(self.user)
        self.pop_conn.pass_(self.password)

    def get_messages(self):
        full_messages = [self.pop_conn.top(i, 100000) for i in range(1, len(self.pop_conn.list()[1]) + 1)]
        messages = []
        for full_message in full_messages:
            parts = []
            for message_part in full_message[1]:
                parts.append(message_part.decode('utf-8'))
            messages.append("\n".join(parts))

        messages = [email.message_from_string(msg) for msg in messages]
        return messages

    def close(self):
        self.pop_conn.quit()

    def get_message_data(self, message):
        z = message.get_payload(1)
        return z.get_payload(decode=True)
