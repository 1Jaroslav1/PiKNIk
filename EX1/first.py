import time


def timeDekorator(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        answer = function(*args, **kwargs)
        end = time.time()

        print(f"Executing time: {(end- start)*1000}")
        return answer
    return wrapper


@timeDekorator
def testFunction(firstNumber, secondNumber):
    #time.sleep(1) # if time of executing is 0 then you have cool computer, so uncomment this line
    return firstNumber + secondNumber


if __name__ == "__main__":
    print(testFunction(2, 3))