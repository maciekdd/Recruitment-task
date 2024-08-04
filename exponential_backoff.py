import time
from requests.exceptions import RequestException
from typing import Callable, Any

class ExponentialBackoff:
    def __init__(self, base_delay: int = 1, factor: int = 2, max_delay: int = 8, max_retries: int = 10) -> None:
        """
        Initialize the exponential backoff strategy.
        """
        self.base_delay = base_delay
        self.factor = factor
        self.max_delay = max_delay
        self.max_retries = max_retries

    def execute(self, func: Callable[[], Any]) -> Any:
        """
        Execute a function with exponential backoff strategy.
        """
        delay = self.base_delay
        retries = 0
        while retries < self.max_retries:
            try:
                return func()
            except RequestException as e:
                print(f"Request failed: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
                delay = min(delay * self.factor, self.max_delay)
                retries += 1
        raise RequestException("Max retries exceeded")
