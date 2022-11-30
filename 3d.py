import tkinter as t 
import math

def get_coord(x,y,z):
	global center


	w=100000
	h=900-2

	cx=1440/2
	cy=h/2
	center=[cx,cy]


	zz=50+z

	w=100000
	h=900-2

	in_ax=math.atan(((w)/(2*zz)))
	in_ax*=57.2958


	in_ay=math.atan(((h)/(2*zz)))
	in_ay*=57.2958



	ww=50*math.tan(math.radians(in_ax))
	hh=50*math.tan(math.radians(in_ay))


	v1=50028.080935786355
	v2=449.00213084900463


	xx=cx+(x*ww/v1)
	yy=cy-(y*hh/v2)



	return xx,yy
def draw_floor():
	global can
	#100,20

	vy=449.00213084900463


	ar=[]

	x_=-50028.080935786355
	for a in range(1000):
		x1,y1=get_coord(x_,-vy,0)
		ar.append([x1,y1])
		x_+=100

	z=15
	cnt=0
	for a in range(40):
		
		x_=-50028.080935786355

		ar1=[]
		cnt=0
		
		for b in range(1000):

			x1,y1=get_coord(x_,-vy,z)
			x2,y2=get_coord(x_+100,-vy,z)

			try:
				can.create_polygon(ar[cnt][0],ar[cnt][1],x1,y1,x2,y2,ar[cnt+1][0],ar[cnt+1][1],fill="#111111",outline="#555555")
			except:
				pass
			ar1.append([x1,y1])

			x_+=100
			cnt+=1
		ar=ar1

		z+=15





def up_(e):

	print(e.char)
	

root=t.Tk()
root.wm_attributes("-fullscreen",1)
can=t.Canvas(width=1440,height=900,relief="flat",highlightthickness=0,border=0,bg="#000000")
can.bind("<KeyPress>",up_)
can.place(in_=root,x=0,y=0)
draw_floor()

ground=-449.00213084900463

x1,y1=get_coord(-500,ground,100)
x2,y2=get_coord(500,ground,100)


x3,y3=get_coord(500,ground,0)
x4,y4=get_coord(-500,ground,0)


x5,y5=get_coord(-100,-300,100)
x6,y6=get_coord(100,-300,100)


x7,y7=get_coord(100,-300,110)
x8,y8=get_coord(-100,-300,110)


x9,y9=get_coord(0,ground,100)
x10,y10=get_coord(0,-ground,100)

can.create_line(x1,y1, x2,y2, x3,y3, x4,y4, x1,y1,fill="gold")
#can.create_line(x5,y5, x6,y6, x7,y7, x8,y8, x5,y5,fill="red")


can.create_line(x9,y9,x10,y10,fill="red")



#can.create_line(x1,y1, x2,y2,fill="red")







can.focus_set()
root.mainloop()