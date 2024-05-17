"""
Программная реализация машины Тьюринга
Реализован класс TuringMachine, а также консольное взаимодействие с ним.


INPUT EXAMPLE:
abc
3
1 a0 ost
2 a0 ost
3 a0 2 a0 L
1 a 3 a R
2 a 2 a L
3 a 3 a R
1 b 1 c R
2 b 2 a0 L
3 b 3 a0 R
1 c 1 c R
2 c 2 a0 L
3 c 3 a0 R
bccb
"""
from collections import deque


class TuringMachine:
    BELT_MOVES = {"L", "R", "C"}
    EMPTY_VALUE = "a0"
    PROCESS_BREAKER = "ost"

    def __init__(self, alphabet: set, states_count: int):
        self.alphabet = alphabet
        alphabet.add(self.EMPTY_VALUE)
        self.states_table = self.init_table(states_count)
        self.cursor = 0
        self.belt = deque([self.EMPTY_VALUE])

    def init_table(self, states_count: int) -> dict[str, tuple[int, str, str]]:
        n = len(self.alphabet)
        table = {key: [None for _ in range(states_count + 1)] for key in self.alphabet}
        print("Введите через пробел: статус код, символ, новый статус код, новый символ, передвижение ленты")
        print(f"Передвижение ленты: L, R или C. Если новый символ - пустой, то введите {self.EMPTY_VALUE}")
        print(f"Введите статус код, символ, {self.PROCESS_BREAKER}, если это точка останова")
        for _ in range(n * states_count):
            input_value = input()
            if not input_value:
                break
            if self.PROCESS_BREAKER in input_value:
                state, symbol, _ = input_value.split()
                table[symbol][int(state)] = self.PROCESS_BREAKER
            else:
                state, symbol, new_state, new_symbol, belt_move = input_value.split()
                table[symbol][int(state)] = (int(new_state), new_symbol, belt_move)
        return table

    def clear_belt(self):
        self.belt.clear()
        self.belt.append("a0")
        self.cursor = 0

    def put_belt(self, string):
        if set(string) - self.alphabet:
            raise KeyError("Строка содержит символ, не входящий в алфавит")
        self.clear_belt()
        for sym in string:
            self.belt.append(sym)
            self.cursor += 1
        self.belt.append(self.EMPTY_VALUE)
        self.run()
        
    def run(self) -> str:
        current_state = 1
        current_symbol = self.belt[self.cursor]
        while current_symbol != self.PROCESS_BREAKER:
            step = self.states_table[current_symbol][current_state]
            if step == self.PROCESS_BREAKER:
                current_symbol = self.PROCESS_BREAKER
            else:
                current_state, new_symbol, belt_move = step
                self.belt[self.cursor] = new_symbol
                if belt_move == "R":
                    self.cursor -= 1
                elif belt_move == "L":
                    self.cursor += 1
                elif belt_move == "C":
                    pass
                else:
                    raise ValueError("Некорректный шаг")
                if self.cursor == -1:
                    self.cursor = 0
                    self.belt.appendleft(self.EMPTY_VALUE)
                if self.cursor > len(self.belt):
                    self.belt.append(self.EMPTY_VALUE)
                current_symbol = self.belt[self.cursor]
        output = [x for x in self.belt if x != "a0"]
        return "".join(output)

    def __repr__(self):
        return self.belt, self.alphabet, self.cursor
    
    def __str__(self):
        return f"Лента: {self.belt}"


def main():
    alphabet = set(input("Введите все символы алфавита без пробелов. Пустой символ указывать не нужно:\n"))
    states_count = int(input("Укажите число состояний машины Тьюринга: "))
    machine = TuringMachine(alphabet, states_count)
    while True:
        string = input("Введите строку, которую необходимо поместить на ленту:\n")
        if string and "quitMT()" not in string:
            try:
                machine.put_belt(string)
                print(machine.run())
                machine.clear_belt()
            except KeyError:
                print("Ошибка при вводе строки: строка содержит символы из другого алфавита")
        else:
            break


if __name__ == "__main__":
    main()
