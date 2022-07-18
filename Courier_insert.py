from tkinter import *
root = Tk()

import psycopg2


root.title("COURIER SERVICE")


#conn = psycopg2.connect(host="localhost",database="courierservice",user="postgres",password="Jairus@2520")

#c = conn.cursor()

def submit():
    conn = psycopg2.connect(host="localhost",database="courierservice",user="postgres",password="Jairus@2520")

    c = conn.cursor()

    #insert into table
    
    c.execute("INSERT INTO customer(cust_id,cust_name,cust_pho,cust_email,cust_ddr) " +"VALUES(%s,%s,%s,%s,%s)",(cust_id.get(),cust_name.get(),cust_pho.get(),cust_email.get(),cust_ddr.get()))
            
    c.execute("select *from customer")
    
    c.execute("INSERT INTO courier(courier_id,courier_name,courier_type,courier_weight,courier_s_id) " +"VALUES(%s,%s,%s,%s,%s)",(courier_id.get(),courier_name.get(),courier_type.get(),courier_weight.get(),courier_s_id.get()))

    c.execute("select *from courier")
    conn.commit()
    row=c.fetchall()
    print(row)
    
#create text boxes
cust_id = Entry(root,width=30)
cust_id.grid(row=1 , column =1)

cust_name = Entry(root,width=30)
cust_name.grid(row=2 , column =1)

cust_pho = Entry(root,width=30)
cust_pho.grid(row=3 , column =1)

cust_email = Entry(root,width=30)
cust_email.grid(row=4 , column =1)

cust_ddr = Entry(root,width=30)
cust_ddr.grid(row=5 , column =1)

courier_id = Entry(root,width=30)
courier_id.grid(row=8 , column =1)

courier_name = Entry(root,width=30)
courier_name.grid(row=9 , column =1)

courier_type = Entry(root,width=30)
courier_type.grid(row=10 , column =1)

courier_weight = Entry(root,width=30)
courier_weight.grid(row=11 , column =1)

courier_s_id = Entry(root,width=30)
courier_s_id.grid(row=12 , column =1)



#to create labels
cust_id_label=Label(root,text="customer id")
cust_id_label.grid(row=1,column=0)

cust_name_label=Label(root,text="Name")
cust_name_label.grid(row=2,column=0)

cust_pho_label=Label(root,text="Phone no")
cust_pho_label.grid(row=3,column=0)

cust_email_label=Label(root,text="mail id")
cust_email_label.grid(row=4,column=0)

cust_ddr_label=Label(root,text="Address")
cust_ddr_label.grid(row=5,column=0)

courier_id_label=Label(root,text="courier")
courier_id_label.grid(row=6,column=0)

courier_id_label=Label(root,text="courier_id")
courier_id_label.grid(row=8,column=0)

courier_name_label=Label(root,text="courier name")
courier_name_label.grid(row=9,column=0)

courier_type_label=Label(root,text="type")
courier_type_label.grid(row=10,column=0)

courier_weight_label=Label(root,text="weight")
courier_weight_label.grid(row=11,column=0)

courier_s_id_label=Label(root,text="sender_Id")
courier_s_id_label.grid(row=12,column=0)

#to create a submit button
submit_btn = Button(root,text="Submit",command=submit)
submit_btn.grid(row=15 , column=3 )
