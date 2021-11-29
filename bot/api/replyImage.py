def messageImage(url):
    card_message = [
        {
            "type": "card",
            "theme": "secondary",
            "size": "lg",
            "modules": [
                {
                    "type": "container",
                    "elements": [
                        {
                            "type": "image",
                            "src": url
                        }
                    ]
                }
            ]
        }
    ]
    return card_message
