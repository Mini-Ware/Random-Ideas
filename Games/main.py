from classes import Board, Human, Com

b = Board()
h = Human()
c = Com()

switch = True

#gamr loop
while True:
    try:
        switch = not switch
        while b.get_checker():
            b.set_checker((b.set_square(
                h.select_square(),str(h)),
                b.set_square(c.select_square(),str(h))
            )[switch])
        b.check_game_over()
        print(b)
    except IndexError:
        print("Please give a valid location!")
