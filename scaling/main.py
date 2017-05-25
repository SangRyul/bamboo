
if __name__ == "__main__":
    text_file_directory = '../data/'


    summery_data = {}
    before_day = 5
    image_number = 1
    import scaling
    import datetime
    import os
    for text_file_number in range(40491, 37840, -1):
        text_file_name = str(text_file_number) + '.txt'

        text_file = text_file_directory + text_file_name
        if os.path.isfile(text_file):
            f = open(text_file)
            date = datetime.datetime.strptime(f.readline(), "%Y년 %m월 %d일 %p %H:%M ")
            print(date.weekday())
            if before_day == 0 and date.weekday() != before_day :
                import operator
                summery_data = sorted(summery_data.items(), key=operator.itemgetter(1), reverse=True)

                # Draw Wordcloud

                import word_cloud
                tags = word_cloud.get_tags(summery_data)
                word_cloud.draw_cloud(tags, 'wordcloud'+str(image_number)+'.png')
                image_number +=1
                print(summery_data)

                summery_data = {}

            before_day = date.weekday()
            data = f.read()
            #print(data)
            filter_set = []
            filter_set= filter_set+scaling.filter_pronouns
            filter_set = filter_set + scaling.most_common_words_filter(500)


            scaled_data = scaling.filtering_data(data, filter_set)
            scaled_data = scaling.check_count_nouns(scaled_data)


            for key, value in scaled_data.items():
                if key in summery_data.keys():
                    summery_data[key] += value
                else:
                    summery_data[key] = value



            print(text_file_number) # print processing text number
        else:
            print("No File :", text_file)


        # filter_set
    # sorting
