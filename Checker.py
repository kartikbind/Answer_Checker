import tkinter

attempt = []
Max_Marks = 720
no_correct = 0
no_wrong = 0
no_left = 0
total_marks = 0
percentage = 0.0
question_no: int = 1


def correct():
    global total_marks, no_correct
    attempt.append(True)
    total_marks += 4
    no_correct += 1
    mark_update()
    question()


def wrong():
    global total_marks, no_wrong
    attempt.append(False)
    total_marks -= 1
    no_wrong += 1
    mark_update()
    question()


def left():
    global no_left
    no_left += 1
    attempt.append(0)
    mark_update()
    question()


def step_back():
    global attempt, question_no, no_correct, no_left, no_wrong, total_marks
    question_no -= 2
    question()
    if attempt[-1] is True:
        no_correct -= 1
        total_marks -= 4
    elif attempt[-1] is False:
        no_wrong -= 1
        total_marks += 1
    else:
        no_left -= 1

    del attempt[-1]


def question():
    global question_no
    tkinter.Label(check, text="Question No: {}".format(question_no)).grid(row=1, column=0)
    question_no += 1


def mark_update():
    global total_marks, no_correct, no_wrong, no_left, percentage
    
    tkinter.Label(result_frame, text='Total Marks = ').grid(row=0, column=0, sticky='w')
    tkinter.Label(result_frame, text=total_marks).grid(row=0, column=1)
    
    tkinter.Label(result_frame, text='No of Correct = ').grid(row=1, column=0, sticky='w')
    tkinter.Label(result_frame, text=no_correct).grid(row=1, column=1)
    
    tkinter.Label(result_frame, text='No of Wrong = ').grid(row=2, column=0, sticky='w')
    tkinter.Label(result_frame, text=no_wrong).grid(row=2, column=1)
    
    tkinter.Label(result_frame, text='No of Left = ').grid(row=3, column=0, sticky='w')
    tkinter.Label(result_frame, text=no_left).grid(row=3, column=1)

    percentage = (total_marks/Max_Marks)*100
    tkinter.Label(result_frame, text='Percentage').grid(row=5, column=0)
    tkinter.Label(result_frame, text='{0:3.3f}'.format(percentage)).grid(row=5, column=1, columnspan=2)


def text_box_fun():

    text_box = tkinter.Text(check, width=50, height=30)
    text_box.grid(row=5, column=0)

    scrollbar = tkinter.Scrollbar(check, orient=tkinter.VERTICAL, command=text_box.yview)
    scrollbar.grid(row=5, column=1, sticky='ns')
    text_box['yscrollcommand'] = scrollbar.set

    i: float = 1.0
    with open('results.txt', 'r') as file_text:
        for text in file_text:
            if text[0] is not '[':
                text_box.insert(i, text)
                i += 1.0


# Initialising the window
check = tkinter.Tk()
check.geometry("500x790+900+0")
check['padx'] = 20
check['pady'] = 20

# Label for the welcome message
tkinter.Label(check, text='Welcome to Checker').grid(row=0, column=0)

question()

# Frame holding the button
button_frame = tkinter.Frame(check)
button_frame.grid(row=2, column=0)

# Button for correct, wrong and left
correct_button = tkinter.Button(button_frame, text='CORRECT', command=correct)
wrong_button = tkinter.Button(button_frame, text='WRONG', command=wrong)
left_button = tkinter.Button(button_frame, text='LEFT', command=left)
step_back_button = tkinter.Button(button_frame, text='STEP BACK', command=step_back)

# Adding the button to the
correct_button.grid(row=0, column=0)
wrong_button.grid(row=0, column=1, padx=5)
left_button.grid(row=0, column=2, padx=5)
step_back_button.grid(row=0, column=3)

# result frame
result_frame = tkinter.Frame(check)
result_frame.grid(row=3, column=0)

mark_update()
text_box_fun()

tkinter.Button(check, text='CANCEL', command=check.quit).grid(row=4, column=0, padx=5, columnspan=2)
check.mainloop()

with open('results.txt', 'a') as file_result:
    print(attempt, file=file_result)
    print("Total Marks: {}".format(total_marks), file=file_result)
    print("No of left: {}".format(no_left), file=file_result)
    print("No of correct: {}".format(no_correct), file=file_result)
    print("No of Wrong: {}".format(no_wrong), file=file_result)
    print("Percentage: {}".format(percentage), file=file_result)
    print('', file=file_result)
