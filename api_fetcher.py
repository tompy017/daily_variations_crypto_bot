import requests

from coin import Coin


class ApiFetcher:
    BASE_URL = "https://api.coingecko.com/api/v3/coins/"
    PARAMETERS = "?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false"

    def get_coin(self, coin_name: str) -> Coin:
        """Makes a request to coingecko api to get a coin's data.
        :param coin_name : The name of the coin to fetch.
        :return: Coin: new coin object.
        """
        api_url = self.get_api_url(coin_name)

        try:  # get request
            response = requests.get(api_url)

            if response.status_code == 200:
                coin_data = response.json()                     # CONVERTS JSON TO DICT
                coin = self.convert_data_to_coin(coin_data)     # CONVERTS DICT TO COIN
                return coin

            else:  # status code not 200
                print(
                    f"Get request error for {coin_name}"
                    f"\nURL: {api_url}"
                    f"\nstatus code: {response.status_code}"
                )

        except requests.RequestException as e:
            print(f"Error on fetching data for {coin_name}: {str(e)}")

    def get_api_url(self, coin_name: str) -> str:
        """ Adds the name of the coin to construct the url to make the get request
        """
        api_url = f"{self.BASE_URL}{coin_name}{self.PARAMETERS}"
        return api_url

    def convert_data_to_coin(self, coin_data: dict) -> Coin:
        """Returns a Coin object from a dictionary with the required data
        """
        # Get the data needed to create a Coin
        name = coin_data['name']
        symbol = coin_data['symbol'].upper()
        current_price = coin_data['market_data']['current_price']['usd']
        price_change_24h = coin_data['market_data']['price_change_24h']
        price_change_percentage_24h = coin_data['market_data']['price_change_percentage_24h']
        # Create the coin
        coin = Coin(
            name=name,
            symbol=symbol,
            current_price=current_price,
            price_change_24h=price_change_24h,
            price_change_percentage_24h=price_change_percentage_24h
        )
        return coin
