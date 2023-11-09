def hero():
    # .......Draw a I
    import turtle

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("white")
    pen.goto(-200, 0)

    pen.color("pink")
    pen.fillcolor("pink")
    pen.begin_fill()
    pen.forward(30)
    pen.left(90)
    pen.forward(150)
    pen.left(90)
    pen.forward(30)
    pen.left(90)
    pen.forward(150)
    pen.end_fill()

    # .......Draw a heart shape with turtle....!
    import turtle

    # Creating turtle
    t = turtle.Turtle()
    t.hideturtle()

    # To design curve
    def curve():
        for i in range(200):
            t.right(1)
            t.forward(1)

            #t. speed(1)


    t.color("pink")

    t.begin_fill()
    t.left(140)
    t.forward(111.65)
    curve()

    t.left(120)
    curve()
    t.forward(111.65)
    t.end_fill()

    lg = turtle.Turtle()
    lg.color("pink")
    lg.setposition(105,95)
    lg.color("white")
    lg.setposition(170,150)
    lg.pensize(40)
    lg.color("pink")
    lg.rt(90)
    lg.fd(50)
    lg.circle(80,180)
    lg.fd(50)
    turtle.done()


if __name__ == '__main__':

    import random
    print("Try to win the game ")
    print("\nTHERE IS A SURPRISE FOR YOU IF YOU WIN THE GAME")
    print("\nstone, paper, scissor game ")
    i= 0
    l = ["s", "p", "sc"]
    won = 0
    pc = 0
    draw = 0
    while i < 10:
        guess = str(input("\nenter s ,p ,sc : "))
        guess = guess.lower()
        rand = random.choice(l)
        rand = rand.lower()
        print(f"PC guess is {rand}")

        if guess == "s":
            if guess == "s" and rand == "sc":
                won += 1
                print("\nYou got 1 point")

            elif guess == rand:
                print(f"\nDraw! your guess : {guess},"
                      f"\nPC guess : {rand} ")
                draw += 1
            else:
                pc += 1
                print(f"\n PC got 1 point")
            print()
            print(f"your Points = {won}")
            print(f"PC points = {pc}")
            print(f"Draw : {draw}")
            print(f"\n Number of turns Remaining : {9-i}")
        elif guess == "p":

            if guess == "p" and rand == "s":
                won +=1
                print("\nYou got 1 point")
            elif guess == rand:
                print(f"\nDraw! your guess : {guess},"
                      f"\nPC guess : {rand} ")
                draw += 1

            else:
                pc += 1
                print(f"\n PC got 1 point")
            print()
            print(f"your Points = {won}")
            print(f"PC points = {pc}")
            print(f"Draw : {draw}")
            print(f"\n Number of turns Remaining : {9-i}")

        elif guess == "sc":

            if guess == "sc" and rand == "p":
                won += 1
                print("\nYou got 1 point")
            elif guess == rand:
                print(f"\nDraw! your guess : {guess},"
                      f"\nPC guess : {rand} ")
                draw += 1
            else:
                pc += 1
                print(f"\n PC got 1 point")
            print()
            print(f"your Points = {won}")
            print(f"PC points = {pc}")
            print(f"Draw : {draw}")
            print(f"\n Number of turns Remaining : {9-i}")
        else:
            print("Enter a valid ANS : ")
            i -= 1
        i += 1

    if won >= pc:
        print("YOU WON !")
        print("See the surprise in the new pop up tab")
        hero()

    else:
        print("Better luck next time")
