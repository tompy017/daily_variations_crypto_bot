from coin import Coin
from api_fetcher import ApiFetcher


bitcoin = Coin("bitcoin", "btc", 50_000, 500, 0.1)

print(bitcoin)


api_fetcher = ApiFetcher()
#print(api_fetcher.get_coin("bitcoin"))

new_coin = api_fetcher.get_coin("bitcoin")
print(new_coin)
#
# eth = api_fetcher.get_data("ethereum")
# print(eth)