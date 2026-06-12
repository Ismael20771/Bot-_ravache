<<<<<<< HEAD
import time
print("Oi! Tudo bem? 🍻\n"
"Seja bem-vindo à Ravache!\n"
"Como posso te ajudar hoje?\n")

def responder(mensagem):
    mensagem = mensagem.lower()

    if any(p in mensagem for p in ["promocao","promo","promoções","promocoes","promoção",]):
        time.sleep(2.5)
        return "Só um momento! Iremos encaminhar uma pessoa para te explicar as promoções do dia!"

    elif any(p in mensagem for p in [ "cardapio", "cardápio", "menu", "comida","copo","chopp"]):
        time.sleep(3)
        return ("🍻 Claro! Confira alguns dos destaques do nosso cardápio:\n"

        "*🍟 PETISCOS*\n"
        "• Combo Família - R$ 99,90\n"
        "• Combo Casal - R$ 64,90\n"
        "• Combo Clássico - R$ 34,90\n"
        "• Trio da Casa - R$ 43,90\n"
        "• Batata Supreme - R$ 39,90\n"
        "• Prato de Frios - R$ 27,90\n"

        "*🍹 DRINKS*\n"
        "• Afrodisíaco - R$ 24,90\n"
        "• Sex on the Beach - R$ 24,90\n"
        "• Moranpinga - R$ 24,90\n"
        "• Caipirinha - R$ 14,90\n"
        "• Caipivodka - R$ 19,00\n"
        "• Pink Lemonade - R$ 8,90\n"

        "*🍺 TORRES DE CHOPP*\n"
        "• 2 Litros - R$ 44,90\n"
        "• 3 Litros - R$ 59,90\n"

        "*🍻 CHOPP (400ml | 500ml)*\n"
        "• Pilsen - R$ 11,00 | R$ 12,00\n"
        "• Pilsen Leve --    | R$10,00\n"
        "• Black - R$ 11,00 | R$ 13,00\n"
        "• Gold - R$ 11,00 | R$ 13,00\n"
        "• Weiss - R$ 11,00 | R$ 13,00\n"
        "• APA - R$ 12,00 | R$ 14,00\n"
        "• IPA - R$ 12,00 | R$ 14,00\n"
        "• Vinho - R$ 12,00 | R$ 14,00\n"

        "Caso queira informações sobre as promoções, é só me chamar! 😊\n")
    elif (any(p in mensagem for p in ["valor", "valores", "preço", "precos", "custa"])and any(p in mensagem for p in ["barril", "barris"])):
         time.sleep(2.5)
         return (
            "🍺 Temos barris disponíveis nos tamanhos de 20L e 30L:\n"

            "Pilsen - R$ 262,14 | R$ 359,29\n"
            "Black - R$ 262,14 | R$ 359,29\n"
            "Gold - R$ 279,33 | R$ 384,84\n"
            "Weiss - R$ 279,33 | R$ 384,84\n"
            "APA - R$ 279,33 | R$ 384,84\n"
            "IPA - R$ 296,18 | R$ 410,12\n"
            "Vinho - R$ 271,04 | R$ 372,39\n"
            "Pilsen Leve - R$ 245,23 | R$ 333,70\n"

            "Os valores acima correspondem aos barris de 20L e 30L, respectivamente.\n"
        )

    elif any(p in mensagem for p in [ "curriculo", "currículo","vaga","trabalho","emprego"]):
            time.sleep(2.5)
            return "Claro! Pode nos enviar seu currículo por aqui e iremos encaminhá-lo ao setor responsável. 😊"

    elif "obrigado" in mensagem or "tchau" in mensagem or "bye" in mensagem:
          time.sleep(0.5)
          return "Muito obrigado pelo contato! Foi um prazer atendê-lo. Esperamos vê-lo novamente em breve. 🍻😊"
    
    elif any(p in mensagem for p in ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"]):
            time.sleep(1)
            return "Olá! 😊 Como posso te ajudar hoje?"

    else:
            time.sleep(0.5)
            return "Ops! Não consegui entender sua mensagem. Pode tentar escrever de outra forma?😅"
=======
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
>>>>>>> 6d5f3bdec94f9e3f232a1e1ddc80b6b12e1ce60f
