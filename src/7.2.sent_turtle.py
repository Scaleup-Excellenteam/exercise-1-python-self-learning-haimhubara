"""
PostOffice class that allows users to send, receive, and search messages.

This class simulates a simple postal system where users can send messages to each other.
Each user has an inbox, and the system supports sending urgent messages, reading messages,
and searching for messages by specific terms.

Classes:
    PostOffice: Manages user inboxes and message sending/receiving operations.

Functions:
    __init__(self, usernames):
        Initializes the PostOffice with a list of users and their inboxes.

    send_message(self, sender, recipient, message_body, urgent=False):
        Sends a message from one user to another, with the option to mark it as urgent.

    read_inbox(self, username, num_messages=None):
        Reads the user's inbox, marking messages as read. Optionally, a number of messages can be specified.

    search_inbox(self, username, search_term):
        Searches for messages in the user's inbox containing the specified search term.
"""


class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        if recipient not in self.boxes:
            raise KeyError(f"Recipient {recipient} does not exist.")

        user_box = self.boxes[recipient]
        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'read': False,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, num_messages=None):
        """Read the user's inbox and mark messages as read.

        :param str username: The user's inbox to read.
        :param num_messages: The number of messages to return, or None for all.
        :type num_messages: int or None
        :return: A list of messages.
        :rtype: list
        :raises KeyError: if the user does not exist.
        """
        if username not in self.boxes:
            raise KeyError(f"User {username} does not exist.")

        user_box = self.boxes[username]
        unread_messages = [msg for msg in user_box if not msg['read']]

        if num_messages is not None:
            unread_messages = unread_messages[:num_messages]

        for msg in unread_messages:
            msg['read'] = True

        return unread_messages

    def search_inbox(self, username, search_term):
        """Search the inbox for messages containing the search term.

        :param str username: The user's inbox to search.
        :param str search_term: The string to search for.
        :return: A list of matching messages.
        :rtype: list
        :raises KeyError: if the user does not exist.
        """
        if username not in self.boxes:
            raise KeyError(f"User {username} does not exist.")

        user_box = self.boxes[username]
        matching_messages = [msg for msg in user_box if search_term in msg['body'] or search_term in msg['sender']]

        return matching_messages


if __name__ == "__main__":
    po = PostOffice(["alice", "bob"])

    po.send_message("alice", "bob", "Hello, Bob!")
    po.send_message("bob", "alice", "Hi, Alice!", urgent=True)
    po.send_message("alice", "bob", "What are you doing today?")

    print(po.read_inbox("bob", num_messages=2))
    print(po.read_inbox("alice", num_messages=1))
    print(po.search_inbox("bob", "Hello"))
