from db.people import get_employees
from salary import calculate_salary
import datetime as tdate
import tetris

def prints():
    calculate_salary()
    get_employees()
    today_date = tdate.datetime.today()
    print(f'{today_date.day}.{today_date.month}.{today_date.year}')

def tetris_game():
    game = tetris.BaseGame(board_size=(8, 8), seed=128)
    for _ in range(6):
        game.hard_drop()
    print(game)

if __name__ == '__main__':
    prints()
    tetris_game()

