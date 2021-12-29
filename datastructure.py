def add(List, word):
    # 맨 끝에 새로운 단어를 추가하는 함수에요.
    i = 0
    while List[i] != None:
        i += 1
    List[i] = word

def addAt(List,word,index):
    # index 자리에 새로운 단어를 추가하는 함수에요.
    # index 자리 앞에는 전부 비어 있으면 안돼요.
    # 추가할 수 없는 경우에는 "~ 에 ~ 를 추가할 수 없습니다"를 출력해 주세요.
    if index < 0 or index >= len(List):
        print(index,"에", word, "를 추가할 수 없습니다")
        return

    i = index + 1
    tmp = List[index]
    List[index] = word
    while List[i] != None:
        List[i], tmp = tmp, List[i]
        i+=1
    List[i] = tmp

def deleteAt(List, index):
    # index 자리에 단어를 제거하는 함수에요.
    # index 자리는 비어있으면 안돼요.
    # 제거할 수 없는 경우에는 "~ 에서 제거할 수 없습니다"를 출력해주세요.
    if index < 0 or index >= len(List):
        print(index,"에서 단어를 제거할 수 없습니다")
        return
    if List[index] is None:
        print(index,"에서 단어를 제거할 수 없습니다")
        return
    i = index
    while List[i+1] != None:
        List[i] = List[i+1]
        i+=1
    List[i] = None

def printList(List):
    # 리스트를 출력하는 함수에요. 수정하지 않아도 돼요.
    print("< 엘리스 토끼 단어장 >")
    for word in List:
        if word != None:
            print(word)
        else:
            return

def main():
    # 100개짜리 어레이를 만드는 코드입니다. 지우지 마세요.
    List = [None for _ in range(100)]

    while True:
        value = input()
        if value == "":
            break
        elif value.startswith("#"):
            continue
        elif value == "printList":
            printList(List)
        elif value.startswith("add "):
            add(List, value[4:])
        elif value.startswith("addAt "):
            value = value[6:].split()
            addAt(List, ' '.join(value[:-1]), int(value[-1]))
        elif value.startswith("deleteAt "):
            deleteAt(List, int(value.split()[1]))
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()