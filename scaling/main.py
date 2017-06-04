
if __name__ == "__main__":
    textFileDirectory = '../data/'


    summery = {}
    beforeFileDay = 5
    imgNumber = 1
    import scaling
    import readFile
    import os
    for number in range(40491, 37840, -1):
        textFileName = str(number) + '.txt'
        textFile = textFileDirectory + textFileName


        readFile.read(textFile)
        if beforeFileDay == 0 and readFile.date.weekday() != beforeFileDay :
            import operator
            summery = sorted(summery.items(), key=operator.itemgetter(1), reverse=True)

            # Draw Wordcloud

            import wordcloud
            tags = wordcloud.getTags(summery)
            wordcloud.drawCloud(tags, 'wordcloud' + str(imgNumber) + '.png')
            imgNumber +=1
            print(summery)
            summery = {}

        beforeFileDay = readFile.date.weekday()


        scaledData = scaling.getFilteredData(readFile.data, scaling.filter_pronouns + scaling.getMostCommonWords(500))
        scaledData = scaling.getCountNouns(scaledData)


        for key, value in scaledData.items():
            if key in summery.keys():
                summery[key] += value
            else:
                summery[key] = value



        print(number) # print processing text number

        # filter_set
    # sorting
