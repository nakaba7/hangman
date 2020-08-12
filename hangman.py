import random

def hangman(word):
    wrong=0
    stages=["",
            "_______        ",
            "|              ",
            "|      |       ",
            "|      o       ",
            "|     /|\      ",
            "|     /\       ",
            "|              "
            ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("ハングマンへようこそ！")
    
    while wrong < len(stages)-1:
        print("\n")
        msg="一文字入力してね(二文字以上入力すると不正解扱いとなります):"
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
        else:
            wrong+=1
        print(" ".join(board))
        
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち!")
            print(" ".join(board))
            win=True
            break
    if not win:
       
        print("あなたの負け！正解は{}.".format(word))
    
word_list=["dog","cat","fish","gorilla","monkey"]
random.shuffle(word_list)


hangman(word_list[0])