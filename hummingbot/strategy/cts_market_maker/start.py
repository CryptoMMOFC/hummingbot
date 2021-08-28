from hummingbot.strategy.market_trading_pair_tuple import MarketTradingPairTuple
from hummingbot.strategy.cts_market_maker import CTSMarketMaker
from hummingbot.strategy.cts_market_maker.cts_market_maker_config_map import cts_market_maker_config_map as c_map


def start(self):
    connector = c_map.get("connector").value.lower()
    market = c_map.get("market").value

    self._initialize_markets([(connector, [market])])
    base, quote = market.split("-")
    market_info = MarketTradingPairTuple(self.markets[connector], market, base, quote)
    self.market_trading_pair_tuples = [market_info]

    self.strategy = CTSMarketMaker(market_info)
