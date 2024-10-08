from pydantic import Field, BaseModel
from typing import List
from .chain import ReActChain


class ReActScratchpad(BaseModel):
    """Agent working memory as a collection of ReAct chains.

    This class represents a collection of ReAct chains, providing methods to
    manipulate and retrieve the stored information in various formats.

    Attributes:
        steps (List[BaseModel]): A list of ReAct chains representing the steps
            of the reasoning process.

    Methods:
        to_text(): Converts the scratchpad content to a string representation.
        to_messages(last): Converts the scratchpad content to a list of messages.
        to_log(): Converts the scratchpad content to a list of logs.
        to_json(): Converts the scratchpad content to a JSON-compatible dictionary.
        update(item): Adds a new ReAct chain to the scratchpad.
    """
    steps: List[BaseModel] = Field(default_factory=list)

    def to_text(self):
        """Converts the scratchpad content to a string representation.

        Returns:
            str: A string representation of all ReAct chains in the scratchpad,
                 with each chain separated by a newline.
        """
        text = '\n'
        for chain in self.steps:
            text += chain.to_str()
        return text

    def to_messages(self, last: int = None):
        """Converts the scratchpad content to a list of messages.

        Args:
            last (int, optional): Number of the last execution steps to include.
                If None, all steps are included. Defaults to None.

        Returns:
            List[dict]: A list of message dictionaries, each representing a step
                in the ReAct chain.
        """
        messages = []
        if last == None:
            last = len(self.steps)
        else:
            last = min(last, len(self.steps))

        for chain in self.steps[-last:]:
            messages += chain.to_messages()

        return messages

    def to_log(self):
        """Converts the scratchpad content to a list of logs.

        Returns:
            List[dict]: A list of dictionaries, each representing a log entry
                for a single execution step in the ReAct chain.
        """
        logs = []
        for chain in self.steps:
            logs.append(chain.to_log())

        return logs

    def to_json(self):
        """Converts the scratchpad content to a JSON-compatible dictionary.

        Returns:
            dict: A dictionary representation of the scratchpad, currently
                containing an empty 'scratchpad' list. This method may need
                to be implemented further to include actual content.
        """
        objs = {'scratchpad': []}

        return objs

    def update(self, item: ReActChain):
        """Adds a new ReAct chain to the scratchpad.

        Args:
            item (ReActChain): The ReAct chain to be added to the scratchpad.
        """
        self.steps.append(item)
