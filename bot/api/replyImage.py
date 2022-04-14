from khl.card import Card, CardMessage, Module, Element


def messageImage(url):
    card_message = CardMessage(Card(Module.Container(Element.Image(url))))
    return card_message
