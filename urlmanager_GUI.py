from tkinter import *
from tkinter import messagebox,ttk
import pyshorteners
import webbrowser

tk=Tk()
tk.title("URL MANAGER | MANJUNATHAN C")
tk.configure(bg="black")
tk.geometry("253x250")
button_1=Button(text="URL SHORT",fg="white",bg="red",command=lambda: press('S'),height=4,width=28)
button_1.place(x=0,y=0)

button_1=Button(text="URL EXPAND",fg="white",bg="green",command=lambda: press('E'),height=4,width=28)
button_1.place(x=0,y=171)

button_2=Button(text="EXIT",fg="blue",bg="white",command=tk.quit,height=4,width=28)
button_2.place(x=0,y=85)

def press(key):
	if(key=='S'):
		short()
	if(key=='E'):
		expand()

OPTIONS=["TINYURL","CHILP.IT","CLCK.RU","CUTT.LY","GIT.IO(GITHUB URLS ONLY)","DA.GD","NULLPOINTER","OS.DB","OW.LY","QPS.RU","IS.GD"]

def short():

	def action(event):

		url=entry.get()
		p=pyshorteners.Shortener()
		
		try:
			if(option.get()==OPTIONS[0]):
				try:
					messagebox.showinfo("Success",p.tinyurl.short(url))
				except :
					messagebox.showerror("Failed", "Unknown Error") 		
				

			elif(option.get()==OPTIONS[1]):
				try:
					messagebox.showinfo("Success",p.chilpit.short(url))
				except:
					messagebox.showerror("Failed", "Unknown Error") 
			elif(option.get()==OPTIONS[2]):
				try:
					messagebox.showinfo("Success",p.clckru.short(url))	
				except  :
					messagebox.showerror("Failed", "Unknown Error") 

			elif(option.get()==OPTIONS[3]):
				try:
					messagebox.showinfo("Success",p.cuttly.short(url))
				except  :
					messagebox.showerror("Failed", "Unknown Error") 

			elif(option.get()==OPTIONS[4]):
				try:
					messagebox.showinfo("Success",p.gitio.short(url))	
				except  :
					messagebox.showerror("Failed", "Unknown Error") 

			elif(option.get()==OPTIONS[5]):
				try:
					messagebox.showinfo("Success",p.dagd.short(url))	
				except  :
					messagebox.showerror("Failed", "Unknown Error") 

			elif(option.get()==OPTIONS[6]):
				try:
					messagebox.showinfo("Success",p.nullpointer.short(url))	
				except  :
					messagebox.showerror("Failed", "Unknown Error") 

			elif(option.get()==OPTIONS[7]):
				try:
					messagebox.showinfo("Success",p.osdb.short(url))	
				except  :
					messagebox.showerror("Failed", "Unknown Error") 

			elif(option.get()==OPTIONS[8]):
				try:
					messagebox.showinfo("Success",p.owly.short(url))	
				except  :
					messagebox.showerror("Failed", "Unknown Error") 


			elif(option.get()==OPTIONS[9]):
				try:
					messagebox.showinfo("Success",p.qpsru.short(url))	
				except  :
					messagebox.showerror("Failed", "Unknown Error") 

			elif(option.get()==OPTIONS[10]):
				try:
					messagebox.showinfo("Success",p.isgd.short(url))	
				except  :
					messagebox.showerror("Failed", "Unknown Error") 
		except:
			messagebox.showerror("Failed", "Unknown Error") 

	tk=Tk()
	tk.title("SHORTENER | MANJUNATHAN C")
	tk.configure(bg="red")

	lab1=Label(tk,text="ENTER THE URL YOU WANT TO SHORT ").grid(padx=10,pady=10)

	entry=Entry(tk,width=70,borderwidth=10,font=("fontawesome",15,"bold italic"))
	entry.grid(padx=90,rowspan=2,pady=20)
	
	option = ttk.Combobox(tk,value=OPTIONS)
	option.current(0)
	option.bind("<<ComboboxSelected>>",action)
	option.grid()

	tk.mainloop()
	

def expand():

	def action(event):

		url=entry.get()
		p=pyshorteners.Shortener()
		
		try:
			if(option.get()==OPTIONS[0]):
				try:
					messagebox.showinfo("Success",p.tinyurl.expand(url))
					webbrowser.open(p.tinyurl.expand(url))
				except :
					messagebox.showerror("Failed", "Unknown Error") 		
				

			elif(option.get()==OPTIONS[1]):
				try:
					messagebox.showinfo("Success",p.chilpit.expand(url))
					webbrowser.open(p.chilpit.expand(url))
				except:
					messagebox.showerror("Failed", "Unknown Error") 
			elif(option.get()==OPTIONS[2]):
				try:
					messagebox.showinfo("Success",p.clckru.expand(url))
					webbrowser.open(p.clckru.expand(url))	
				except  :
					messagebox.showerror("Failed", "Unknown Error") 

			elif(option.get()==OPTIONS[3]):
				try:
					messagebox.showinfo("Success",p.cuttly.expand(url))
					webbrowser.open(p.cuttly.expand(url))
				except  :
					messagebox.showerror("Failed", "Unknown Error") 

			elif(option.get()==OPTIONS[4]):
				try:
					messagebox.showinfo("Success",p.gitio.expand(url))	
					webbrowser.open(p.gitio.expand(url))
				except  :
					messagebox.showerror("Failed", "Unknown Error") 

			elif(option.get()==OPTIONS[5]):
				try:
					messagebox.showinfo("Success",p.dagd.expand(url))	
					webbrowser.open(p.dagd.expand(url))
				except  :
					messagebox.showerror("Failed", "Unknown Error") 

			elif(option.get()==OPTIONS[6]):
				try:
					messagebox.showinfo("Success",p.nullpointer.expand(url))	
					webbrowser.open(p.nullpointer.expand(url))
				except  :
					messagebox.showerror("Failed", "Unknown Error") 

			elif(option.get()==OPTIONS[7]):
				try:
					messagebox.showinfo("Success",p.osdb.expand(url))	
					webbrowser.open(p.osdb.expand(url))
				except  :
					messagebox.showerror("Failed", "Unknown Error") 

			elif(option.get()==OPTIONS[8]):
				try:
					messagebox.showinfo("Success",p.owly.expand(url))	
					webbrowser.open(p.owly.expand(url))
				except  :
					messagebox.showerror("Failed", "Unknown Error") 


			elif(option.get()==OPTIONS[9]):
				try:
					messagebox.showinfo("Success",p.qpsru.expand(url))	
					webbrowser.open(p.qpsru.expand(url))
				except  :
					messagebox.showerror("Failed", "Unknown Error") 

			elif(option.get()==OPTIONS[10]):
				try:
					messagebox.showinfo("Success",p.isgd.expand(url))	
					webbrowser.open(p.isgd.expand(url))
				except  :
					messagebox.showerror("Failed", "Unknown Error") 
		except:
			messagebox.showerror("Failed", "Unknown Error") 

	tk=Tk()
	tk.configure(bg="green")
	tk.title("EXPANDER | MANJUNATHAN C")

	lab1=Label(tk,text="ENTER THE SHORTENED URL YOU WANT TO EXPAND").grid(padx=10,pady=10)

	entry=Entry(tk,width=70,borderwidth=10,font=("fontawesome",15,"bold italic"))
	entry.grid(padx=80,rowspan=2,pady=10)
	
	option = ttk.Combobox(tk,value=OPTIONS)
	option.current(0)
	option.bind("<<ComboboxSelected>>",action)
	option.grid()

	tk.mainloop()




tk.mainloop()

