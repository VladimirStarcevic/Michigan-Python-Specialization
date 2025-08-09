inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for item in inventory:
    product_parts = item.split(",")


    name = product_parts[0].strip()
    quantity = product_parts[1].strip()
    price = product_parts[2].strip()


    output_sentence = "The store has {} {}, each for {} USD.".format(quantity, name, price)
    print(output_sentence)