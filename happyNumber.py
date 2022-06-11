def isHappyNumber(num: int) -> bool:

    def makeOperation(num:int) -> int:
        numStr = str(num)
        outNum = 0
        for i in numStr:
            outNum += pow(int(i),2)
        return outNum

    results = []
    while True:
        nextNum = makeOperation(num)
        if nextNum == 1:
            return True
        elif nextNum in results:
            return False

        results.append(nextNum)
