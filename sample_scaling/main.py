text_file_directory = '../data/'


summery_data = {}
for text_file_number in range(22829, 22750, -1):
    text_file_name = str(text_file_number) + '.txt'

    text_file = text_file_directory + text_file_name
    f = open(text_file)
    data = f.read()

    filter_set = []

    print(text_file_number)
    import scaling

    filter_set= filter_set+scaling.filter_pronouns
    scaled_data = scaling.filtering_data(data, filter_set)
    #print(scaling.check_count_nouns(scaled_data))
    scaled_data = scaling.check_count_nouns(scaled_data)
    for key, value in scaled_data.items():
        if key in summery_data.keys():
            summery_data[key] += value
        else:
            summery_data[key] = value


import operator
summery_data = sorted(summery_data.items(), key=operator.itemgetter(1), reverse=True)
print(summery_data)
