# -*- coding: utf-8 -*-

"""
Haegal Book Manager (Ver 1.1.1)
Date: 2023-12-01
Creator: JaeyoungHan

Version History:
Ver 1.0.0 // 2023-11-16
Ver 1.1.0 // 2023-11-21
Ver 1.1.1 // 2023-12-01
"""

# Import modules ===================================================
# > for psql
from dbtool_main import ManageBook  # module for managing books
from dbtool_login import ManageLogin  # module for managing login data

# > for GUI
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk
import ctypes  # for icon

# Font & Colors ====================================================
# text
font = 'AppleSDGothicNeoM00'
COLOR_BG1 = '#CCCCCC'  # light gray
COLOR_BG2 = '#666666'  # dark gray
COLOR_FG1 = '#F3F3F3'  # white
COLOR_FG2 = '#222222'  # black
info = '\t      [해갈 도서 관리 프로그램]\n' \
        '\t   Version: 1.1.1  (2023/12/01)\n' \
        '\t    Creator: 23년도 회장 한재영\n\n'\
        '< 사용법 >\n'\
        '책 이름 입력 후 엔터. 줄임말이나 일부분만 검색 가능.\n'\
        '입력 안 하고 엔터 누르면 모든 도서 열람 가능.\n'\
        "'^!책장번호'로 그 책장에 있는 책 열람 가능 (ex. ^!A-1, ^!C)\n\n"\
        '대출, 반납 시 해당 버튼 누르면 자동 반영.\n'\
        '추가 버튼 누르고 정보 입력하면 추가 가능.\n'\
        '변경/삭제는 회장단만 가능.\n'


# Functions for program ============================================
def open_program_info(_=None):
    """
    Open the menu 'program info'
    :param _: Key binding (F12)
    :return: None
    """
    # GUI for new window
    table = tk.Toplevel(root)
    table.title('Info')
    table.geometry('325x230+500+300')
    table.resizable(False, False)
    table['bg'] = '#CCCCCC'

    table.focus_set()
    table.grab_set()

    # label
    label_info = tk.Label(table, text=info, font=(font, 10), fg=COLOR_FG2, bg=COLOR_BG1, justify='left')
    label_info.place(x=10, y=10)

    # button
    button_close = tk.Button(table, text='닫기', font=(font, 10), width=7,
                             command=table.destroy, fg=COLOR_FG1, bg=COLOR_BG2)
    button_close.place(x=250, y=190)

    # key binding
    table.bind('<Escape>', lambda _: table.destroy())

    table.mainloop()


def exit_window(_=None):
    """
    Close the program
    :param _: Key binding (Ctrl + Q)
    :return: None
    """
    msg_quit = msg.askquestion('Quit', '프로그램을 종료하시겠습니까?')
    if msg_quit == 'yes':
        root.destroy()


def update_issue():
    """
    Open a window for error
    :return: None
    """
    msg.showerror('이런!', '업데이트 예정')


def str_to_num(num):
    if '.' not in num:
        return int(num)
    return float(num)


def change_id():
    """
    Change the id of the program
    :return: None
    """
    # GUI for new window
    table = tk.Toplevel(root)
    table.title('아이디 변경')
    table.geometry('300x170+700+200')
    table.resizable(False, False)
    table['bg'] = COLOR_BG1

    table.focus_set()
    table.grab_set()

    label_old = tk.Label(table, text='기존 아이디', font=(font, 11), fg=COLOR_FG1, bg=COLOR_BG2)
    entry_old = tk.Entry(table, width=30, font=(font, 11))
    label_old.place(x=10, y=10)
    entry_old.place(x=10, y=30)

    label_new = tk.Label(table, text='새 아이디', font=(font, 11), fg=COLOR_FG1, bg=COLOR_BG2)
    entry_new = tk.Entry(table, width=30, font=(font, 11))
    label_new.place(x=10, y=70)
    entry_new.place(x=10, y=90)

    # functions
    def adapt_id():
        """
        Change the id
        :return: None
        """
        global db_id
        # errors
        if entry_old.get() != db_id:
            msg.showerror('오류', '기존 아이디가 다릅니다.')
            entry_old.delete(0, tk.END)
        elif not entry_new.get().isalnum():
            msg.showerror('오류', '새 아이디가 잘못되었습니다.')
            entry_new.delete(0, tk.END)
        elif len(entry_new.get()) < 4:
            msg.showerror('오류', '아이디는 5글자 이상이어야 합니다.')
            entry_new.delete(0, tk.END)
        else:
            msg.showinfo('변경 완료', '아이디가 성공적으로 변경되었습니다.')
            lgn_db.change_db_id(entry_new.get())
            db_id = entry_new.get()
            table.destroy()

    # buttons
    button_change = tk.Button(table, text='변경', font=(font, 11), width=10,
                              command=adapt_id, fg=COLOR_FG1, bg=COLOR_BG2)
    button_change.place(x=100, y=125)

    # key binding
    table.bind('<Return>', lambda _: adapt_id())
    table.mainloop()


def change_pw():
    """
    Change the id of the program
    :return: None
    """
    # GUI for new window
    table = tk.Toplevel(root)
    table.title('비밀번호 변경')
    table.geometry('300x170+700+200')
    table.resizable(False, False)
    table['bg'] = COLOR_BG1

    table.focus_set()
    table.grab_set()

    label_old = tk.Label(table, text='기존 비밀번호', font=(font, 11), fg=COLOR_FG1, bg=COLOR_BG2)
    entry_old = tk.Entry(table, show='*', width=30, font=(font, 11))
    label_old.place(x=10, y=10)
    entry_old.place(x=10, y=30)

    label_new = tk.Label(table, text='새 비밀번호', font=(font, 11), fg=COLOR_FG1, bg=COLOR_BG2)
    entry_new = tk.Entry(table, show='*', width=30, font=(font, 11))
    label_new.place(x=10, y=70)
    entry_new.place(x=10, y=90)

    # functions
    def adapt_pw():
        """
        Change the pw
        :return: None
        """
        global db_pw
        # errors
        if entry_old.get() != db_pw:
            msg.showerror('오류', '기존 비밀번호가 다릅니다.')
            entry_old.delete(0, tk.END)
        elif not entry_new.get() or ' ' in entry_new.get():
            msg.showerror('오류', '새 비밀번호가 잘못되었습니다.')
            entry_new.delete(0, tk.END)
        elif len(entry_new.get()) < 6:
            msg.showerror('오류', '비밀번호는 6자리 이상이어야 합니다.')
            entry_new.delete(0, tk.END)
        else:
            msg.showinfo('변경 완료', '비밀번호가 성공적으로 변경되었습니다.')
            lgn_db.change_db_pw(entry_new.get())
            db_pw = entry_new.get()
            table.destroy()

    # buttons
    button_change = tk.Button(table, text='변경', font=(font, 11), width=10,
                              command=adapt_pw, fg=COLOR_FG1, bg=COLOR_BG2)
    button_change.place(x=100, y=125)

    # key binding
    table.bind('<Return>', lambda _: adapt_pw())
    table.mainloop()


# Main GUI settings ================================================
# > db settings
db = ManageBook()
db_schema, db_table = 'public', 'haegal_bookshelf'
lgn_db = ManageLogin()
db_id, db_pw = lgn_db.get_login_info()

# > GUI for main window
root = tk.Tk()
root.title('해갈 책장')
root.geometry('690x305+100+100')
root.resizable(False, False)
root['bg'] = '#CCCCCC'
icon = tk.PhotoImage(file='C:/hgb-images/icon.png')
root.iconphoto(True, icon, icon)

myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)  # for icon setting error

# > menu
menubar = tk.Menu(root)
menu_info = tk.Menu(menubar, tearoff=0)
menu_info.add_command(label='정보', command=open_program_info, accelerator='F12')
menu_info.add_command(label='나가기', command=exit_window, accelerator='Ctrl+Q')
menubar.add_cascade(label='Info', menu=menu_info)

menu_config = tk.Menu(menubar, tearoff=0)
menu_config.add_command(label='ID 변경', command=change_id)
menu_config.add_command(label='PW 변경', command=change_pw)
menubar.add_cascade(label='Config', menu=menu_config)

root.config(menu=menubar)

# > frame
input_frame = tk.Frame(root, height=295, width=680, relief='ridge', bd=2, bg=COLOR_BG1, padx=2, pady=2)
input_frame.place(x=5, y=5)

# > input entry
label_input = tk.Label(root, text='도서명을 검색하세요', font=(font, 11), fg=COLOR_FG1, bg=COLOR_BG2)
label_input.place(x=10, y=10)
entry_input = tk.Entry(width=35, font=(font, 11))
entry_input.place(x=10, y=30, height=20)

# > treeview
column = ['location', 'name', 'number', 'rent']
book_table = ttk.Treeview(root, columns=column, displaycolumns=column)
book_table.place(x=10, y=70)
book_table.column(column[0], width=80, anchor='center')
book_table.heading(column[0], text='책장 번호', anchor='center')
book_table.column(column[1], width=300, anchor='center')
book_table.heading(column[1], text='도서명', anchor='center')
book_table.column(column[2], width=60, anchor='center')
book_table.heading(column[2], text='권', anchor='center')
book_table.column(column[3], width=100, anchor='center')
book_table.heading(column[3], text='대출 가능 여부', anchor='center')
book_table['show'] = 'headings'


# Main functions ===================================================
def get_book(_=None):
    """
    Show the selected language on the table
    :param _: Key binding (Select listbox)
    :return: None
    """
    # initializing
    book_table.delete(*book_table.get_children())  # initialize the treeview
    book_table.yview_moveto(0)  # initialize the scrollbar

    # show the table
    if entry_input.get()[:2] == '^!' and len(entry_input.get()) == 3:
        location = f'{entry_input.get()[2]}-%'
        tree_value = db.get_location(location)
    elif entry_input.get()[:2] == '^!':
        location = f'{entry_input.get()[2:]}'
        tree_value = db.get_location(location)
    else:
        value = f'%{entry_input.get()}%'
        tree_value = db.read_db(value)

    for i, v in enumerate(tree_value):
        book_table.insert('', 'end', text='', values=v, iid=i)

    # set scrollbar
    scroll = ttk.Scrollbar(root, orient='vertical', command=book_table.yview)
    scroll.place(x=552, y=70, height=225)
    book_table.configure(yscrollcommand=scroll.set)


def rent_book():
    """
    Change a book to rent status
    :return: None
    """
    if book_table.focus():
        selection = book_table.item(book_table.focus()).get('values')
        name, number = selection[1:3]
        db.update_db('rent', '대출 중', name, number)
        get_book()
    else:
        msg.showerror('오류', '대출할 도서가 선택되지 않았습니다.')


def return_book():
    """
    Change a book to return status
    :return: None
    """
    # I know that the func 'rent_book' is completely same as 'return_book',
    # but tkinter is weird; I cannot combine those into just one func.

    if book_table.focus():
        selection = book_table.item(book_table.focus()).get('values')
        name, number = selection[1:3]
        db.update_db('rent', '대출 가능', name, number)
        get_book()
    else:
        msg.showerror('오류', '반납할 도서가 선택되지 않았습니다.')


def change_book():
    """
    Change the status of a book
    :return: None
    """
    if book_table.focus():  # selected
        # GUI for login window
        table = tk.Toplevel(root)
        table.title('로그인')
        table.geometry('251x129+700+300')
        table.resizable(False, False)
        table['bg'] = COLOR_BG1

        table.focus_set()
        table.grab_set()

        # label
        explain_frame = tk.Frame(table, height=115, width=240, relief='ridge', bd=2, bg=COLOR_BG1, padx=2, pady=2)
        label_id = tk.Label(table, text='ID', font=(font, 11), fg=COLOR_FG2, bg=COLOR_BG1, justify='left')
        input_id = tk.Entry(table, width=20, font=(font, 11))
        label_pw = tk.Label(table, text='PW', font=(font, 11), fg=COLOR_FG2, bg=COLOR_BG1, justify='left')
        input_pw = tk.Entry(table, show='*', width=20, font=(font, 11))
        explain_frame.place(x=5, y=5)
        label_id.place(x=15, y=20)
        input_id.place(x=45, y=20, height=20)
        label_pw.place(x=15, y=50)
        input_pw.place(x=45, y=50, height=20)

        # functions
        def get_login(_=None):
            """
            Check the login
            :param _: Key Binding (Return)
            :return: None
            """
            if input_id.get() != db_id or input_pw.get() != db_pw:
                msg.showerror('로그인 실패', '아이디나 비밀번호가 다릅니다.')
                input_pw.delete(0, tk.END)
            else:
                table.destroy()
                update_book()

        def update_book():
            """
            Change the status of the selected book
            :return: None
            """
            new_table = tk.Toplevel(root)
            new_table.title('항목 변경')
            new_table.geometry('300x180+700+300')
            new_table.resizable(False, False)
            new_table['bg'] = COLOR_BG1

            new_table.focus_set()
            new_table.grab_set()

            def adapt_option():
                """
                Save the changes to the server
                :return: None
                """
                menu = menu_var.get()
                change = entry.get()
                book_name, number = book_table.item(book_table.focus()).get('values')

                if not change:
                    msg.showerror('오류', '입력이 잘못되었습니다.')
                else:
                    db.update_db(menu, change, book_name, number)
                    msg.showinfo('변경 완료', '성공적으로 변경되었습니다.')
                    entry.delete(0, tk.END)

            def delete_book():
                """
                Delete the selected book
                :return: None
                """
                selection = book_table.item(book_table.focus()).get('values')
                book_name, number = selection[1:3]
                yesno = msg.askokcancel('삭제', '정말 삭제하시겠습니까? \n이 작업은 되돌릴 수 없습니다.')
                if yesno:
                    db.delete_db(book_name, number)
                    msg.showinfo('삭제 완료', '성공적으로 삭제되었습니다.')
                    entry.delete(0, tk.END)

            # changes - location, name, number, type, byname, language
            # > labels
            label_sel = tk.Label(new_table, text='변경 항목을 선택하세요', font=(font, 11), fg=COLOR_FG1, bg=COLOR_BG2)
            label_sel.place(x=10, y=10)

            # > radio buttons
            menu_var = tk.StringVar()
            location = tk.Radiobutton(new_table, text='위치', font=(font, 11), value='location',
                                      variable=menu_var, bg=COLOR_BG1)
            name = tk.Radiobutton(new_table, text='이름', font=(font, 11), value='name',
                                  variable=menu_var, bg=COLOR_BG1)
            num = tk.Radiobutton(new_table, text='권', font=(font, 11), value='number',
                                 variable=menu_var, bg=COLOR_BG1)
            types = tk.Radiobutton(new_table, text='타입', font=(font, 11), value='type',
                                   variable=menu_var, bg=COLOR_BG1)
            byname = tk.Radiobutton(new_table, text='별칭', font=(font, 11), value='byname',
                                    variable=menu_var, bg=COLOR_BG1)
            language = tk.Radiobutton(new_table, text='언어', font=(font, 11), value='language',
                                      variable=menu_var, bg=COLOR_BG1)
            location.select()

            location.place(x=20, y=40)
            name.place(x=115, y=40)
            num.place(x=210, y=40)
            types.place(x=20, y=60)
            byname.place(x=115, y=60)
            language.place(x=210, y=60)

            # > input entry (for the changes)
            entry = tk.Entry(new_table, width=30, font=(font, 11))
            entry.place(x=10, y=100, height=20)

            # > button for save
            button_change = tk.Button(new_table, text='변경', font=(font, 11), width=10,
                                      command=adapt_option, fg=COLOR_FG1, bg=COLOR_BG2)
            button_delete = tk.Button(new_table, text='삭제', font=(font, 11), width=10,
                                      command=delete_book, fg=COLOR_FG1, bg=COLOR_BG2)

            button_change.place(x=45, y=140)
            button_delete.place(x=170, y=140)

            # > key binding
            new_table.bind('<Return>', lambda _: adapt_option())

            new_table.mainloop()

        # button for login
        button_close = tk.Button(table, text='로그인', font=(font, 10), width=10,
                                 command=get_login, fg=COLOR_FG1, bg=COLOR_BG2)
        button_close.place(x=150, y=80)

        # key binding
        table.bind('<Return>', lambda _: get_login())

        table.mainloop()

    else:
        msg.showerror('오류', '변경할 도서가 선택되지 않았습니다.')


def add_book():
    """
    Add a book
    :return: None
    """
    # GUI for new window
    table = tk.Toplevel(root)
    table.title('도서 추가')
    table.geometry('300x450+700+200')
    table.resizable(False, False)
    table['bg'] = COLOR_BG1

    table.focus_set()
    table.grab_set()

    # > input entry for location
    label_location = tk.Label(table, text='도서 위치', font=(font, 11), fg=COLOR_FG1, bg=COLOR_BG2)
    entry_location = tk.Entry(table, width=30, font=(font, 11))
    label_location.place(x=10, y=10)
    entry_location.place(x=10, y=30)

    # > input entry for book name
    label_name = tk.Label(table, text='도서명(정확하게 입력해주세요)', font=(font, 11), fg=COLOR_FG1, bg=COLOR_BG2)
    entry_name = tk.Entry(table, width=30, font=(font, 11))
    label_name.place(x=10, y=70)
    entry_name.place(x=10, y=90)

    # > input entry for number
    label_number = tk.Label(table, text='권수(숫자만 입력해주세요)', font=(font, 11),
                            fg=COLOR_FG1, bg=COLOR_BG2)
    entry_number = tk.Entry(table, width=30, font=(font, 11))
    label_number.place(x=10, y=130)
    entry_number.place(x=10, y=150)

    # > input buttons for type
    label_type = tk.Label(table, text='도서 종류', font=(font, 11), fg=COLOR_FG1, bg=COLOR_BG2)
    menu_add = tk.StringVar()
    comic = tk.Radiobutton(table, text='만화', font=(font, 11), value='만화', variable=menu_add, bg=COLOR_BG1)
    novel = tk.Radiobutton(table, text='소설', font=(font, 11), value='소설', variable=menu_add, bg=COLOR_BG1)
    draw = tk.Radiobutton(table, text='작법서', font=(font, 11), value='작법서', variable=menu_add, bg=COLOR_BG1)
    paint = tk.Radiobutton(table, text='일러북', font=(font, 11), value='일러북', variable=menu_add, bg=COLOR_BG1)
    etc = tk.Radiobutton(table, text='기타', font=(font, 11), value='기타', variable=menu_add, bg=COLOR_BG1)
    label_type.place(x=10, y=190)
    comic.place(x=30, y=220)
    novel.place(x=115, y=220)
    draw.place(x=200, y=220)
    paint.place(x=73, y=245)
    etc.place(x=158, y=245)
    comic.select()

    # > input entry for byname
    label_byname = tk.Label(table, text='별칭(없으면 공란)', font=(font, 11), fg=COLOR_FG1, bg=COLOR_BG2)
    entry_byname = tk.Entry(table, width=30, font=(font, 11))
    label_byname.place(x=10, y=285)
    entry_byname.place(x=10, y=305)

    # > input buttons for language
    label_language = tk.Label(table, text='도서 언어', font=(font, 11), fg=COLOR_FG1, bg=COLOR_BG2)
    menu_lang = tk.StringVar()
    kor = tk.Radiobutton(table, text='한국어', font=(font, 11), value='kor', variable=menu_lang, bg=COLOR_BG1)
    jpn = tk.Radiobutton(table, text='일본어', font=(font, 11), value='jpn', variable=menu_lang, bg=COLOR_BG1)
    etc_ = tk.Radiobutton(table, text='기타', font=(font, 11), value='other', variable=menu_lang, bg=COLOR_BG1)
    label_language.place(x=10, y=345)
    kor.place(x=30, y=375)
    jpn.place(x=115, y=375)
    etc_.place(x=200, y=375)
    kor.select()

    def put_book():
        """
        Save the changes to the server
        :return: None
        """
        location = entry_location.get()
        name = entry_name.get()
        number = entry_number.get()
        types = menu_add.get()
        byname = entry_byname.get()
        language = menu_lang.get()

        # errors
        if '-' not in location:
            msg.showerror('오류', '위치가 잘못되었습니다.')
        elif not name or len(name) > 50:
            msg.showerror('오류', '이름이 잘못되었습니다.')
        elif not number.isnumeric():
            msg.showerror('오류', '권수가 잘못되었습니다.')
        elif db.is_same_db(name, number, types, language):
            msg.showerror('오류', '이미 있는 도서입니다.')
        else:
            # append
            db.insert_db(location, name, str_to_num(number), types, byname, language)
            msg.showinfo('추가 완료', '성공적으로 추가되었습니다.')

    # button for adding
    button_close = tk.Button(table, text='추가', font=(font, 11), width=10,
                             command=put_book, fg=COLOR_FG1, bg=COLOR_BG2)
    button_close.place(x=100, y=410)

    # key binding
    table.bind('<Return>', lambda _: put_book())
    table.bind('<Escape>', lambda _: table.destroy())

    table.mainloop()


# key bindings
entry_input.bind('<Return>', get_book)
root.bind('<F12>', open_program_info)
root.bind('<Control-q>', exit_window)

# buttons
btn_rent = tk.Button(text='대출', font=(font, 12), command=rent_book, fg=COLOR_FG1, bg=COLOR_BG2)
btn_return = tk.Button(text='반납', font=(font, 12), command=return_book, fg=COLOR_FG1, bg=COLOR_BG2)
btn_change = tk.Button(text='변경/삭제', font=(font, 12), command=change_book, fg=COLOR_FG1, bg=COLOR_BG2)
btn_add = tk.Button(text='추가', font=(font, 12), command=add_book, fg=COLOR_FG1, bg=COLOR_BG2)
btn_rent.place(x=580, y=80, width=100)
btn_return.place(x=580, y=135, width=100)
btn_change.place(x=580, y=190, width=100)
btn_add.place(x=580, y=245, width=100)

# run
root.mainloop()


if __name__ == '__main__':
    pass
