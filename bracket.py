from dataclasses import dataclass
import random


@dataclass
class MyPair:
    match: int
    player1: str
    player2: str


@dataclass
class Bracket:
    pair: list


def make_player(num, name1, name2):
    return MyPair(num, name1, name2)


def random_pairs(name_list):
    duos = []
    while len(name_list) != 0:
        rand_idx = random.randint(0,len(name_list)-1)
        name1 = name_list.pop(rand_idx)
        rand_idx = random.randint(0,len(name_list)-1)
        name2 = name_list.pop(rand_idx)
        
        duo_tup = (name1,name2)
        duos.append(duo_tup)

    return duos


def main():
    name_list = ['John', 'Bob', 'Peter', 'Amy', 'Clara', 'Jan']
    pairs = random_pairs(name_list)

    bracket = [make_player(pairs.index(pair),pair[0],pair[1]) for pair in pairs]

    print(bracket)


main()
