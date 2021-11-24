def TEST_DATA_BANK():
    jsn = []
    with open('filtered.csv', "r") as csv:
        index = 0
        head = ''
        geo_point = ""
        for line in csv:
            dic = {}
            line = line.replace("\n", "").split(',')
            if index == 0:
                head = line
                index += 1
            else:
                line[19] +=','+ line[20] 
                del line[20]
                for val, title in zip(line, head):
                    dic[title] = val
                jsn.append(dic)                
        return jsn
