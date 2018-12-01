def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate*3.5) - (cigs_smoked*2)
    print(answer)


matts_data = [27, 20, 0]


health_calculator(matts_data[0], matts_data[1], matts_data[2])

# Unpacking an argument list
health_calculator(*matts_data)

