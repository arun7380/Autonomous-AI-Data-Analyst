from fastapi import HTTPException, status


class DomainException(Exception):
    """Base domain exception for the application."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class DatasetNotFoundException(DomainException):
    def __init__(self, dataset_id: str):
        super().__init__(f"Dataset with ID '{dataset_id}' was not found.")


class UnsupportedFileFormatException(DomainException):
    def __init__(self, format_name: str):
        super().__init__(f"File format '{format_name}' is not supported.")


class DataProcessingException(DomainException):
    def __init__(self, details: str):
        super().__init__(f"Error occurred during data processing: {details}")


class AgentExecutionException(DomainException):
    def __init__(self, agent_name: str, reason: str):
        super().__init__(f"Agent '{agent_name}' failed execution: {reason}")
