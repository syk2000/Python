class test:
    def __init__(self, data, n):
        self.d = data
        self.i = n#반복 횟수

    def __iter__(self):
        #__next__ 메서드를 가진 객체 호출
        return self #바로 아래서 next를 만들것 이므로

    def __next__(self):
        #매 반복마다 출력을 정의,
        #끝까지 가면,  StopIteration 에러 raise
        if(self.i > 0):
            self.i -=1
            return self.d

        else:
            raise StopIteration


class Reverse:
    def __init__(self, data):
        self.d = data
        self.i = len(data)#반복 횟수

    def __iter__(self):
        #__next__ 메서드를 가진 객체 호출
        return self #바로 아래서 next를 만들것 이므로

    def __next__(self):
        #매 반복마다 출력을 정의,
        #끝까지 가면,  StopIteration 에러 raise
        if(self.i > 0):
            self.i -=1
            return self.d[self.i]

        else:
            raise StopIteration


class myrange:
    def __init__(self, start, end, jump=1):
        self.s = start
        self.e = end
        self.j = jump

    def __iter__(self):
        return self

    def __next__(self):
        if(self.s >= self.e):
            raise StopIteration
        else:
            tmp = self.s
            self.s += self.j
            return tmp
        
