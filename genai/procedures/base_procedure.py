
class BaseProcedure():
    def __init__(self, llm, prompt_template: str):
        """Base class for defining reasoning procedures using a generative agent (LLM).

        This class provides an interface for reasoning procedures that use a 
        large language model (LLM) to perform various tasks based on a specified 
        prompt template. It serves as a foundation for more specialized procedures 
        that can be implemented by subclassing.

        Args:
            llm (LLMClient): An instance of the LLM client responsible for 
                interacting with the language model.
            prompt_template (str): A string template used to generate the prompts 
                that will be sent to the LLM.

        Attributes:
            llm (LLMClient): The LLM client responsible for executing tasks based 
                on the prompt.
            prompt_template (str): The prompt template that will be formatted and 
                used as input to the LLM.

        Methods:
            run (str): Executes the reasoning procedure.
        """
        self.llm = llm
        self.prompt_template = prompt_template

    def run(self):
        """Executes the reasoning procedure.

        This method must be implemented by any subclass to define how 
        the procedure interacts with the LLM and processes its responses.

        Raises:
            NotImplementedError: This is an abstract method that should be 
                overridden in derived classes.
        """
        raise NotImplementedError
