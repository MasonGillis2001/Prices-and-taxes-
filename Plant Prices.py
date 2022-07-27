flowerpot = int(input('How many flowerpots? '))
flower_seeds = int(input('How many packs of flower seeds? '))
soil = int(input('How many bags of soil? '))

flowerpot_price = 4.00
flower_seeds_price = 1.00
soil_price = 5.00
tax_rate = 0.06

flower_pot_total = flowerpot * flowerpot_price
flower_seeds_total = flower_seeds * flower_seeds_price
soil_total = soil * soil_price
total = flower_pot_total + flower_seeds_total + soil_total
tax = total * tax_rate
grand_total = total + tax

print(f'Your total for flower pots will be {flower_pot_total}, your total for seeds will be {flower_seeds_total}, your total for soil will {soil_total}, \
your total amount of tax will be {tax}, and your grand total will be {grand_total}.')

