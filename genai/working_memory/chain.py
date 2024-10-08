class ReActChain():
    """Single ReAct (Reasoning and Acting) unit of agent scratchpad.

    Args:
        summary (str): The produced summary for the current chain
        thought (str): The produced thought for the current chain
        action (str): The produced action for the current chain
        observation (str): The resulting observation for the current chain
        error (str, optional): The error message in case of agent failure. 
            Defaults to 'None'.

    Attributes:
        summary (str): The produced summary for the current chain.
        thought (str): The produced thought for the current chain.
        action (str): The produced action for the current chain.
        observation (str): The resulting observation for the current chain.
        error (str): The error message in case of agent failure.

    Methods:
        format: Create a ReActChain instance with optional parameters.
        to_str: Convert the ReActChain to a formatted string representation.
        to_messages: Convert the ReActChain to a list of message dictionaries.
        to_log: Convert the ReActChain to a dictionary for JSON-formatted output.
    """

    def __init__(self, summary: str, thought: str, action: str, observation: str, error: str = 'None'):
        self.summary = summary  # The produced summary for the current chain
        self.thought = thought  # The produced thought for the current chain
        self.action = action  # The produced action for the current chain
        self.observation = observation  # The resulting observation for the current chain
        self.error = error  # The error message in case of agent failure

    @classmethod
    def format(cls, summary='', thought='', action='', observation='', error='None'):
        """Create a ReActChain instance with optional parameters.

        Args:
            summary (str, optional): The produced summary for the current chain. 
                Defaults to ''.
            thought (str, optional): The produced thought for the current chain. 
                Defaults to ''.
            action (str, optional): The produced action for the current chain. 
                Defaults to ''.
            observation (str, optional): The resulting observation for the current 
                chain. Defaults to ''.
            error (str, optional): The error message in case of agent failure. 
                Defaults to 'None'.

        Returns:
            ReActChain: A new instance of the ReActChain class.
        """
        return cls(
            summary=summary,
            thought=thought,
            action=action,
            observation=observation,
            error=error
        )

    def to_str(self):
        """Convert the ReActChain to a formatted string representation.

        Returns:
            str: A string representation of the ReActChain, including thought, 
                action, and observation.
        """
        # Correct format for action
        action = self.action
        tool = action.__class__.__name__

        # Get the thought as first item of the chain
        text = f'Thought: {self.thought}\n'

        # Format the action as second item of the chain
        if self.action == '':
            text += f'Action: \n'
        else:
            text += f'Action: {tool}({action})\n'

        # Get the observation as last item of the chain
        text += f'Observation: {self.observation}\n'

        return text

    def to_messages(self):
        """Convert the ReActChain to a list of message dictionaries.

        Returns:
            list: A list of two dictionaries representing assistant and user messages.
        """
        # Correct format for action
        action = self.action
        tool = action.__class__.__name__

        # Format assistant and user messages
        if self.action == '':
            assistant_msg = f'Thought: {self.thought}\nAction: '
        else:
            assistant_msg = f'Thought: {self.thought}\nAction: {tool}({action})'
        user_msg = f'Observation: {self.observation}'

        # Build messages
        messages = [
            {'role': 'assistant', 'content': assistant_msg},
            {'role': 'user', 'content': user_msg}
        ]

        return messages

    def to_log(self):
        """Convert the ReActChain to a dictionary for JSON-formatted output.

        Returns:
            dict: A dictionary containing thought, action, observation, summary, 
                and error information.
        """
        # Correct format for action
        action = self.action
        tool = action.__class__.__name__

        # Get all the items as dict for JSON-formatted output
        obj = {
            'thought': f'Thought: {self.thought}',
            'action': f'Action: {tool}({action})',
            'observation': f'Observation: {self.observation}',
            'summary': f'Summary: {self.summary}',
            'error': f'Error: {self.error}'
        }

        return obj
