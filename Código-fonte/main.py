def identificar_bandeira(numero_cartao: str) -> str:
    numero_cartao = numero_cartao.replace(" ", "")
    
    if not numero_cartao.isdigit():
        return "Número inválido. Use apenas dígitos."

    if numero_cartao.startswith("4"):
        return "Visa"
    elif numero_cartao.startswith(("51", "52", "53", "54", "55")):
        return "MasterCard"
    elif numero_cartao.startswith(("34", "37")):
        return "American Express"
    elif numero_cartao.startswith("6011") or numero_cartao.startswith("65"):
        return "Discover"
    elif numero_cartao.startswith(("35")):
        return "JCB"
    elif numero_cartao.startswith(("36", "38", "39")):
        return "Diners Club"
    else:
        return "Bandeira desconhecida"

def main():
    numero = input("Digite o número do cartão de crédito: ")
    bandeira = identificar_bandeira(numero)
    print(f"Bandeira identificada: {bandeira}")

if __name__ == "__main__":
    main()
