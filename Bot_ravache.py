print("Olá tudo bem? Aqui é a Ravache, como posso te ajudar?")

def responder(mensagem):
    mensagem = mensagem.lower()

    if "promoção" in mensagem or "promoções" in mensagem:
        return "Hoje temos dose dupla de caipirinha!"

    elif "cardápio" in mensagem or "cardapio" in mensagem:
        return "Nosso cardápio é variado com hambúrgueres, porções e bebidas."

    elif (
        "barril" in mensagem or
        "barris" in mensagem
    ) and (
        "valor" in mensagem or
        "valores" in mensagem
    ):
        return (
            "Temos barris de 20L e 30L:\n"
            "GOLD: 20L e 30L\n"
            "PILSEN: 20L e 30L\n"
            "IPA: 20L e 30L\n"
            "APA: 20L e 30L\n"
            "BLACK: 20L e 30L\n"
            "CHOPP DE VINHO: 20L e 30L"
        )

    elif "curriculo" in mensagem or "currículo" in mensagem:
        return "Pode nos enviar que iremos encaminhar para o setor responsável."

    else:
        return "Não entendi sua mensagem. Pode repetir?"