print("Olá tudo bem? Aqui é a Ravache, como posso te ajudar?")

def responder(mensagem):
    mensagem = mensagem.lower()

    if "promoção" in mensagem or "promoções" in mensagem:
        return "Só um momento! iremos encaminha uma pessoa para te explicar as promoções do dia!"

    elif "ver" in mensagem "cardápio" in mensagem or "cardapio" in mensagem:
        return "Nosso cardapio conta com:\n"
                "*PETISCOS*:\n"
                "combo familia - R$ 99,90\n"
                "Combo casal - R$ 64,90\n"
                "Combo clássico - R$ 34,90\n"
                "Trio da casa - R$ 43,90\n"
                "Batata supreme - R$ 39,90\n"
                "Prato de frios - R$ 27,90\n"
                "*DRINKS:\n*"
                "Afrodisíaco - R$ 24,90\n"
                "Sex on the beach - R$ 24,90\n"
                "Moranpinga - R$ 24,90\n"
                 "Caipirinha - R$ 14,90\n"
                 "Caipivodka - R$ 19,00\n"
                 "Pink lemonade - R$ 08,90\n"
                 "*Torres:*\n"

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
