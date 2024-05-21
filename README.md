# Машина Тьюринга
#### Программная реализация
___

## Установка программы
1. Скачать архив или склонировать репозиторий
```bash
git clone https://github.com/aeonva1ues/turing_machine.git
```

2. Запустить файл turing.py
```bash
python turing.py
```
___
## Работа программы
1. Введите непрерывную последовательность символов - алфавит
2. Укажите количество состояний машины - целое число, не меньшее 1
3. Заполните таблицу, путем ввода строк формата:
```
state symbol new_state new_symbol move
state symbol ost
```
Где state - текущее состояние, symbol - текущий символ, а new_state и new_symbol - новое состояние и новый символ. Значение move - L(left), R(right), C(center), определяет направление движения поля.
4. Введите строку, состоящую из символов заданного алфавита - в следующей строке получите результат работы машины Тьюринга
5. Для выхода зажмите CTRL + C, либо введите quitTM() или quitMT()
___
https://github.com/aeonva1ues/turing_machine