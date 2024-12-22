from .vars.types import BASE, RANDOM, TREND, ANTITREND, CUSTOM
from .vars.actions import BUY, SELL, NOTHING
from random import choices as random_choices

class BaseAgent:
    """
    Represents a base agent with common functionalities for different agent types.
    """

    VALID_AGENT_TYPES = {BASE, RANDOM, TREND, ANTITREND, CUSTOM}
    ACTIONS = {BUY, SELL, NOTHING}

    def __init__(self, agent_type=BASE):
        """
        Initializes a new base agent instance.
        """
        if agent_type not in self.VALID_AGENT_TYPES:
            raise ValueError(f"[ERROR] Invalid agent_type: {agent_type}")
        
        self.agent_type = agent_type
        self.balance = 1000
        self.inventory = {}
        self.order = 0
        print(f'[INFO] Created agent {self.agent_type} with {self.balance} balance and {self.inventory}')

    def set_order(self, number):
        """
        Sets the order number for the agent.
        """
        self.order = number

    def decide_action(self, *args, **kwargs):
        """
        Decides the action to be taken by the agent.
        """
        action = NOTHING
        print(f'[INFO] Agent ({self.agent_type}) decide {action}')
        return action

    def can_trade(self, action, product):
        """
        Checks if the agent can perform the given trade action on the product.
        """
        BUY_REQUIREMENTS = [self.balance > product.price]
        SELL_REQUIREMENTS = [product.id in self.inventory and self.inventory[product.id]['stock'] > 0]
        if action == BUY:
            return all(BUY_REQUIREMENTS)
        elif action == SELL:
            return all(SELL_REQUIREMENTS)

    def trade(self, action, product):
        """
        Executes the trade action on the product.
        """
        if self.can_trade(action, product):
            if action == BUY:
                self.balance -= product.price
                if product.id in self.inventory:
                    self.inventory[product.id]['stock'] += 1
                else:
                    self.inventory[product.id] = { 'stock': 1 } 

                return True

            elif action == SELL:
                self.inventory[product.id]['stock'] -= 1
                self.balance += product.price
                
                return True
    
    def autotrade(self, product, **kwargs):
        """
        Automatically decides and executes a trade action on the product.
        """
        action = self.decide_action(**kwargs)
        return self.trade(action, product, product)

class RandomAgent(BaseAgent):
    """
    Represents an agent that makes random trade decisions.
    """

    def __init__(self):
        """
        Initializes a new random agent instance.
        """
        super().__init__(RANDOM)

    def decide_action(self, *args, **kwargs):
        """
        Decides a random action to be taken by the agent.
        """
        from random import choice as random_choice
        action = random_choice(list(self.ACTIONS))
        print(f'[INFO] Agent ({self.agent_type}) decide {action}')
        return BUY

class TrendAgent(BaseAgent):
    """
    Represents an agent that makes trade decisions based on market trends.
    """

    def __init__(self):
        """
        Initializes a new trend agent instance.
        """
        super().__init__(TREND)

    def decide_action(self, product, *args, **kwargs):
        """
        Decides an action based on the trend of the product's price.
        """
        difference = product.price - product.last_price
        percentage_difference = (difference / product.last_price) * 100

        if percentage_difference >= 1:
            action = random_choices([BUY, NOTHING], weights=[75, 25])[0]
        else:
            action = random_choices([SELL, NOTHING], weights=[20, 80])[0]

        print(f'[INFO] Agent ({self.agent_type}) decide {action}')
        return action

class AntiTrendAgent(BaseAgent):
    """
    Represents an agent that makes trade decisions against market trends.
    """

    def __init__(self):
        """
        Initializes a new anti-trend agent instance.
        """
        super().__init__(ANTITREND)

    def decide_action(self, product, *args, **kwargs):
        """
        Decides an action based on the anti-trend of the product's price.
        """
        difference = product.price - product.last_price
        percentage_difference = (difference / product.last_price) * 100

        if percentage_difference <= -1:
            action = random_choices([BUY, NOTHING], weights=[75, 25])[0]
        else:
            action = random_choices([SELL, NOTHING], weights=[20, 80])[0]

        print(f'[INFO] Agent ({self.agent_type}) decide {action}')
        return action

class ClintellAgent(BaseAgent):
    """
    Represents a custom agent with specific trading strategies.
    """

    def __init__(self):
        """
        Initializes a new Clintell agent instance.
        """
        super().__init__(CUSTOM)
        self.STRATEGIES_POSITION = [40, 60, 100]
        self.strategy = None
        self.last_price_bought = None

    def __strategy_on_start(self, product):
        """
        Strategy to be executed at the start of trading.
        """
        difference = product.price - product.last_price
        percentage_difference = (difference / product.last_price) * 100

        if percentage_difference >= 1:
            action = random_choices([BUY, NOTHING], weights=[75, 25])[0]
        else:
            action = random_choices([SELL, NOTHING], weights=[20, 80])[0]

        print(f'[INFO] Agent ({self.agent_type}) decide {action}')
        return action

    def __strategy_on_middle(self, product):
        """
        Strategy to be executed in the middle of trading.
        """
        difference = product.price - product.last_price
        percentage_difference = (difference / product.last_price) * 100

        if percentage_difference >= 1:
            action = random_choices([BUY, NOTHING], weights=[60, 40])[0]
        else:
            action = random_choices([SELL, NOTHING], weights=[30, 70])[0]

        print(f'[INFO] Agent ({self.agent_type}) decide {action}')
        return action

    def __strategy_on_end(self, product):
        """
        Strategy to be executed at the end of trading.
        Ensures that the agent has 0 graphic cards.
        """
        if product.id in self.inventory and self.inventory[product.id]['stock'] > 0:
            action = SELL
        else:
            action = NOTHING

        print(f'[INFO] Agent ({self.agent_type}) decide {action}')
        return action

    def decide_strategy(self):
        """
        Decides the trading strategy based on the order number.
        """
        for number in self.STRATEGIES_POSITION:
            self.strategy = number
            if self.order > number:
                break

    def decide_action(self, product):
        """
        Decides an action based on the current strategy.
        """
        if not self.strategy:
            self.decide_strategy()

        action = NOTHING
        if self.strategy == self.STRATEGIES_POSITION[0]:
            action = self.__strategy_on_start(product)
        elif self.strategy == self.STRATEGIES_POSITION[1]:
            action = self.__strategy_on_middle(product)
        elif self.strategy == self.STRATEGIES_POSITION[2]:
            action = self.__strategy_on_end(product)

        return action
