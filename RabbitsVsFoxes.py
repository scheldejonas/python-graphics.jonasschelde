from tkinter import *


# Set - canvas window
t_kinter = Tk()

t_kinter.title("Rabbit vs. Foxes")

canvas = Canvas(t_kinter, width=1280, height=720, bg="#eeeeee")

canvas.pack()


# Prepare - graph boundries and titles
canvas.create_line(50, 670, 1230, 670, fill='#000000')

canvas.create_line(50, 670, 50, 50, fill='#000000')

canvas.create_text(640, 30, anchor=N, font=('Arial', 26), text="Rabbit vs. Foxes")

canvas.create_text(640, 80, anchor=N, font=('Arial', 18), text="- Who's gonna be the winner in the long run")

x_baseline = 50

y_baseline = 670


# Set - changable parameters for the estimated population growth
rabbit_a = 0.1

rabbit_b = 0.00002

rabbit_c = 0.01


fox_a = 0.01

fox_b = 0.00002

fox_c = 0.0001


start_rabbits = 500

start_foxes = 10


# Populate - the graph with population data on each animal
def render_graph() :

    start_rabbits = int( input_field_start_rabbits.get() )

    start_foxes = int( input_field_start_foxes.get() )

    rabbits_xy = [50, (y_baseline - start_rabbits)]

    foxes_xy = [50, (y_baseline - start_foxes)]

    rabbits = start_rabbits

    foxes = start_foxes

    for x in range(51, 1230, 1):

        current_rabbits = rabbits

        current_foxes = foxes

        rabbits = current_rabbits * (
                1 + rabbit_a
                - (rabbit_b * current_rabbits)
                - rabbit_c * current_foxes )

        foxes = current_foxes * (1 - fox_a + fox_b * current_rabbits - fox_c * current_foxes )

        rabbit_xy = [x, (y_baseline - rabbits)]

        fox_xy = [x, (y_baseline - foxes)]

        rabbits_xy.extend(rabbit_xy)

        foxes_xy.extend(fox_xy)

    print(rabbits_xy)

    print(foxes_xy)

    last_rabbit_count = str(
        '{:,.2f}'.format(
            (y_baseline - rabbits_xy[-1])
        )
    )


    last_fox_count = str(
        '{:,.2f}'.format(
            (y_baseline - foxes_xy[-1])
        )
    )

    print( 'The steady state for the rabbits, was in this case: ' + last_rabbit_count )

    print( 'The steady state for the foxes, was in this case: ' + last_fox_count )


    # Paint - the two graphes
    canvas.create_line(rabbits_xy, fill='blue')

    canvas.create_line(foxes_xy, fill='red')


    # Set - steady state labels
    label_text_steady_rabbits.set( 'Steady state rabbits: ' + last_rabbit_count )

    label_text_steady_foxes.set( 'Steady state foxes: ' + last_fox_count)


    # Reset - values
    rabbits_xy = []

    foxes_xy = []

    current_rabbits = 0

    current_foxes = 0


# Prepare - input buttons with labels
label_rabbits = Label(canvas, text='Rabbits start')

canvas.create_window( x_baseline + 0, y_baseline + 20, anchor=NW, window=label_rabbits, height=20, width=100)

input_field_start_rabbits = Entry(canvas)

canvas.create_window(x_baseline + 120, y_baseline + 20, anchor=NW, window=input_field_start_rabbits, height=20, width=50)


label_foxes = Label(canvas, text='Rabbits start')

canvas.create_window( x_baseline + 190, y_baseline + 20, anchor=NW, window=label_foxes, height=20, width=100)

input_field_start_foxes = Entry(canvas)

canvas.create_window( x_baseline + 310, y_baseline + 20, anchor=NW, window=input_field_start_foxes, height=20, width=50)


# Prepare - re-render button
render_button = Button(canvas, text='Render', command=render_graph)

canvas.create_window(x_baseline + 380, y_baseline + 20, anchor=NW, window=render_button, height=20, width=100)


# Prepare - steady state result labels
label_text_steady_rabbits = StringVar()

label_text_steady_rabbits.set('Steady state rabbits: 0')

label_steady_state_rabbits = Label(canvas, textvariable=label_text_steady_rabbits)

canvas.create_window( x_baseline + 550, y_baseline + 20, anchor=NW, window=label_steady_state_rabbits, height=20, width=200)

label_text_steady_foxes = StringVar()

label_text_steady_foxes.set('Steady state foxes: 0')

label_steady_state_foxes = Label(canvas, textvariable=label_text_steady_foxes)

canvas.create_window( x_baseline + 770, y_baseline + 20, anchor=NW, window=label_steady_state_foxes, height=20, width=200)





# Open - window
input_field_start_rabbits.insert( 10 , str( start_rabbits ) )

input_field_start_foxes.insert( 10 , str( start_foxes ) )

render_graph()

t_kinter.mainloop()