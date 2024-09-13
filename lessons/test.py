def get_ticket_price() -> int:
    age: int = int(input("What is your age?"))
    if age <= 12:
        price: int = 5
    else:
        price: int = 10
    return price


print(get_ticket_price())
