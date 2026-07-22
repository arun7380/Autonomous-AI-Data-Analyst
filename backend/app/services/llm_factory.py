import os
from typing import Optional, Any
from app.core.config import settings
from app.core.logger import logger


def get_llm(
    provider: Optional[str] = None,
    model_name: Optional[str] = None,
    temperature: float = 0.0,
    max_tokens: Optional[int] = None,
    **kwargs: Any
) -> Any:
    """
    Factory function to instantiate Chat LLMs for Google Gemini or Groq.
    
    :param provider: 'google', 'gemini', or 'groq'. Defaults to settings.DEFAULT_LLM_PROVIDER.
    :param model_name: Name of the model. Defaults to settings.DEFAULT_MODEL_NAME.
    :param temperature: Sampling temperature (0.0 to 1.0).
    :param max_tokens: Maximum completion tokens.
    :return: An instance of ChatGoogleGenerativeAI or ChatGroq.
    """
    selected_provider = (provider or settings.DEFAULT_LLM_PROVIDER).lower()
    selected_model = model_name or settings.DEFAULT_MODEL_NAME

    if selected_provider in ["google", "gemini"]:
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
        except ImportError:
            raise ImportError(
                "langchain-google-genai package is required for Google Gemini. "
                "Please run 'pip install langchain-google-genai'."
            )
        
        api_key = settings.GOOGLE_API_KEY or os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            logger.warning("GOOGLE_API_KEY is not set in settings or environment variables.")
        
        llm_kwargs = {
            "model": selected_model,
            "temperature": temperature,
            "google_api_key": api_key,
            **kwargs
        }
        if max_tokens:
            llm_kwargs["max_output_tokens"] = max_tokens

        logger.info(f"Instantiating ChatGoogleGenerativeAI (model={selected_model})")
        return ChatGoogleGenerativeAI(**llm_kwargs)

    elif selected_provider == "groq":
        try:
            from langchain_groq import ChatGroq
        except ImportError:
            raise ImportError(
                "langchain-groq package is required for Groq. "
                "Please run 'pip install langchain-groq'."
            )
            
        api_key = settings.GROQ_API_KEY or os.environ.get("GROQ_API_KEY")
        if not api_key:
            logger.warning("GROQ_API_KEY is not set in settings or environment variables.")

        llm_kwargs = {
            "model_name": selected_model,
            "temperature": temperature,
            "groq_api_key": api_key,
            **kwargs
        }
        if max_tokens:
            llm_kwargs["max_tokens"] = max_tokens

        logger.info(f"Instantiating ChatGroq (model={selected_model})")
        return ChatGroq(**llm_kwargs)

    else:
        raise ValueError(
            f"Unsupported LLM provider '{selected_provider}'. "
            "Supported providers are 'google' (or 'gemini') and 'groq'."
        )


def get_embeddings(
    provider: Optional[str] = None,
    model_name: Optional[str] = None,
    **kwargs: Any
) -> Any:
    """
    Factory function to instantiate text embedding models for Google Gemini.
    """
    selected_provider = (provider or settings.DEFAULT_LLM_PROVIDER).lower()
    selected_model = model_name or settings.EMBEDDING_MODEL_NAME

    if selected_provider in ["google", "gemini"]:
        try:
            from langchain_google_genai import GoogleGenerativeAIEmbeddings
        except ImportError:
            raise ImportError(
                "langchain-google-genai package is required for Google embeddings. "
                "Please run 'pip install langchain-google-genai'."
            )
            
        api_key = settings.GOOGLE_API_KEY or os.environ.get("GOOGLE_API_KEY")
        return GoogleGenerativeAIEmbeddings(
            model=selected_model,
            google_api_key=api_key,
            **kwargs
        )
    else:
        raise ValueError(
            f"Embeddings not supported for provider '{selected_provider}'. "
            "Please use 'google' / 'gemini' for embeddings."
        )
