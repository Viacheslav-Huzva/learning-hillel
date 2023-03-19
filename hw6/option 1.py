def calculate_profit(cash_flow, tax):
    # узнаємо суму налога
    tax_result = cash_flow / 100 * tax
    print("Сума налога: {:.2f} грн".format(tax_result))

    # прибыль - налог = чистая прибыль
    net_profit = cash_flow - tax_result
    print("Чистая прибыль: {:.2f} грн".format(net_profit))

    return net_profit


if __name__ == '__main__':
    cash_flow = float(input('Введите размер прибыли: '))
    tax = float(input('Введите размер налога в %: '))

    net_profit = calculate_profit(cash_flow, tax)

    print("Чистая прибыль составляет: {:.2f} грн".format(net_profit))
