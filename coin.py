"""Coin class to model a crypto token."""


class Coin:

    def __init__(self, name, symbol, current_price, price_change_24h, price_change_percentage_24h):
        self.name = name
        self.symbol = symbol
        self.current_price = current_price
        self.price_change_24h = price_change_24h
        self.price_change_percentage_24h = price_change_percentage_24h

    def __str__(self) -> str:
        return f"Name: {self.name.title()}" \
               f"\nSymbol: {self.symbol.upper()}" \
               f"\nActual Price: {self.current_price:,.2f} USD" \
               f"\nPrice change (24h): {self.price_change_24h:,.2f} USD" \
               f"\nPrice change % (24h) {self.price_change_percentage_24h:,.2f}%"
