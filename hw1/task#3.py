cash_flow = float(input('размер прибыли:'))
tax = float(input('размер налога в %:'))

# узнаем сумму налога

tax_result = cash_flow / 100 * tax
print("сумма налога:{:.2f} грн".format(tax_result))

# прибыль - налог = чистая прибыль

x = cash_flow - tax_result
print("чистой прибыли:{:.2f} грн".format(x))