# Python Developer Recruitment Task

## Usage

### Install the required libraries
```bash
pip install -r requirements.txt
```

### Run the script
```bash
python main.py
```
#### Example Response
```
Total products: 204
Products in each category:
Pet Supplies: 27
Electronics: 19
Toys & Games: 21
Outdoor Equipment: 17
Office Supplies: 15
Sports Gear: 17
Fashion: 20
Automotive: 21
Home Appliances: 22
Health & Wellness: 25
Most expensive product in Fashion: 187 - Pulsar Gadget
Average price of Toys & Games products: 38463.45 PLN
```

### Run tests
```bash
pytest
```

## Exponential Backoff

In case of issues with accessing the HTTP service (e.g., 503 status code), the script uses the `ExponentialBackoff` class, which implements an exponential backoff retry strategy.

### Adjusting Parameters

The parameters of the exponential backoff strategy can be adjusted based on the service's characteristics to optimize the waiting time and the number of retries. The default parameters are:

- **base_delay**: Initial delay in seconds (default is 1 second).
- **factor**: Multiplier to increase the delay after each failed attempt (default is 2).
- **max_delay**: Maximum delay in seconds (default is 8 seconds).
- **max_retries**: Maximum number of retries (default is 10).

Example of adjusting the parameters:
```python
backoff_strategy = ExponentialBackoff(base_delay=2, factor=3, max_delay=10, max_retries=5)
```

### Measuring Response Times

To optimally adjust the exponential backoff parameters, you can measure the service's response times and the frequency of 503 errors. Based on this data, you can select appropriate values for `base_delay`, `factor`, `max_delay`, and `max_retries` to minimize waiting time and the number of retries while increasing the script's reliability.