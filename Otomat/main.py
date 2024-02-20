items_in_stock = [
    {
    "item_id": 0,
    "item_name": "Su",
    "item_price": 5,
    },
    {
    "item_id": 1,
    "item_name": "Çay",
    "item_price": 10
    },
    {
    "item_id": 2,
    "item_name": "Meyveli Soda",
    "item_price": 15
    },
    {
    "item_id": 3,
    "item_name": "Kahve",
    "item_price": 30
    },
    {
    "item_id": 4,
    "item_name": "Salep",
    "item_price": 30
    },
    {
    "item_id": 5,
    "item_name": "Tavuk Döner Dürüm",
    "item_price": 60
    },
    {
    "item_id": 6,
    "item_name": "Tavuk Döner Porsiyon",
    "item_price": 160
    },
    {
    "item_id": 7,
    "item_name": "Ayran",
    "item_price": 15
    },
    {
    "item_id": 8,
    "item_name": "Kola",
    "item_price": 20
    },
    {
    "item_id": 9,
    "item_name": "Fanta",
    "item_price": 20
    },
    {
    "item_id": 10,
    "item_name": "İce Tea",
    "item_price": 20
    }

]

the_item = []

receipt = """
\t\tÜRÜNLER -- FİYAT
"""

sum = 0

run = True

print("------- PYTHON OTOMAT -------\n\n")
print("---------- Stoktaki Ürünler ----------\n\n")

for i in items_in_stock:
    print(f"Ürün No: {i['item_id']} --- Ürün Adı: {i['item_name']} --- Ürün Fiyatı: {i['item_price']}₺")


def machine(items_in_stock,run, the_item):
    while run:

        buy_item = int(input("\n\nSatın almak istediğiniz ürünün numarasını giriniz: "))

        if buy_item < len(items_in_stock):
            the_item.append(items_in_stock[buy_item])
            print(f"\n\n{items_in_stock[buy_item]['item_name']} sepetinize eklendi.")
        else:
            print("\n\nUrun numarası hatalı. Lütfen tekrar deneyiniz.")
            break
        run = False


    rec_bool = input("\n\nFiş ister misiniz? (E/H): ")
    if rec_bool == "E":
        print(create_receipt(the_item,receipt))
    elif rec_bool == "H":
        print(toplam(the_item))
    else:
        print("Hatalı giris yaptınız. Lütfen tekrar deneyiniz.")


def toplam(the_item):
    sum = 0

    for i in the_item:
        sum += i['item_price']
    print(f"Toplam fiyat: {sum}₺")
    return sum


def create_receipt(the_item,receipt):
    for i in the_item:
        receipt += f"""
        \t{i['item_name']} --- {i['item_price']}₺
        """

    receipt += f"""
        \tTotal --- {toplam(the_item)}₺
    """
    return receipt


if __name__ == "__main__":
    machine(items_in_stock,run, the_item)

