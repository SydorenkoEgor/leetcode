class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon:str = "balloon"
        characters:dict = dict()
        for char in balloon:
            if char not in characters:
                characters[char] = 0

        for char in text :
                if char in characters:
                    characters[char] +=1

        characters['o'] = int(characters['o'] / 2)
        characters['l'] = int(characters['l'] / 2)

        counterOfWords = min(value for key, value in characters.items())

        return counterOfWords