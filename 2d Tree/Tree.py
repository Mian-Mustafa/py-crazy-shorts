import turtle

t=turtle.Turtle()
t.speed(0)
t.left(90)
turtle.bgcolor("black")
t.color("lime")

def fractral_tree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        fractral_tree(branch_len - 15)
        t.left(40)
        fractral_tree(branch_len - 15)
        t.right(20)
        t.backward(branch_len)

t.penup()
t.goto(0,-250)
t.pendown()
fractral_tree(100)
turtle.done()