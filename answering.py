from json import load, dumps
from random import choices, shuffle


def text_similarity(text1: str, text2: str) -> float:
    """ На сколько похожи два текста.
    Возвращает от 0 до 1.
    """
    words1 = set(text1.split())
    words2 = set(text2.split())
    common_words = words1.intersection(words2)
    a, b = len(common_words), max(len(words1), len(words2))
    if b == 0:
        return 0
    return a / b


def get_answer(text: str) -> str:
    """ Возвращает один из наиболее вероятных ответов.
    Если наиболее вероятных ответов нет, то просто выбирается рандомный.
    """
    with open('answers.json', encoding='utf-8') as file:
        data = load(file)
    text = text.lower()
    answers = []
    for question, answer in data['answers'].items():
        similar = text_similarity(text, question.lower())
        for a in answer:
            answers.append([a, similar])
    shuffle(answers)
    answers = sorted(answers, key=lambda x: x[1])
    answers.reverse()
    answers = answers[:10]
    return choices(answers)[0][0]


if __name__ == '__main__':
    while True:
        text = input('Я: ')
        print(f'Бот: {get_answer(text)}')
