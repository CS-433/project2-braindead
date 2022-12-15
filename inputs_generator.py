import yaml # for the config file

# Basic input: 

listValues = [26,10,36,48,200,200,200,200,200,200,200,200,3,1,22]
listKeys = ['n_letter_1gram','n_digit_1gram','n_punctuation_1gram','n_POS_tag_1gram',
            'n_letter_2gram','n_letter_3gram','n_letter_4gram',
            'n_punctuation_2gram','n_word_1gram',
            'n_word_2gram','n_POS_tag_2gram','degree_svm','C_svm','seed']


hyperparameters = [20,100,50]
id = 0
listValues_tmp = listValues[:]  # copy and not assignment 
for j in range(4,10):
    for hp in hyperparameters:
        id +=1 
        path_to_input_file = 'Inputs/Input'+str(id)+'.yaml'
        listValues[j] = hp
        features_param = {listKeys[i]: listValues[i] for i in range(0, len(listKeys), 1)}
        with open(path_to_input_file, 'w') as file:
            yaml.dump(features_param, file) 
        listValues = listValues_tmp[:]