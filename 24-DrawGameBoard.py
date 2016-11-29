def draw_board(w, h):
    print((" ---"*w + "\n" + "|   "*(w+1) + "\n")*h + " ---"*w)

if __name__ == "__main__":
    draw_board(int(input("Width: ")), int(input("Height: ")))