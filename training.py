from json import load, dumps
from time import time

start = time()
with open('messages.json', encoding='utf-8') as file:  # <-- Файл с сообщениями messages.json !
    data = load(file)
messages: list[dict] = data['messages']
messages.reverse()
temp_msgs = {message['id']: message['content'] for message in messages}
answers = {}

for message in messages:
    if message['reply_message_id'] is not None:
        text = temp_msgs.get(message['reply_message_id'])
        if text is None: continue
        if answers.get(text) is not None:
            answers[text].append(message['content'])
            continue
        answers[text] = [message['content']]

with open('answers.json', 'w', encoding='utf-8') as file:
    file.write(dumps({'answers': answers}, ensure_ascii=False))

print(f'Программа выполнена за {round(time() - start, 2)} сек.')
input()
