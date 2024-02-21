def decorator(fun):
    def get_in():
        print('we are in')
        fun()
        print('we are out')
    return get_in()
@decorator
def play_game():
    print('i like cricket')
play_game()