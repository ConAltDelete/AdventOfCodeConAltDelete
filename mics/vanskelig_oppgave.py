
import logging
logging.basicConfig(filename="./mics/vo.log", encoding='utf-8', filemode="w", level=logging.DEBUG)
import aux_functions as aux
import testing_framework as tf

max_val = 3000
forventet_resultat: int = aux.brute_force(max_val) # kjempe tung funksjon, men gir riktig svar
#forventet_resultat = 155

number_of_valids = tf.N_valid(
    parameter_space=tf.Generate_parameter_space,
    filter=tf.Pyhtagorean_validator,
    parameter_function=aux.two_ints,
    transformer_function=aux.quad_py_2,
    maximum_value = max_val,
    parameter_filter = aux.parameter_filter,
    factor_filter = aux.factor_filter
    )

prosent_of_calls = number_of_valids / aux.calls["quad_py_2"]

print("antall gyldige: {}/{}, som git prosent {}".format(number_of_valids,forventet_resultat,prosent_of_calls))
