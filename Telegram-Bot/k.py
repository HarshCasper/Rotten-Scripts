
def riddle():
    riddles = []
    with open('riddle.txt' ,'r') as file:
        for i in file:
            riddles.append(i.strip('\n'))
    return(riddles)


def ur():
    urls = []
    with open('joke.txt' , 'r') as file:
        for l in file:
            urls.append(l.strip('\n'))
    return(urls)

if __name__ == "__main__":
    print(len(ur()))
    print(len(riddle()))
