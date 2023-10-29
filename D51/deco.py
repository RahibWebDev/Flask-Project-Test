
def decorator(func):
    def innerFunc():
        result = func()
        return len(result)
    return innerFunc


@decorator
def showData():
    return "This is func for show"

# @decorator


def nextFunc():
    return "It's next function"


# myDecorator = decorator(nextFunc)
# print(myDecorator())

# print(showData())

def multiplyByTwo(f):
    def inner(*args, **kwargs):
        result = f(*args, **kwargs)
        tempList = []
        for i in result:
            tempList.append(i*2)
        return tempList
    return inner


@multiplyByTwo
def numList(list):
    return list


# print(numList((1, 3, 4)))


# Work to be done
# hərfləri böyük hərfə çevirən dekorator

def upperCaseDecorator(func):
    def innerFunction(*args, **kwargs):
        result = func(*args, **kwargs)
        newResult = result.upper()
        return newResult

    return innerFunction


@upperCaseDecorator
def sayWord(text):
    return text


result = sayWord("fazil")
print(result)


# hərflər arasından saitləri istehsal edən dekorator

def vowelDecorator(func):
    def innerFunction(*args, **kwargs):
        result = func(*args, **kwargs)
        vowels = ["a", "e", "i", "o", "u"]
        newResult = []

        for letter in result:
            if letter in vowels:
                newResult.append(letter)

        return newResult

    return innerFunction


@vowelDecorator
def filterVowels(text):
    return text


result = filterVowels("fazil")
print(result)


# daxil edilən sözün string daxilində olub olmadığını bildirən dekorator
def stringDecorator(func):
    def innerFunction(*args, **kwargs):
        word = input("Sozu daxil et: ")
        result = func(word, *args, **kwargs)
        text = "Fazil son gunler hech xoshbext deyil"
        if word in text:
            print(f"'{word}' sozu cumlede var")
        else:
            print(f"'{word}' sozu cumlede yoxdur")
        return result

    return innerFunction


@stringDecorator
def checkWordInText(word):
    return word


res = checkWordInText()


# list daxilində təkrarlanan ədədlərdən sadəcə birini saxlayıb digərlərini sildikdən sonra yeni listi istehsal edən dekorator

def checkNumsDecorator(func):
    def innerFunction(*args, **kwargs):
        result = func(*args, **kwargs)
        newNums = []
        for num in result:
            if num not in newNums:
                newNums.append(num)
        return newNums

    return innerFunction


@checkNumsDecorator
def sortNumList(nums):
    return nums


res = sortNumList([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 3, 5, 9, 1])
print(res)


# ədədlərin cəmini istehsal edən dekorator

def sumDecorator(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        totalSum = 0
        for i in result:
            totalSum += i
        return totalSum
    return inner


@sumDecorator
def inputForSum(nums):
    return nums


res = inputForSum([1, 2, 3, 4, 5, 6, 7, 8])
print(f"Cem: {res}")
 