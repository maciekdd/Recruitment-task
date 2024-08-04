import pytest
from requests.exceptions import RequestException
from exponential_backoff import ExponentialBackoff

def test_exponential_backoff():
    """
    Test that ExponentialBackoff raises RequestException after max retries.
    """
    def mock_func() -> None:
        raise RequestException("Mocked exception")

    backoff = ExponentialBackoff(base_delay=0.1, max_delay=0.2, max_retries=3)
    with pytest.raises(RequestException):
        backoff.execute(mock_func)
