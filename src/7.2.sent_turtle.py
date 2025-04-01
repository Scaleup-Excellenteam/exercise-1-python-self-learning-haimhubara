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

    def send_message(self, sender, recipient, title, message_body, urgent=False):
        """Send a message to a recipient."""
        if recipient not in self.boxes:
            raise KeyError(f"Recipient {recipient} does not exist.")

        user_box = self.boxes[recipient]
        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'read': False,
            'unread': True,
            'title': title,  # Adding title to the message
        }
        if urgent:
            user_box.insert(0, message_details)  # Urgent messages go to the top
        else:
            user_box.append(message_details)  # Normal messages go to the bottom
        return self.message_id

    def read_inbox(self, username, num_messages=None):
        """Read the user's inbox and mark messages as read."""
        if username not in self.boxes:
            raise KeyError(f"User {username} does not exist.")

        user_box = self.boxes[username]
        unread_messages = [msg for msg in user_box if not msg['read']]

        if num_messages is not None:
            unread_messages = unread_messages[:num_messages]

        for msg in unread_messages:
            msg['read'] = True
            msg['unread'] = False  # Marking 'unread' as False after reading

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
        # Searching in the body and title of the message
        matching_messages = [msg for msg in user_box if search_term.lower() in msg['body'].lower() or search_term.lower() in msg['title'].lower()]

        return matching_messages


if __name__ == "__main__":
    po = PostOffice(["alice", "bob"])

    po.send_message("alice", "bob", "Greeting", "Hello, Bob!")
    po.send_message("bob", "alice", "Quick response", "Hi, Alice!", urgent=True)
    po.send_message("alice", "bob", "Plans for today", "What are you doing today?")

    print(po.read_inbox("bob", num_messages=2))  # Reads first 2 messages in Bob's inbox
    print(po.read_inbox("alice", num_messages=1))  # Reads 1 message in Alice's inbox
    print(po.search_inbox("bob", "tomorrow"))  # Search for 'tomorrow' in Bob's inbox
