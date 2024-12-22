from random import shuffle as random_shuffle
from product.model import Product
from market.model import Market
from agent.model import RandomAgent, TrendAgent, AntiTrendAgent, ClintellAgent
from agent.vars.actions import ( 
    BUY as AGENT_ACTION_BUY,
    SELL as AGENT_ACTION_SELL
)
from agent.vars.types import CUSTOM as AGENT_TYPE_CUSTOM
import csv

def create_agents(agent_class, count):
    return [agent_class() for _ in range(count)]

def main():
    # Number of simulation loops
    LOOP = 1000
    # Selected product ID
    SELECTED_PRODUCT = "GC1"

    # Number of agents of each type
    AGENT_COUNTS = {
        RandomAgent: 51,
        TrendAgent: 24,
        AntiTrendAgent: 24,
        ClintellAgent: 1
    }

    print('[INFO] Starting...')

    print('[INFO] Creating products...')
    # Create a list of products
    PRODUCTS = [
        Product(
            product_id="GC1",
            name="graphicCard",
            stock=100000,
            buy_tax=5,
            sell_tax=5,
            price=200
        )
    ]

    print('[INFO] Creating market...')
    # Initialize the market with the products
    market = Market(PRODUCTS)

    print('[INFO] Creating agents...')
    # Create a list of agents
    total_agents = []
    for agent_class, count in AGENT_COUNTS.items():
        total_agents.extend(create_agents(agent_class, count))
    
    # Shuffle the agents list
    random_shuffle(total_agents)
    # Set order for each agent
    for index, agent in enumerate(total_agents):
        agent.set_order(index + 1)

    # Get the selected product from the market
    product = market.get_item(SELECTED_PRODUCT)
    # Simulation loop
    for fase in range(LOOP):
        for agent in total_agents:
            # Agent decides action based on the product
            action = agent.decide_action(product)

            # Agent performs the trade action
            if agent.trade(action, product):
                if action == AGENT_ACTION_BUY:
                    product.buy()
                elif action == AGENT_ACTION_SELL:
                    product.sell()
        
        # Save the current price of the product
        product.save_price()

    # Print the final state of each agent
    for agent in total_agents:
        print('[RESULT]', agent.order, agent.agent_type, agent.balance, agent.inventory)
        if agent.agent_type == AGENT_TYPE_CUSTOM:
            with open('profit_clintellagent.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([agent.agent_type, agent.balance, agent.inventory.get(SELECTED_PRODUCT, {}).get('stock', 0)])

if __name__ == "__main__":
    main()