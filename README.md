# Project Documentation

## Overview
This project simulates a market environment where different types of agents interact with products. The agents make decisions based on various strategies to buy or sell products, affecting the market dynamics.

## File Structure
The project is organized into the following files and directories:

- **/product**: Contains the product-related code.
  - **model.py**: Defines the `Product` class, representing a product with attributes and methods for buying, selling, and saving prices.

- **/market**: Contains the market-related code.
  - **model.py**: Defines the `Market` class, representing a market that manages a collection of products and provides methods to add, update, retrieve, and delete products.

- **/agent**: Contains the agent-related code.
  - **model.py**: Defines various agent classes (`BaseAgent`, `RandomAgent`, `TrendAgent`, `AntiTrendAgent`, `ClintellAgent`) that represent different strategies for interacting with the market.
  - **vars/types.py**: Defines constants for different agent types.
  - **vars/actions.py**: Defines constants for different actions agents can take (BUY, SELL, NOTHING).

- **main.py**: The main entry point of the application, where the market and agents are initialized, and the simulation loop is executed.

## Classes and Functions

### Product Class (`product/model.py`)
- **Product**: Represents a product with attributes such as id, name, stock, buy tax, sell tax, price, and last price.
  - **\_\_init\_\_()**: Initializes a new product instance.
  - **\_\_str\_\_()**: Returns a string representation of the product.
  - **buy()**: Buys the product, decreasing stock and increasing price.
  - **sell()**: Sells the product, increasing stock and decreasing price.
  - **save_price()**: Saves the current price as the last price.

### Market Class (`market/model.py`)
- **Market**: Represents a market containing various items.
  - **\_\_init\_\_()**: Initializes a new market instance with a list of items.
  - **add_item()**: Adds a new item to the market inventory.
  - **get_item()**: Retrieves an item from the market inventory by its id.
  - **update_item()**: Updates attributes of an item in the market inventory.
  - **delete_item()**: Deletes an item from the market inventory by its id.

### Agent Classes (`agent/model.py`)
- **BaseAgent**: Represents a base agent with common functionalities for different agent types.
  - **\_\_init\_\_()**: Initializes a new base agent instance.
  - **set_order()**: Sets the order number for the agent.
  - **decide_action()**: Decides the action to be taken by the agent.
  - **can_trade()**: Checks if the agent can perform the given trade action on the product.
  - **trade()**: Executes the trade action on the product.
  - **autotrade()**: Automatically decides and executes a trade action on the product.

- **RandomAgent**: Represents an agent that makes random trade decisions.
  - **\_\_init\_\_()**: Initializes a new random agent instance.
  - **decide_action()**: Decides a random action to be taken by the agent.

- **TrendAgent**: Represents an agent that makes trade decisions based on market trends.
  - **\_\_init\_\_()**: Initializes a new trend agent instance.
  - **decide_action()**: Decides an action based on the trend of the product's price.

- **AntiTrendAgent**: Represents an agent that makes trade decisions against market trends.
  - **\_\_init\_\_()**: Initializes a new anti-trend agent instance.
  - **decide_action()**: Decides an action based on the anti-trend of the product's price.

- **ClintellAgent**: Represents a custom agent with specific trading strategies.
  - **\_\_init\_\_()**: Initializes a new Clintell agent instance.
  - **decide_strategy()**: Decides the trading strategy based on the order number.
  - **decide_action()**: Decides an action based on the current strategy.

### Constants (`agent/vars/types.py` and `agent/vars/actions.py`)
- **types.py**: Defines constants for different agent types (BASE, RANDOM, TREND, ANTITREND, CUSTOM).
- **actions.py**: Defines constants for different actions agents can take (BUY, SELL, NOTHING).

## Getting Started
To get started with the project, follow these steps:

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Run the main script using `python main.py`.

## Contributing
If you would like to contribute to the project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License.
