
#stockfish.is_move_correct('a2a3')
#stockfish.get_board_visual()


import tkinter as tk
import math
import random
import os
from PIL import Image, ImageDraw, ImageTk, ImageGrab
from PIL import ImageColor
import time
import chess
from stockfish import Stockfish



"""

im=Image.open("data/white_pawn.png")
im=im.resize((70,70))
im2=im.crop((0,0,35,70))
im.save("data/white_pawn.png")
im2.save("data/white_pawn2.png")

im=Image.open("data/black_pawn.png")
im=im.resize((70,70))
im2=im.crop((35,0,70,70))
im.save("data/black_pawn.png")
im2.save("data/black_pawn2.png")

im=Image.open("data/white_bishop.png")
im=im.resize((70,70))
im.save("data/white_bishop.png")


im=Image.open("data/black_bishop.png")
im=im.resize((70,70))
im.save("data/black_bishop.png")



im=Image.open("data/white_knight.png")
im=im.resize((70,70))
im.save("data/white_knight.png")


im=Image.open("data/black_knight.png")
im=im.resize((70,70))
im.save("data/black_knight.png")


im=Image.open("data/white_rook.png")
im=im.resize((70,70))
im.save("data/white_rook.png")


im=Image.open("data/black_rook.png")
im=im.resize((70,70))
im.save("data/black_rook.png")


im=Image.open("data/white_queen.png")
im=im.resize((70,70))
im.save("data/white_queen.png")


im=Image.open("data/black_queen.png")
im=im.resize((70,70))
im.save("data/black_queen.png")


im=Image.open("data/white_king.png")
im=im.resize((70,70))
im.save("data/white_king.png")


im=Image.open("data/black_king.png")
im=im.resize((70,70))
im.save("data/black_king.png")


"""

board_ar=[]
flag=0

tp_st=0
def main():
	global can,st,state,cpu,user,board_ar,pmoves,click,user_move,sel_,col,turn,flag,moves

	

	can.delete("all")

	al="abcdefgh"




	board=str(stockfish.get_board_visual()).replace("+","")
	board=board.replace("-","")
	board=board.replace(" ","")



	board_ar=[]

	ar=board.split("\n")
	ar.pop(-1)
	ar.pop(-1)
	for a in ar:
		a_=a.split("|")

		try:
			a_.pop(0)
			a_.pop(-1)
		except:
			pass

		if not len(a_)==0:
			board_ar.append(a_)


	con=0

	y_=8
	for y in range(8):

		for x in range(8):

			if board_ar[y][x]=="k":
				bking=al[x]+str(y_)

			elif board_ar[y][x]=="K":

				wking=al[x]+str(y_)

		y_-=1









	fen=stockfish.get_fen_position()

	board = chess.Board(fen)


	s=fen.split(" ")[1]

	if board.is_check()==True:

		if s=="w":

			p=wking

			cx,cy=getxy_from_pos(p[0],p[1])[:2]
		elif s=="b":

			p=bking

			cx,cy=getxy_from_pos(p[0],p[1])[:2]

		con=1
		flag=1
	else:
		flag=0






	draw_board()












	




	board_col=[]

	if cpu=="b":
		bst=1
	else:
		bst=0


	for y in range(8):

		ar=[]

		for x in range(8):

			ar.append(bst)

			if not x==7:

				if bst==0:
					bst=1
				elif bst==1:
					bst=0

		board_col.append(ar)


	def draw_bg(p,c,colv):
		global col



		bc=board_col[al.index(p[0])][int(p[1])-1]



		if bc==0:
			col_=col[0]
		elif bc==1:
			col_=col[1]

		rgb=ImageColor.getcolor(col_, "RGB")



		nrgb=(int((rgb[0]+colv[0])/2),int((rgb[1]+colv[1])/2),int((rgb[2]+colv[2])/2))

		ncol='#%02x%02x%02x' % nrgb

		x,y=getxy_from_pos(p[0],p[1])[:2]
		if y<0:
			y=-y



		check=check_piece_with_pos(p)

		if check[0]==1 and c==1:
				ncol="#ff5757"


		can.create_rectangle(x,y,x-76,y-76,fill=ncol,outline=ncol)
	
	if sel_!="":
		draw_bg(sel_,0,[120, 254, 39])



	if len(moves)>0 and click==0:

		ppos=moves[-1][:2]
		cpos=moves[-1][2:][:2]




		draw_bg(ppos,0,[255,255,0])
		draw_bg(cpos,0,[255,255,0])


	for m in pmoves:


		p=m[2:][:2]

		draw_bg(p,1,[120, 254, 39])












	if con==1:

		can.create_rectangle(cx,cy, cx-76,cy-76, fill="#ff5757",outline="#ff5757")

























	py=8


	for y in range(8):


		for x in range(8):




			pos=al[x]+str(py)

			if board_ar[y][x]=="r":
				col_=1
				typ="rook"

			elif board_ar[y][x]=="R":
				col_=0
				typ="rook"


			elif board_ar[y][x]=="n":
				col_=1
				typ="knight"

			elif board_ar[y][x]=="N":
				col_=0
				typ="knight"


			elif board_ar[y][x]=="b":
				col_=1
				typ="bishop"

			elif board_ar[y][x]=="B":
				col_=0
				typ="bishop"


			elif board_ar[y][x]=="q":
				col_=1
				typ="queen"

			elif board_ar[y][x]=="Q":
				col_=0
				typ="queen"


			elif board_ar[y][x]=="k":
				col_=1
				typ="king"

			elif board_ar[y][x]=="K":
				col_=0
				typ="king"


			elif board_ar[y][x]=="p":
				col_=1
				typ="pawn"

			elif board_ar[y][x]=="P":
				col_=0
				typ="pawn"

			elif board_ar[y][x]=="":
				continue

			xx,yy=getxy_from_pos(pos[0],pos[1])




			if typ=="pawn":
				draw_pawn(xx,yy,col_)
			elif typ=="rook":
				draw_rook(xx,yy,col_)
			elif typ=="king":
				draw_king(xx,yy,col_)
			elif typ=="bishop":
				draw_bishop(xx,yy,col_)
			elif typ=="queen":
				draw_queen(xx,yy,col_)
			elif typ=="knight":
				draw_knight(xx,yy,col_)

		py-=1



	_board_ = chess.Board()

	try:
		for move in moves:
			_board_.push_uci(move)
	except ValueError as e:
		pass
	    #return f"Invalid move sequence: {e}"

	con=0

	if _board_.is_checkmate():
		fen=stockfish.get_fen_position()
		s=fen.split(" ")[1]

		if s=="w":
			winner="b"
		elif s=="b":
			winner="w"

		if winner==user:
			statement="Checkmate. You win!"
		else:
			statement="Checkmate. You lose!"


		state="gameover"

		con=1
	elif _board_.is_stalemate():
		state="gameover"
		statement="Draw by stalemate!"

		con=1


	elif _board_.is_insufficient_material():
		
		statement="Draw by insufficient material!"
		state="gameover"

		con=1

	elif _board_.is_seventyfive_moves():
		statement="Draw by seventy-five moves rule!"
		state="gameover"

		con=1

	elif _board_.is_fivefold_repetition():
		statement="Draw by fivefold repetition!"
		state="gameover"

		con=1

	elif _board_.is_game_over():
		statement="Game over for another reason!"
		state="gameover"

		con=1







	if con==1:

		xx,yy=496,150

		x_=((40+76*8)-xx)/2
		y_=((40+76*8)-yy)/2



		draw_transparent_bg((40+76*8),(40+76*8),0,0,15,"#000000",0.5,0)
		draw_transparent_bg(xx,yy,x_,y_,15,"#000000",0.8,1)

		can.create_text(x_+xx/2,y_+(yy-40)/2,text=statement,font=("FreeMono",13),fill="#ffffff")


		
		can.create_line(x_,y_+yy-40, x_+xx,y_+yy-40,fill="#555555")
		can.create_line((40+76*8)/2,y_+yy-40, (40+76*8)/2,y_+yy, fill="#555555")

		can.create_text(x_+xx/4,y_+yy-20, text="New Game",font=("FreeMono",13),fill="#ffffff")
		can.create_text((40+76*8)/2+xx/4,y_+yy-20, text="Quit",font=("FreeMono",13),fill="#777777")




	if state=="transform_pawn":

		if user=="b":
			col1="#000000"
			col2="#ffffff"
			col3="#000000"
		elif user=="w":
			col1="#ffffff"
			col2="#000000"
			col3="#ffffff"






		xx,yy=496,300

		x_=((40+76*8)-xx)/2
		y_=((40+76*8)-yy)/2


		draw_transparent_bg((40+76*8),(40+76*8),0,0,15,"#000000",0.5,0)
		draw_transparent_bg(xx,yy,x_,y_,15,col2,0.8,1)


		can.create_text((40+76*8)/2,y_+30,text="Transform Pawn",font=("FreeMono",13),fill=col1)

		global tp_st




		xv=(xx-76*4)/5






		if tp_st==1:
			sel(x_+xv,y_+100,col3)
		elif tp_st==2:
			sel(x_+xv*2+76,y_+100,col3)
		elif tp_st==3:
			sel(x_+xv*3+76*2,y_+100,col3)
		elif tp_st==4:
			sel(x_+xv*4+76*3,y_+100,col3)






		if user=="w":
			clr=0
		elif user=="b":
			clr=1


		draw_queen(x_+xv+76,y_+100+76,clr)
		draw_rook(x_+xv*2+76+76,y_+100+76,clr)
		draw_knight(x_+xv*3+76*2+76,y_+100+76,clr)
		draw_bishop(x_+xv*4+76*3+76,y_+100+76,clr)



		can.create_line(x_,y_+yy-40, x_+xx,y_+yy-40,fill="#555555")


		




		can.create_text((40+76*8)/2,y_+yy-20,text="OK",font=("FreeMono",13),fill=col1)


	elif state=="quit":


		xx,yy=496,150

		x_=((40+76*8)-xx)/2
		y_=((40+76*8)-yy)/2


		draw_transparent_bg((40+76*8),(40+76*8),0,0,15,"#000000",0.5,0)
		draw_transparent_bg(xx,yy,x_,y_,15,"#000000",0.8,1)

		can.create_text((40+76*8)/2,y_+(yy-40)/2,text="Are you sure you want to quit?",font=("FreeMono",13),fill="#ffffff")

		can.create_line(x_,y_+yy-40, x_+xx,y_+yy-40,fill="#555555")
		can.create_line((40+76*8)/2,y_+yy-40, (40+76*8)/2,y_+yy, fill="#555555")





		
		can.create_text(x_+xx/4,y_+yy-20, text="YES",font=("FreeMono",13),fill="#ffffff")
		can.create_text((40+76*8)/2+xx/4,y_+yy-20, text="NO",font=("FreeMono",13),fill="#777777")





	global quit,undo,wd,wh



	x=(wd-740)/2
	root.geometry(str(wh+40)+"x"+str(wh)+"+"+str(int(x))+"+0" )

	quit=ImageTk.PhotoImage(file="data/quit.png")
	undo=ImageTk.PhotoImage(file="data/undo.png")

	can.create_rectangle((40+76*8),0,740,(40+76*8),fill="blue",outline="blue")

	can.create_rectangle((40+76*8),0, 740,75,fill=col[1],outline=col[1])

	ar=[(40+76*8),75]

	a_=180
	for a in range(90):

		x=10*math.sin(math.radians(a_))+(40+76*8)+10
		y=10*math.cos(math.radians(a_))+75+10

		ar.append(x)
		ar.append(y)

		a_+=1


	can.create_polygon(ar,fill=col[1],outline=col[1])



	ar=[740+1,75]

	a_=90
	for a in range(90):

		x=10*math.sin(math.radians(a_))+740-10+1
		y=10*math.cos(math.radians(a_))+75-10

		ar.append(x)
		ar.append(y)

		a_-=1

	can.create_polygon(ar,fill="blue",outline="blue")


	a_=90


	cx,cy=(40+76*8)-10,10
	for a in range(90):

		x=10*math.sin(math.radians(a_))+cx
		y=10*math.cos(math.radians(a_))+cy

		
		ar.append(x)
		ar.append(y)

		a_+=1


	ar.append((40+76*8))
	ar.append(0)



	can.create_polygon(ar,fill=col[1],outline=col[1])


	can.create_image((40+76*8)+5,5,image=quit,anchor="nw")
	can.create_image((40+76*8)+5,5+30+5,image=undo,anchor="nw")







cpu_st=0
def cpu_move():
	global state,moves,cpu_st,turn,user,start_time

	if state=="game" and cpu_st==1:# and time.time()>=start_time+1:

		main()



		if len(moves)>0:
			stockfish.set_position(moves)



		res=stockfish.get_best_move()

		moves.append(res)

		stockfish.set_position(moves)

		

		
		cpu_st=0
		
		turn=user
		main()
		

		

		







	root.after(1000,cpu_move)


def check_piece_with_pos(p):
	global board_ar

	al="abcdefgh"

	xx=al.find(p[0])

	yy=int(p[1])-8

	if yy<0:
		yy=-yy


	if board_ar[yy][xx]=="":
		return [0,""]
	else:
		return [1,board_ar[yy][xx]]






click=0
user_move=""
pmoves=[]

sel_=""
pstate=""


qst=0
def can_b1(e):
	global difficulty,state,moves,cpu_st,click,board_ar,user_move,pmoves,sel_,pstate
	global user,turn,st
	global start_time
	global tp_st, sel_side
	global flag,difficulty
	global qst
	global col,bg_sel


	if state=="intro":
		

		if 143<=e.x<=143+76:
			if 209<=e.y<=209+76:

				sel_side=1
				intro()

				return


		if 286<=e.x<=286+76:
			if 209<=e.y<=209+76:

				sel_side=2
				intro()

				return


		if 429<=e.x<=429+76:
			if 209<=e.y<=209+76:

				sel_side=3
				intro()

				return



		if 143-10<=e.x<=505+10:
			if 399-10<=e.y<=399+10:

				if e.x<143:
					difficulty=0
				elif e.x>505:
					difficulty=20
				else:

					x=e.x-143

					difficulty=x*20/(505-143)

				if difficulty<1:
					difficulty=1







				intro()





		if 269+15<=e.x<=474-15:
			if 474<=e.y<=474+30:
				start_game()
				return


		cx,cy=269+15,474+15


		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:

			start_game()
			return




		cx,cy=269+70-15,474+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:
			start_game()
			return




	elif state=="transform_pawn":
		
		if 144.4<=e.x<=114.4+76:
			if 274<=e.y<=274+76:

				tp_st=1

				main()


		if 228.8<=e.x<=228.8+76:
			if 274<=e.y<=274+76:

				tp_st=2

				main()


		if 343.2<=e.x<=343.2+76:
			if 274<=e.y<=274+76:

				tp_st=3

				main()


		if 457.6<=e.x<=457.6+76:
			if 274<=e.y<=274+76:

				tp_st=4

				main()






		p=""
		if 76<=e.x<=572:
			if 434<=e.y<=434+40:

				


				if tp_st==1:
					p="q"

				elif tp_st==2:
					p="r"

				elif tp_st==3:
					p="n"

				elif tp_st==4:
					p="b"




		if not p=="":

			user_move+=p

			moves.append(user_move)

			stockfish.set_position(moves)

			state="game"

			

			user_move=""
			pmoves=[]
			click=0
			cpu_st=1

			start_time=time.time()

			turn=cpu

			sel_=""

			tp_st=0

			main()

	elif state=="game" and turn==user:


		if 20<=e.x<=(40+76*8):

			x=e.x
			y=e.y





			if st==1:

				if x<20:
					pass
				elif x<=(20+76):
					x="a"
				elif x<=(20+76*2):
					x="b"
				elif x<=(20+76*3):
					x="c"
				elif x<=(20+76*4):
					x="d"
				elif x<=(20+76*5):
					x="e"
				elif x<=(20+76*6):
					x="f"
				elif x<=(20+76*7):
					x="g"
				elif x<=(20+76*8):
					x="h"


				if y<20:
					pass
				elif 20<=y<=(20+76):
					y="8"
				elif y<=(20+76*2):
					y="7"		
				elif y<=(20+76*3):
					y="6"
				elif y<=(20+76*4):
					y="5"
				elif y<=(20+76*5):
					y="4"
				elif y<=(20+76*6):
					y="3"
				elif y<=(20+76*7):
					y="2"
				elif y<=(20+76*8):
					y="1"
			elif st==0:


				if x<20:
					pass
				elif x<=(20+76):
					x="h"
				elif x<=(20+76*2):
					x="g"
				elif x<=(20+76*3):
					x="f"
				elif x<=(20+76*4):
					x="e"
				elif x<=(20+76*5):
					x="d"
				elif x<=(20+76*6):
					x="c"
				elif x<=(20+76*7):
					x="b"
				elif x<=(20+76*8):
					x="a"


				if y<20:
					pass
				elif y<=(20+76):
					y="1"
				elif y<=(20+76*2):
					y="2"		
				elif y<=(20+76*3):
					y="3"
				elif y<=(20+76*4):
					y="4"
				elif y<=(20+76*5):
					y="5"
				elif y<=(20+76*6):
					y="6"
				elif y<=(20+76*7):
					y="7"
				elif y<=(20+76*8):
					y="8"



			pos=x+y


			sel_=pos






			check=check_piece_with_pos(pos)


			if click==1:


					try:
						v=pmoves.index(user_move+pos)

						cp=check_piece_with_pos(user_move)



						if cp[1].lower()=="p":
							if pos[-1]=="8" or pos[-1]=="1" :
								state="transform_pawn"

								user_move+=pos

								main()

								

								return





						#############

						user_move+=pos

						moves.append(user_move)

						stockfish.set_position(moves)

						user_move=""
						pmoves=[]
						click=0
						cpu_st=1

						start_time=time.time()

						turn=cpu

						sel_=""
					except:
						user_move=""
						pmoves=[]
						click=0



			if click==0:

				if check[0]==0:

					user_move=""
					click=0
				else:

					if click==0:


						user_move=str(pos)


						pmoves=[]

						def possible_moves(user_move):
							global pmoves

							al="abcdefgh"

							y_=8

							for y in range(8):

								for x in range(8):

									xx=al[x]


									p=user_move+xx+str(y_)


									if stockfish.is_move_correct(p)==True:
										pmoves.append(p)

									elif stockfish.is_move_correct(p+"q")==True:
										pmoves.append(p)


								y_-=1





						possible_moves(user_move)


						if len(pmoves)>0:
							click=1







			main()













	if state=="game" or state=="transform_pawn" or state=="gameover" or state=="quit":




		cx,cy=(40+76*8)+5+15,5+15

		r=math.sqrt( (cx-e.x)**2 + (cy-e.y)**2 )

		if r<=15:
			if qst==0:
				pstate=state
			state="quit"

			


			if qst==0:
				qst=1
			elif qst==1:
				qst=0





			main()

			



		cx,cy=(40+76*8)+5+15,5+30+5+15

		r=math.sqrt( (cx-e.x)**2 + (cy-e.y)**2 )

		if r<=15:
			try:


				if turn==user:

					if cpu=="w" and len(moves)==1:
						pass

						

					elif cpu=="b" and len(moves)==1: 
						moves.pop(-1)
					else:

						moves.pop(-1)
						moves.pop(-1)


					turn=user

					if state=="transform_pawn" or state=="gameover":
						state="game"


					stockfish.set_position(moves)

					pmoves=[]

					main()
			except:
				pass


	





	if state=="quit" and qst==1:



		if 76<=e.x<=(40+76*8)/2:
			if 359<=e.y<=399:

				board_ar=[]
				flag=0


				click=0
				user_move=""
				pmoves=[]

				sel_=""
				pstate=""
				sel_side=2

				turn="x"

				difficulty=1
				qst=0


				intro()






		if (40+76*8)/2<=e.x<=572:
			if 359<=e.y<=399:

				state="game"
				qst=0

				main()

		cx,cy=376.33333333333363+15,375+15


	if state=="quit" and qst==0:
		state=pstate


		main()

















	if state=="gameover":




		if 76<=e.x<=(40+76*8)/2:
			if 359<=e.y<=399:

				board_ar=[]
				flag=0


				click=0
				user_move=""
				pmoves=[]

				sel_=""
				pstate=""
				sel_side=2

				turn="x"

				difficulty=1
				qst=0


				intro()








		if (40+76*8)/2<=e.x<=572:
			if 359<=e.y<=399:

				root.quit()








def draw_pawn2(x,y,col_):
	global st,can,col
	global white_pawn2,black_pawn2




	if col_==0:

		can.create_image(x+(76-70)/2,y+(76-70)/2, image=white_pawn2,anchor="nw")
	elif col_==1:

		can.create_image(x+(76-70)/2,y+(76-70)/2, image=black_pawn2,anchor="nw")










def draw_pawn(x,y,col_):
	global st,can,col
	global white_pawn,black_pawn2




	x1=x-76
	y1=y-76


	if col_==0:
		can.create_image(x1+(76-70)/2,y1+(76-70)/2, image=white_pawn,anchor="nw")
	elif col_==1:
		can.create_image(x1+(76-70)/2,y1+(76-70)/2, image=black_pawn,anchor="nw")



def draw_rook(x,y,col_):
	global st,can,col

	global white_rook,black_rook





	x1=x-76
	y1=y-76


	if col_==0:

		can.create_image(x1+(76-70)/2,y1+(76-70)/2, image=white_rook,anchor="nw")
	elif col_==1:

		can.create_image(x1+(76-70)/2,y1+(76-70)/2, image=black_rook,anchor="nw")




def draw_king(x,y,col_):
	global st,can,col

	global white_king,black_king

	x1=x-76
	y1=y-76


	if col_==0:
		can.create_image(x1+(76-70)/2,y1+(76-70)/2, image=white_king,anchor="nw")
	elif col_==1:

		can.create_image(x1+(76-70)/2,y1+(76-70)/2, image=black_king,anchor="nw")





def draw_bishop(x,y,col_):
	global st,can,col

	global white_bishop,black_bishop


	x1=x-76
	y1=y-76


	if col_==0:
		can.create_image(x1+(76-70)/2,y1+(76-70)/2, image=white_bishop,anchor="nw")
	elif col_==1:
		can.create_image(x1+(76-70)/2,y1+(76-70)/2, image=black_bishop,anchor="nw")



def draw_queen(x,y,col_):
	global st,can,col

	global white_queen,black_queen



	x1=x-76
	y1=y-76


	if col_==0:

		can.create_image(x1+(76-70)/2,y1+(76-70)/2, image=white_queen,anchor="nw")
	elif col_==1:
		can.create_image(x1+(76-70)/2,y1+(76-70)/2, image=black_queen,anchor="nw")





def draw_knight(x,y,col_):
	global st,can,col

	global white_knight,black_knight

	x1=x-76
	y1=y-76

	if col_==0:

		can.create_image(x1+(76-70)/2,y1+(76-70)/2, image=white_knight,anchor="nw")
	elif col_==1:

		can.create_image(x1+(76-70)/2,y1+(76-70)/2, image=black_knight,anchor="nw")




def getxy_from_pos(x,y):

	global st



	if st==1:

		if x=="a":
			x=76
		elif x=="b":
			x=76*2
		elif x=="c":
			x=76*3
		elif x=="d":
			x=76*4
		elif x=="e":
			x=76*5
		elif x=="f":
			x=76*6	
		elif x=="g":
			x=76*7
		elif x=="h":
			x=76*8


		if y=="8":
			y=76
		elif y=="7":
			y=76*2
		elif y=="6":
			y=76*3
		elif y=="5":
			y=76*4
		elif y=="4":
			y=76*5
		elif y=="3":
			y=76*6
		elif y=="2":
			y=76*7
		elif y=="1":
			y=76*8
	elif st==0:


		if x=="h":
			x=76
		elif x=="g":
			x=76*2
		elif x=="f":
			x=76*3
		elif x=="e":
			x=76*4
		elif x=="d":
			x=76*5
		elif x=="c":
			x=76*6	
		elif x=="b":
			x=76*7
		elif x=="a":
			x=76*8


		if y=="1":
			y=76
		elif y=="2":
			y=76*2
		elif y=="3":
			y=76*3
		elif y=="4":
			y=76*4
		elif y=="5":
			y=76*5
		elif y=="6":
			y=76*6
		elif y=="7":
			y=76*7
		elif y=="8":
			y=76*8


	x=x+20
	y=y+20
	sz=76
	return [x,y]


def create_polygon(*args, **kwargs):
	global can




	if "alpha" in kwargs:         
		if "fill" in kwargs:
			# Get and process the input data
			fill = root.winfo_rgb(kwargs.pop("fill"))\
			       + (int(kwargs.pop("alpha") * 255),)
			outline = kwargs.pop("outline") if "outline" in kwargs else None

			# We need to find a rectangle the polygon is inscribed in
			# (max(args[::2]), max(args[1::2])) are x and y of the bottom right point of this rectangle
			# and they also are the width and height of it respectively (the image will be inserted into
			# (0, 0) coords for simplicity)
			image = Image.new("RGBA", (max(args[::2]), max(args[1::2])))

			ImageDraw.Draw(image).polygon(args, fill=fill, outline=outline)



			images.append(ImageTk.PhotoImage(image))  # prevent the Image from being garbage-collected


			return can.create_image(0, 0, image=images[-1], anchor="nw")  # insert the Image to the 0, 0 coords
		raise ValueError("fill color must be specified!")
	return can.create_polygon(*args, **kwargs)

images = []


def draw_transparent_bg(xx,yy,x_,y_,r,col,opacity,con):



	if con==0:
		create_polygon(x_,y_, x_+xx,y_, x_+xx,y_+yy, x_,y_+yy, fill=col, alpha=opacity)

	elif con==1:



		ar=[]


		ang=270

		for a_ in range(90):


			x=r*math.sin(math.radians(ang))+x_+r
			y=r*math.cos(math.radians(ang))+y_+r


			ar.append(int(x))
			ar.append(int(y))



			ang-=1





		ang=180

		for a_ in range(90):


			x=r*math.sin(math.radians(ang))+x_+xx-r
			y=r*math.cos(math.radians(ang))+y_+r


			ar.append(int(x))
			ar.append(int(y))



			ang-=1




		ang=90

		for a_ in range(90):


			x=r*math.sin(math.radians(ang))+x_+xx-r
			y=r*math.cos(math.radians(ang))+y_+yy-r


			ar.append(int(x))
			ar.append(int(y))



			ang-=1






		ang=0

		for a_ in range(90):


			x=r*math.sin(math.radians(ang))+x_+r
			y=r*math.cos(math.radians(ang))+y_+yy-r


			ar.append(int(x))
			ar.append(int(y))



			ang-=1







		create_polygon(*ar, fill=col, alpha=opacity)


def draw_board():
	global can
	global turn,cpu,user,col,flag


	col3=col[0]

	if flag==1:
		can.create_rectangle(0,0,(40+76*8),(40+76*8),fill="#ff5757",outline="#ff5757")
		col3="#000000"


	al="abcdefgh"

	col1=col[0]
	col2=col[0]
	if turn==cpu:
		can.create_rectangle(0,0, (40+76*8),20-1, fill="#78fe27",outline="#78fe27")
		col1="#000000"

	elif turn==user:
		can.create_rectangle(0,(40+76*8)-20+1, (40+76*8),(40+76*8), fill="#78fe27",outline="#78fe27")
		col2="#000000"





	if cpu==0 or cpu=="b":

		bst=0


		x=20+76/2
		for val in al:
			can.create_text(x,10,text=val,font=("FreeMono",13),anchor="c",fill=col1)

			can.create_text(x,(40+76*8)-10,text=val,font=("FreeMono",13),anchor="c",fill=col2)

			x+=76


		c=8
		y=20+76/2
		for n in range(8):

			can.create_text(10,y,text=str(c),font=("FreeMono",13),anchor="c",fill=col3)
			can.create_text((40+76*8)-10,y,text=str(c),font=("FreeMono",13),anchor="c",fill=col3)

			y+=76
			c-=1



	else:

		bst=1

		v=len(al)

		x=20+76/2
		c=-1
		for val in range(v):
			can.create_text(x,10,text=al[c],font=("FreeMono",13),anchor="c",fill=col1)

			can.create_text(x,(40+76*8)-10,text=al[c],font=("FreeMono",13),anchor="c",fill=col2)

			x+=76
			c-=1


		c=1
		y=20+76/2
		for n in range(8):

			can.create_text(10,y,text=str(c),font=("FreeMono",13),anchor="c",fill=col3)
			can.create_text((40+76*8)-10,y,text=str(c),font=("FreeMono",13),anchor="c",fill=col3)

			y+=76
			c+=1


	y=20

	for y_ in range(8):

		x=20

		for x_ in range(8):

			if bst==0:
				bcol=col[0]
			elif bst==1:
				bcol=col[1]




			can.create_rectangle(x,y, x+76,y+76, fill=bcol,outline=bcol)


			if x_!=7:

				if bst==0:
					bst=1
				elif bst==1:
					bst=0

			x+=76

		y+=76



def sel(x,y,col_="#B1E4B9"):

	global can,col



	can.create_line(x+10,76+y, x+76-10,76+y,fill=col_,width=2)





def start_game():


	global stockfish,difficulty,sel_side,user,cpu,turn,moves,st,cpu_st,state
	global start_time
	global tp_st
	global board_ar,flag,click,user_move,pmoves,pstate,sel_



	board_ar=[]
	flag=0


	click=0
	user_move=""
	pmoves=[]

	sel_=""
	pstate=""



	cwd = os.getcwd()

	cwd2=""
	c=cwd.split("\\")

	for i in c:
		cwd2+=i
		cwd2+="/"


	stockfish = Stockfish(path=cwd2+"stockfish-windows-x86-64-avx2/stockfish/stockfish-windows-x86-64-avx2.exe"
		,depth=difficulty, parameters={"Threads": 2, "Minimum Thinking Time": 30,"Skill Level": difficulty})


	if sel_side==1:
		user="w"
		cpu="b"

		cpu_st=0

		st=1

	elif sel_side==2:

		r=random.randint(0,1)


		if r==0:
			user="w"
			cpu="b"

			cpu_st=0

			st=1
		elif r==1:
			user="b"
			cpu="w"

			cpu_st=1
			start_time=time.time()

			st=0
	elif sel_side==3:
		user="b"
		cpu="w"

		cpu_st=1

		start_time=time.time()

		st=0

	turn="w"

	stockfish.set_fen_position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR/ w KQkq - 0 1")

	moves=[]

	state="game"

	tp_st=0


	main()







def scale_difficulty():

	global difficulty

	#143.0 399.0 505.0 399.0

	#difficulty=0


	x=143

	xx=(difficulty*(505-143)/20)

	x2=x+xx

	can.create_line(x2,399-10, x2,399+10,fill="#B1E4B9",width=2)






def intro():

	global can
	global sel_side

	global state

	global col

	global bg_sel
	global wh
	global difficulty


	x=(wd-(40+76*8))/2
	root.geometry(str(wh)+"x"+str(wh)+"+"+str(int(x))+"+0" )

	state="intro"

	can.delete("all")



	draw_board()


	xx,yy=496,390

	x_=((40+76*8)-xx)/2
	y_=((40+76*8)-yy)/2


	draw_transparent_bg((40+76*8),(40+76*8),0,0,15,"#000000",0.5,0)
	draw_transparent_bg(xx,yy,x_,y_,15,"#000000",0.8,1)

	can.create_text((40+76*8)/2,y_+40,text="Play aganist Stockfish AI",font=("FreeMono",13),anchor="c",fill=col[0])

	xv=(496-(76*3))/4






	xx_=(496-76*3)/4


	if sel_side==1:


		sel(x_+xx_,y_+85)

	elif sel_side==2:

		sel(x_+xx_*2+76,y_+85)

	elif sel_side==3:

		sel(x_+xx_*3+76*2,y_+85)










	draw_pawn(x_+xx_+76,y_+80+76,0)
	draw_pawn2(x_+xx_*2+76,y_+80,0)
	draw_pawn2(x_+xx_*2+76+35,y_+80,1)
	draw_pawn(x_+xx_*3+76*2+76,y_+80+76,1)

	can.create_text(x_+xx_+76/2,y_+80+76+20,text="white",font=("FreeMono",13),fill=col[0])
	can.create_text(x_+xx_*2+76+38,y_+80+76+20,text="random",font=("FreeMono",13),fill=col[0])
	can.create_text(x_+xx_*3+76*2+76/2,y_+80+76+20,text="black",font=("FreeMono",13),fill=col[0])


	can.create_text((40+76*8)/2,y_+220+20,text="Difficulty",font=("FreeMono",13),anchor="c",fill=col[0])


	can.create_line(x_+xv,y_+250+20, x_+xx-xv,y_+250+20,fill=col[0],width=2)

	#print(x_+xv,y_+250+20, x_+xx-xv,y_+250+20)


	
	


	can.create_text((40+76*8)/2,y_+250+30+20,text=str(int(difficulty)),font=("FreeMono",13),fill=col[0])



	scale_difficulty()

	#difficulty=int(difficulty)



	




















	


	#can.create_rectangle(350-40,y_+yy-30-30, 350+40,y_+yy-30,fill="#000000",outline="#000000")
	#can.create_oval(350-40-15,y_+yy-30-30, 350-40+15,y_+yy-30-30+30,fill="#000000",outline="#000000")
	#can.create_oval(350+40-15,y_+yy-30-30, 350+40+15,y_+yy-30-30+30,fill="#000000",outline="#000000")



	can.create_arc((40+76*8)/2-40-15,y_+yy-5-30-10, (40+76*8)/2-40+15,y_+yy-5-30+30-10,start=90,extent=180,style="arc",outline=col[0])
	can.create_arc((40+76*8)/2+40-15,y_+yy-5-30-10, (40+76*8)/2+40+15,y_+yy-5-30+30-10,start=270,extent=180,style="arc",outline=col[0])

	can.create_line((40+76*8)/2-40,y_+yy-5-30-10, (40+76*8)/2+40,y_+yy-5-30-10,fill=col[0])
	can.create_line((40+76*8)/2-40-1,y_+yy-5-10, (40+76*8)/2+40,y_+yy-5-10,fill=col[0])





	#can.create_line(x_,y_+yy-40, x_+xx,y_+yy-40,fill=col[0])


	can.create_text((40+76*8)/2,y_+yy-20-10, text="PLAY", font=("FreeMono",13),fill=col[0])





white_pawn=None
white_pawn2=None
black_pawn=None
black_pawn2=None
white_bishop=None
black_bishop=None
white_knight=None
black_knight=None
white_rook=None
black_rook=None
white_queen=None
black_queen=None
white_king=None
black_king=None

def load_im():
	global white_pawn,white_pawn2,black_pawn,black_pawn2,white_bishop,black_bishop,white_knight,black_knight,white_rook,black_rook,white_queen
	global black_queen,white_king,black_king

	white_pawn=ImageTk.PhotoImage(file="data/white_pawn.png")
	white_pawn2=ImageTk.PhotoImage(file="data/white_pawn2.png")
	black_pawn=ImageTk.PhotoImage(file="data/black_pawn.png")
	black_pawn2=ImageTk.PhotoImage(file="data/black_pawn2.png")
	white_bishop=ImageTk.PhotoImage(file="data/white_bishop.png")
	black_bishop=ImageTk.PhotoImage(file="data/black_bishop.png")
	white_knight=ImageTk.PhotoImage(file="data/white_knight.png")
	black_knight=ImageTk.PhotoImage(file="data/black_knight.png")
	white_rook=ImageTk.PhotoImage(file="data/white_rook.png")
	black_rook=ImageTk.PhotoImage(file="data/black_rook.png")
	white_queen=ImageTk.PhotoImage(file="data/white_queen.png")
	black_queen=ImageTk.PhotoImage(file="data/black_queen.png")
	white_king=ImageTk.PhotoImage(file="data/white_king.png")
	black_king=ImageTk.PhotoImage(file="data/black_king.png")
cpu=0
user=0
col=["#B1E4B9","#70A2A3",]

turn="x"

sel_side=2

st=1

state=0

difficulty=1

stockfish=0

moves=[]

start_time=0

quit=0
undo=0


bg_sel=1


root=tk.Tk()

wd,ht=root.winfo_screenwidth(),root.winfo_screenheight()


x=(wd-(40+76*8))/2

wh=(40+76*8)
root.geometry(str(wh)+"x"+str(wh)+"+"+str(int(x))+"+0" )

root.wm_attributes("-transparentcolor","blue")
root.resizable(0,0)
root.title("HCHESS")
root.wm_attributes("-topmost",1)
root.iconbitmap("data/icon.ico")


can=tk.Canvas(width=wh+40,height=(40+76*8),bg="#000000",relief="flat",highlightthickness=0,border=0)
can.place(in_=root,x=0,y=0)
can.bind("<Button-1>",can_b1)







load_im()



intro()


cpu_move()

root.mainloop()