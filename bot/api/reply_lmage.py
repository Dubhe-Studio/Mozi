from khl.card import Card, CardMessage, Module, Element


def MessageImage(url):
    card_message = CardMessage(Card(Module.Container(Element.Image(url))))
    return card_message
