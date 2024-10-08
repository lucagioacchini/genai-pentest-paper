from typing import Dict, Any, Type
from pydantic import BaseModel, Field
from .base_procedure import BaseProcedure
from ..working_memory import ReActChain


class ThoughtModel(BaseModel):
    thought: str = Field(..., title='thought')

    class Config:
        @staticmethod
        def json_schema_extra(schema: Dict[str, Any], model: Type['ThoughtModel']) -> None:
            for prop in schema.get('properties', {}).values():
                prop.pop('title', None)


class ThoughtProcedure(BaseProcedure):
    """A reasoning procedure that invokes the LLM to produce a thought on a task.

    This class extends the BaseProcedure to handle reasoning and thought production. 
    It leverages the last agent execution step and the task-oriented summary of 
    the agent scratchpad to produce a thought on the next action using the LLM.

    Args:
        llm (LLMClient): The LLM client responsible for executing tasks based 
            on the prompt.
        prompt_template (str): The prompt template that will be formatted and 
            used as input to the LLM.

    Attributes:
        llm (LLMClient): The LLM client responsible for executing tasks based 
            on the prompt.
        prompt_template (str): The prompt template that will be formatted and 
            used as input to the LLM.

    Methods:
        run(summary, last_step): Generates a thought on the next action based 
            on the given inputs using the LLM.
    """

    def run(self, summary: str, last_step: ReActChain):
        """Execute the summary reasoning procedure based on the current task and
        agent scratchpad

        Args:
            summary (str): The produced summary for the current chain.
            last_step (ReActChain): The last step in the reasoning chain, 
                representing the agent's prior thought process.

        Returns:
            ThoughtModel: The ThoughtModel formatted by the LLM
        """
        # Format the prompt
        prompt = self.prompt_template.format(
            summary=summary,
            last_step=last_step.to_str()
        )

        # Invoke LLM
        llm_out = self.llm.invoke(
            response_model=ThoughtModel,
            system_prompt=prompt,
            messages=[]
        )

        return llm_out
