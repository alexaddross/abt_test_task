import json


def count_questions(data: dict):
    # вывести количество вопросов (questions)
    
    count = 0
    for round_object in data['game']['rounds']:
        count += len(round_object['questions'])
    
    print(f'Количество вопрос: {count}')



def print_right_answers(data: dict):
    print('Список всех правильных ответов:')
    for index, round_object in enumerate(data['game']['rounds']):
        print(f'Раунд {index + 1}')
        for question in round_object['questions']:
            print(question['correct_answer'])

        print()

def print_max_answer_time(data: dict):
    answer_times = list()

    for round_object in data['game']['rounds']:
        try:
            answer_times.append(round_object['settings']['time_to_answer'])
        except KeyError:
            pass
        
        for question in round_object['questions']:
            try:
                answer_times.append(question['time_to_answer'])
            except KeyError:
                pass

    print(f'Максимально возможное время ответа: {max(answer_times)}')



def main():
    data = json.load(open('test.json')) # загрузить данные из test.json файла

    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    main()