def product_test(**kwargs):
    print(kwargs)
    try:
        sell_cost = int(kwargs["sell_cost"])
    except:
        print("ВВЕДИТЕ ОДНО ЦЕЛОЕ ЧИСЛО")
        return False
    return True