import main

B = [[42,39,28,87,37],

[89,12,75,82,84],

[17,74,49,3,5],

[56,76,66,92,85],

[27,18,86,8,58]]

sets = main.create_sets(B)

print(main.calc_score(sets,{42,39,28,87,37},1))
