import json

class Count:
    like = 0
    dislike = 0

    def __init__(self) -> None:
        f = open('test.json', 'r')
        data = json.load(f)
        self.like = data['👍']
        self.dislike = data['👎']
        f.close()

    def add(self, txt):
        f = open('test.json', 'w')
        dct = {}
        if txt == '👍':
            self.like+=1
        else:
            self.dislike+=1
        dct['👍'] =self.like
        dct['👎'] = self.dislike
        json.dump(dct, f)
        f.close()