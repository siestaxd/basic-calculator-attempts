import PySimpleGUI as sg

layout = [
    [sg.Txt(''*10)],
    [sg.Text('', size=(15,1), font=('Helvetica', 18), text_color='white', key='input')],
    [sg.Txt(''*10)],
    [sg.ReadFormButton('C'), sg.ReadFormButton('«')],
    [sg.ReadFormButton('1'), sg.ReadFormButton('2'), sg.ReadFormButton('3'), sg.ReadFormButton('/')],
    [sg.ReadFormButton('4'), sg.ReadFormButton('5'), sg.ReadFormButton('6'), sg.ReadFormButton('*')],
    [sg.ReadFormButton('7'), sg.ReadFormButton('8'), sg.ReadFormButton('9'), sg.ReadFormButton('-')],
    [sg.ReadFormButton('.'), sg.ReadFormButton('0'), sg.ReadFormButton('='), sg.ReadFormButton('+')]
]

form = sg.FlexForm(
    'Hesap Makinesi',
    default_button_element_size=(5,2),
    auto_size_buttons=False,
    grab_anywhere=False
)
form.layout(layout)

Result = ''

while True:
    button, value = form.read()
    if button == 'C':
        Result = ''
        form.find_element('input').Update(Result)
    elif button == '«':
        Result = Result[:-1]
        form.find_element('input').Update(Result)
    elif len(Result) == 16:
        pass

    elif button == '=':
        Answer = eval(Result)
        Answer = str(round(float(Answer), 3))
        form.find_element('input').Update(Answer)
        Result = Answer
    
    elif button == 'Quit' or button == None:
        break
    else:
        Result += button
        form.find_element('input').Update(Result)