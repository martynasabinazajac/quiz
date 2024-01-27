import json
import random

user_set=[]
points=0

def quiz_questions(question):
    global points
    while True:
        print(f'Pytanie: {question["pytanie"]},\n a:{question["a"]},\n b:{question["b"]},\n c:{question["c"]},\n d:{question["d"]}')
        try:
            answer=str(input('Wprowadź poprawną odpowiedź (a,b,c lub d):'))
            if answer in {"a","b","c","d"}:
                if answer == question['prawidłowa odpowiedź']:
                    points+=1
                    print(f'Dobrze! Suma Twoich punktów: {points}')
                    x=f'Pytanie: {question["pytanie"]} udzielona odpowiedź {answer} jest PRAWIDŁOWA!'
                else:
                    print("Podałeś nieprawidłowa odpowiedź")
                    x=f'Pytanie: {question["pytanie"]} udzielona odpowiedź {answer} jest NIEPRAWIDŁOWA!'
                break
            else:
                raise ValueError('INVALID: Niepoprawna odpowiedź. Wprowadź odpowedź z przedziału a lub b lub c lub d.')
        except ValueError as e:
            print(e)
    return x

def play_again_quiz():
    correct_answer=[]
    global points
    while True:
        random.shuffle(quiz)
        r_quiz=random.sample(quiz, k=2)
        if r_quiz not in user_set:
            user_set.append(r_quiz)
            break
#kod będzie bardziej dynamiczny jeżlei zastosuje opcje range i len(quiz) zamiast odwoływać się bezpośrednio do listy
    for q in range(len(r_quiz)):
        question=quiz[q]
        qq=quiz_questions(question)
        correct_answer.append(qq)
    print(f'Całkowita ilość zebranych punktów {points}')
    print(correct_answer)
    summ_points=len(r_quiz)
    if points == summ_points:
        print('Wygrałeś zebrałeś maksymalna ilość punktów')
    else:
        print(f'Nie udalo się zebrać maksymalnej ilości punktów. Zebrałeś {points}/{summ_points}')

#encoding='utf-8' - bez tego nie zczytywało poprawnie liter ani odpowiedzi , tylko wyrzucało błąd.
with open('quiz.json','r', encoding='utf-8') as file:
    quiz=json.load(file)

play_again_quiz()

while True:
    play_again=input(str('Czy chcesz zagrać ponownie? tak lub nie: '))
    if play_again == 'tak':
        points=0
        play_again_quiz()
    else:
        exit()

