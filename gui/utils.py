from card import Card, Pip, Suit
from game import GameVariant


def sorted_cards(cards, game_variant: GameVariant):
    # For easier display: sort all cards in descending order, starting with Trump.

    # If no game has been selected (yet), sort as if expecting a Herz-solo (same as any Rufspiel).
    if game_variant is None:
        game_variant = GameVariant(GameVariant.Contract.suit_solo, trump_suit=Suit.herz)

    def sort_key(card: Card):
        key = 0
        # Suit - start with Trump
        is_trump = game_variant.is_trump(card)
        if is_trump:
            key = 1000
        if is_trump and card.pip == Pip.ober:
            key += 500
        if is_trump and card.pip == Pip.unter:
            key += 400

        if card.suit == Suit.eichel:
            key += 30
        elif card.suit == Suit.gras:
            key += 20
        elif card.suit == Suit.herz:
            key += 10

        # Pip
        if card.pip == Pip.sau:
            key += 7
        elif card.pip == Pip.zehn:
            key += 6
        elif card.pip == Pip.koenig:
            key += 5
        elif card.pip == Pip.ober:  # Non-trump ober, for example during Wenz
            key += 4
        elif card.pip == Pip.unter:  # Non-trump unter
            key += 3
        elif card.pip == Pip.neun:
            key += 2
        elif card.pip == Pip.acht:
            key += 1
        elif card.pip == Pip.sieben:
            key += 0

        return key

    return sorted(cards, key=sort_key, reverse=True)