from collections import Counter
from pprint import pprint
from typing import List
from enum import Enum


class Player(Enum):
    First = 1
    Second = 2


class TicTacToe:
    def __init__(self):
        self.__state = "000000000"

    @property
    def state(self) -> str:
        return self.__state

    def __hash__(self) -> int:
        result = 0
        for i, s in enumerate(self.__state):
            print(9-i)
            result += pow(3, 9-i) * int(s)

        return int(result)

    def can_set(self, pos: int) -> bool:
        return self.__state[pos] == "0"

    def set(self, pos: int, player: Player):
        assert self.can_set(pos)
        new_state = self.__state[:pos]
        new_state += str(player.value)
        new_state += self.__state[pos+1:]
        self.__state = new_state

        if TicTacToe.is_finish(self.__state):
            print("Finish")

    def __repr__(self) -> str:
        t = self.state[:3] + "\n" + self.state[3:6] + "\n" + self.state[6:]
        t = t.replace("0", "-").replace("1", "O").replace("2", "X")
        t += "\n==="
        return t

    @staticmethod
    def is_finish(text: str) -> bool:
        num = []
        for item in text:
            if item == "2":
                item = "-1"

            num.append(int(item))
        
        # Check horizontal
        if sum(num[:3]) == 3 or sum(num[3:6]) == 3 or sum(num[6:]) == 3:
            return True
        elif sum(num[:3]) == -3 or sum(num[3:6]) == -3 or sum(num[6:]) == -3:
            return True
        
        # Check vertical
        elif sum(num[::3]) == 3 or sum(num[1::3]) == 3 or sum(num[2::2]) == 3:
            return True
        elif sum(num[::3]) == -3 or sum(num[1::3]) == -3 or sum(num[2::2]) == -3:
            return True

        # Check cross
        elif num[0] + num[4] + num[8] == 3 or num[2] + num[4] + num[6] == 3:
            return True

        elif num[0] + num[4] + num[8] == -3 or num[2] + num[4] + num[6] == -3:
            return True

        return False

    def get_possible_actions(self) -> List[int]:
        possible_pos = []
        for i, s in enumerate(self.__state):
            if s == "0":
                possible_pos.append(i)

        return possible_pos

    @staticmethod
    def get_all_patterns() -> List[str]:
        result = []

        for a in ["0", "1", "2"]:
            for b in ["0", "1", "2"]:
                for c in ["0", "1", "2"]:
                    if TicTacToe.is_finish(a + b + c + "0"*6):
                        result.append(a+b+c+"0"*6)
                        continue
                    for d in ["0", "1", "2"]:
                        for e in ["0", "1", "2"]:
                            for f in ["0", "1", "2"]:
                                if TicTacToe.is_finish(a + b + c + d + e + f + "0"*3):
                                    result.append(a+b+c+d+e+f+"0"*3)
                                    continue
                                for g in ["0", "1", "2"]:
                                    if TicTacToe.is_finish(a + b + c + d + e + f + g + "0"*2):
                                        result.append(a+b+c+d+e+f+g+"0"*2)
                                        continue
                                    for h in ["0", "1", "2"]:
                                        if TicTacToe.is_finish(a + b + c + d + e + f + g + h +"0"):
                                            result.append(a+b+c+d+e+f+g+h+"0")
                                            continue
                                        for i in ["0", "1", "2"]:
                                            t = a + b + c + d + e + f + g + h + i
                                            count = Counter(t)
                                            if abs(count["1"] - count["2"]) <= 1:
                                                result.append(t)

        return result


ttt = TicTacToe()
all_patterns = TicTacToe.get_all_patterns()
pprint(all_patterns[::30])
ttt.set(0, Player.First)
