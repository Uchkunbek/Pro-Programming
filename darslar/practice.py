def big_sales(sales):
    mk = sales[list(sales.keys())[0]]
    mv = sales(sales.values())[0]
    for k, v in sales.items():
        if v > mv:
            mv = v

print(big_sales())


