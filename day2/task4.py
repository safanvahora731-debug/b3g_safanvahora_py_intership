PRICE_PER_NOTEBOOK = 45
BUDGET = 500
QUANTITY_TO_BUY = 7

total_cost_7 = QUANTITY_TO_BUY * PRICE_PER_NOTEBOOK
print(f"Total cost for {QUANTITY_TO_BUY} notebooks: {total_cost_7} rupees")
max_notebooks = BUDGET // PRICE_PER_NOTEBOOK
print(f"Maximum number of notebooks you can buy with {BUDGET} rupees: {max_notebooks}")
money_leftover = BUDGET % PRICE_PER_NOTEBOOK
print(f"Money left over after the purchase: {money_leftover} rupees")