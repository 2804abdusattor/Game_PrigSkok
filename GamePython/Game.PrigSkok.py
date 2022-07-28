from tkinter import *
import random
import time
from tkinter import messagebox
class Ball:
	def __init__(self, canvas, paddle_down, paddle_up,color):
		self.canvas = canvas
		self.paddle_down = paddle_down
		self.paddle_up = paddle_up
		self.id_ball = canvas.create_oval(10,10, 25,25, fill=color,)
		self.canvas.move(self.id_ball, 245,450)
		self.score_pad_up = 0
		self.score_pad_down = 0
		 
		starts = [-3,-2,-1,1,2,3]
		random.shuffle(starts)
		self.x = starts[0]		
		self.y = -1 # мяч двигается в верх
		self.canvas_height = self.canvas.winfo_height()
		self.canvas_width = self.canvas.winfo_width()
		self.hit_bottom = False



		self.lbl_text_score_pad_up = Label(canvas,text="Вас счет:",bg="black",fg="blue")
		self.lbl_text_score_pad_up.place(x=10,y=150)

		self.lbl_text_score_pad_down = Label(canvas,text="Вас счет:",bg="black",fg="red")
		self.lbl_text_score_pad_down.place(x=420,y=300)

	def hit_paddle_up(self,ball_pos):
	
		paddle_up_pos = self.canvas.coords(self.paddle_up.id_paddle_up)
		if ball_pos[2] >= paddle_up_pos[0] and ball_pos[0] <= paddle_up_pos[2]:
			if ball_pos[1] <= paddle_up_pos[3] and ball_pos[1] <= paddle_up_pos[3]:
				self.score_pad_up += 1
				self.lbl_score_up = Label(canvas,text=self.score_pad_up,bg="black",fg="blue")
				self.lbl_score_up.place(x=65,y=150) 
				return True	
		return False


	def hit_paddle_down(self,ball_pos):
		paddle_down_pos = self.canvas.coords(self.paddle_down.id_paddle_down)
		if ball_pos[2] >= paddle_down_pos[0] and ball_pos[0] <= paddle_down_pos[2]:
			if ball_pos[3] >= paddle_down_pos[1] and ball_pos[3] <= paddle_down_pos[3]:
				self.score_pad_down +=1
				self.lbl_score_down = Label(canvas,text=self.score_pad_down,bg="black",fg="red")
				self.lbl_score_down.place(x=475,y=300)
				return True
		return False

	def draw(self):
		self.canvas.move(self.id_ball, self.x, self.y)
		ball_pos = self.canvas.coords(self.id_ball)

		# отскакивать мяч верх,вниз
		if ball_pos[1] <= 0:
			self.hit_bottom = True
			self.canvas.itemconfig(self.id_ball,state=HIDDEN)
			self.canvas.itemconfig(self.paddle_up.id_paddle_up,state=HIDDEN) 
			self.canvas.itemconfig(self.paddle_down.id_paddle_down,state=HIDDEN)
			if self.score_pad_up > self.score_pad_down:
				return messagebox.showinfo("Paddle-Up",("Игрок-1:",self.score_pad_up))
			elif self.score_pad_up < self.score_pad_down:
				return messagebox.showinfo("Paddle-Down",("Игрок-2:",self.score_pad_down))
			else:
				return messagebox.showinfo("Ничья",("Ничья:",self.score_pad_down,",",self.score_pad_up))

			# self.y = 3
		if ball_pos[3] >= self.canvas_height:
			self.hit_bottom = True # end game
			self.canvas.itemconfig(self.id_ball,state=HIDDEN)
			self.canvas.itemconfig(self.paddle_down.id_paddle_down,state=HIDDEN)
			self.canvas.itemconfig(self.paddle_up.id_paddle_up,state=HIDDEN)
			if self.score_pad_up > self.score_pad_down:
				return messagebox.showinfo("Paddle-Up",("Игрок-1",self.score_pad_up))
			elif self.score_pad_up < self.score_pad_down:
				return messagebox.showinfo("Paddle-Down",("Игрок-2:",self.score_pad_down))
			else:
				return messagebox.showinfo("Ничья",("Ничья:",self.score_pad_down,",",self.score_pad_up))
			# self.y = -3
		# меняем направление полета
		score = 0
		if self.hit_paddle_down(ball_pos) == True:
			self.y = -3
				
		if self.hit_paddle_up(ball_pos) == True:
			self.y = 3
		# Это свойства для проверки не достигли мяч правой границы холста
		if ball_pos[0] <=0:
			self.x = 3
		if ball_pos[2] >= self.canvas_width:
			self.x = -3

class Paddle_Up:
	def __init__(self,canvas,color):
		self.canvas = canvas
		self.id_paddle_up = self.canvas.create_rectangle(0,0, 100,10, fill=color)
		self.canvas.move(self.id_paddle_up,200,20)
		
		self.x = 0
		self.y = 0
		self.canvas_width = self.canvas.winfo_width()
		self.canvas.bind_all('<Button-1>',self.turn_L)
		self.canvas.bind_all('<Button-3>',self.turn_R)

	def draw(self):
		self.canvas.move(self.id_paddle_up,self.x,self.y)	
		paddle_up_pos = self.canvas.coords(self.id_paddle_up)
		if paddle_up_pos[0] <=0:
			self.x = 0
		if paddle_up_pos[2] >= self.canvas_width:
			self.x = 0

	def turn_L(self,evt):
		self.x = -4

	def turn_R(self,evt):
		self.x = 4

class Paddle_Down:
	def __init__(self,canvas,color):
		self.canvas = canvas
		self.id_paddle_down = self.canvas.create_rectangle(0,0, 100,10, fill=color)
		self.canvas.move(self.id_paddle_down, 200, 480)

		self.x = 0
		self.y = 0
		self.canvas_width = self.canvas.winfo_width()
		self.canvas.bind_all('<KeyPress-Left>',self.turn_L)
		self.canvas.bind_all('<KeyPress-Right>',self.turn_R)
	
	def draw(self):
		self.canvas.move(self.id_paddle_down,self.x,self.y)
		position = self.canvas.coords(self.id_paddle_down)
		if position[0] <= 0:
			self.x = 0
		if position[2] >= self.canvas_width:
			self.x = 0

	def turn_L(self,evt):
		self.x = -4

	def turn_R(self,evt):
		self.x = 4
def start_game():
	paddle_down = Paddle_Down(canvas,"red")
	paddle_up = Paddle_Up(canvas,"blue")
	ball = Ball(canvas,paddle_down,paddle_up,"white")
	while True:
		if ball.hit_bottom == False:
			ball.draw()
			paddle_down.draw()
			paddle_up.draw()

		# else:
			# return messagebox.showinfo("Ping-Pong","Game-Over")

		root.update_idletasks()
		root.update()
		time.sleep(0.01)
def new_game():
	start_game()


def Exit():
	root.destroy()

root = Tk()
root.title("Game Paddle-Ball")
root.resizable(0,0)
root.wm_attributes("-topmost",1)
root.geometry("500x500")

canvas = Canvas(root,width=500,height=500,bg="black") 
canvas.pack()
root.update()

main_menu  = Menu(root)
root.config(menu=main_menu)

player = Menu(main_menu,tearoff=0)

game_menu = Menu(main_menu,tearoff=0)
game_menu.add_command(label="Новая игра",command = new_game)

game_menu.add_command(label="Выход",command = Exit)
main_menu.add_cascade(label="Игра",menu=game_menu)


root.mainloop()
