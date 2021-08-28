from decimal import Decimal

from hummingbot.client.config.config_var import ConfigVar
from hummingbot.client.config.config_validators import (
    validate_decimal,
    validate_int
)

# Returns a market prompt that incorporates the connector value set by the user


def market_prompt() -> str:
    connector = cts_market_maker_config_map.get("connector").value
    return f'Enter the token trading pair on {connector} >>> '


# List of parameters defined by the strategy
cts_market_maker_config_map = {
    "strategy":
        ConfigVar(key="strategy",
                  prompt="",
                  default="cts_mm",
                  ),
    "connector":
        ConfigVar(key="connector",
                  prompt="Enter the name of the exchange >>> ",
                  prompt_on_new=True,
                  ),
    "market":
        ConfigVar(key="market",
                  prompt=market_prompt,
                  prompt_on_new=True),
    "gamma":
        ConfigVar(key="gamma",
                  prompt="Enter Inventory risk aversion parameter. ",
                  type_str="decimal",
                  validator=lambda v: validate_decimal(v, -10, 10, inclusive=True),
                  default=Decimal("0.2")),
    "limit":
        ConfigVar(key="limit",
                  prompt="Maximum number of entries to grab from database.",
                  type_str="int",
                  default=1,
                  validator= lambda v: validate_int(v, 0)),
    "k":
        ConfigVar(key="k",
                  prompt="Orderbook depth parameter",
                  type_str="float",
                  validator=lambda v: validate_decimal(v, 0, inclusive=False),
                  default=1),
    "eta":
        ConfigVar(key="eta",
                  prompt=" Inventory management parameter",
                  type_str="float",
                  validator=lambda v: validate_decimal(v, 0, inclusive=False),
                  default=1),
    "sigma":
        ConfigVar(key="sigma",
                  prompt="Volatility-related parameter",
                  type_str="float",
                  validator=lambda v: validate_decimal(v, 0, inclusive=False),
                  default=1),
    "win":
        ConfigVar(key="win",
                  prompt="Size of window to use, in minutes.",
                  type_str="int",
                  validator=lambda v: validate_int(v, 0),
                  default=1),
    "ret_gap":
        ConfigVar(key="ret_gap",
                  prompt="Size of interval on which to compute returns, in minutes",
                  type_str="int",
                  validator=lambda v: validate_int(v, 0),
                  default=1),
    "mu":
        ConfigVar(key="mu",
                  prompt="Current approximation of asset drift",
                  type_str="float",
                  validator=lambda v: validate_decimal(v, 0, inclusive=False),
                  default=1)
}

"""
        # "q_max" : float
        #    Maximum trade size.
        # "Q" : float
        #    Maximum amount of inventory possible.
"""
