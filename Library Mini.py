#transachange_password table
#create table transachange_password1(tid int primary key,changing_time datetime,transaction_change_password varchar(50),id int,foreign key(id)references reglogin1(id));
#alter table transachange_password1 modify column tid int auto_increment;

#library table
#create table library1(id int primary key auto_increment,name varchar(50),author varchar(50),price float,type varchar(50));

#cart table
#create table cart1(cartid int primary key auto_increment,name varchar(50),author varchar(50),price float,email varchar(50),quantity int);
#alter table cart1 add type varchar(50);

#admin table
#create table admin1(username varchar(50),password varchar(50));
#insert into admin1 values('John',123);

#reglogin table
#create table reglogin1(id int primary key auto_increment,name varchar(50),email varchar(50),password varchar(50));
#ALTER table reglogin1 add contactno varchar(15);

#ORDERS table
#create table orders1(oid int primary key auto_increment,book_name varchar(50),price float,email varchar(50),quantity int,ord_date varchar(50),total_amt float,id int);
#alter table orders1 drop column total_amt;



import datetime
import mysql.connector
import re
import sys
count=4
class transaction:
    def __init__(self):
        self.conn=mysql.connector.connect(host='localhost',user='root',password='7777777',database='student')
        self.cur=self.conn.cursor()
        self.entermailId=None
        

    def admin(self):
        username=input('Enter username:'.center(175))
        password=input('Enter password:'.center(175))
        
        query='select password,username from admin1 where username=%s'
        values=(username,)
        self.cur.execute(query,values)
        data=self.cur.fetchone()
        if data:
            passwd=data[0]
            if passwd==password:
                print('Login Successfull'.center(175))
            else:
                print('Invallid Credentials'.center(175))
    def insert(self):
        
        bookname=input('Enter book name:'.center(175))
        authername=input('Enter Author name:'.center(175))
        bookprice=int(input('Enter book Price:'.center(175)))
        Typebook=input('Enter book Type:'.center(175))
        
        query='insert into library1(name,author,price,type)values(%s,%s,%s,%s)'
        values=(bookname,authername,bookprice,Typebook)
        self.cur.execute(query,values)
        print('Value addedd successfully'.center(175))
        self.conn.commit()

    def update_entire_row(self):
        
        id=int(input('Enter Id:'.center(175)))
        name=(input('Enter name:'.center(175)))
        author=(input('Enter author:'.center(175)))
        price=int(input('EnIdter price:'.center(175)))
        type=(input('Enter type:'.center(175)))


        query='update library1 set name=%s,author=%s,price=%s,type=%s where id=%s '
        values=(name,author,price,type,id)
        self.cur.execute(query,values)
        print('Value addedd successfully'.center(175))
        self.conn.commit()

    # def update_specific_row(self):
    #     id=int(input('Enter Id:'))
    #     name=(input('Enter name:'))
    #     author=(input('Enter author:'))
    #     query='update library1 set name=%s,author=%s where id=%s'  # give choice what you want to update select option
    #     values=(name,author,id)
    #     self.cur.execute(query,values)
    #     print('Value addedd successfully')
    #     self.conn.commit()


    def name(self):
        id=int(input('Enter Id:'.center(175)))
        name=(input('Enter name:'.center(175)))
        query='update library1 set name=%s where id=%s'  
        values=(name,id)
        self.cur.execute(query,values)
        print('Name added successfully'.center(175))
        self.conn.commit()
    
    def Author(self):
        id=int(input('Enter Id:'.center(175)))
        author=(input('Enter author:'.center(175)))
        query='update library1 set author=%s where id=%s'  
        values=(author,id)
        self.cur.execute(query,values)
        print('Author added successfully'.center(175))
        self.conn.commit()

    def price(self):
        id=int(input('Enter Id:'))
        price=(input('Enter price:'))
        query='update library1 set price=%s where id=%s'  
        values=(price,id)
        self.cur.execute(query,values)
        print('price added successfully'.center(175))
        self.conn.commit()

    def Type(self):
        id=int(input('Enter Id:'.center(175)))
        type=(input('Enter book type:'.center(175)))
        query='update library1 set type=%s where id=%s'  
        values=(type,id)
        self.cur.execute(query,values)
        print('type of book added successfully'.center(175))
        self.conn.commit()
        
            
    def delete(self):
        bookId=int(input('Enter book Id:'.center(175)))
        
        query='delete from library1 where id=%s'
        values=(bookId,)
        self.cur.execute(query,values)
        if self.cur.rowcount > 0:
            print('Data deleted successfully'.center(175))
            self.conn.commit()
        else:
            print('No data found for book Id'.center(175), bookId)
        self.conn.commit()

    def display_all(self):
        query='select *from library1 '
        self.cur.execute(query)
        data=self.cur.fetchall()
        for i in data:
            print(i.center(175))


    def display_one(self):
        bookId=int(input('Enter book Id:'.center(175)))
        query='select *from library1 where id=%s'
        values=(bookId,)
        self.cur.execute(query,values)
        data=self.cur.fetchone()
        print(data.center(175))

    def show_customer_orders(self):
        query='select *from reglogin1 '
        self.cur.execute(query)
        data=self.cur.fetchall()
        for i in data:
            print(i)
  
    def show_single_customer(self):
        id=int(input('Enter Id:'.center(175)))
        password=(input('Enter password:'.center(175)))
        query='select * from reglogin1 where id=%s '  
        values=(id,)
        self.cur.execute(query,values)
        data=self.cur.fetchone()
        if data:
            passwd=data[3]
            if passwd==password:
                print(data)
                self.conn.commit()
            else:
                print('Invallid Credentials'.center(175))
        else:
            print('Invalid ID'.center(175))

    def show_multiple_customer(self):
        query='select *from reglogin1'
        self.cur.execute(query)
        data=self.cur.fetchall()
        for i in data:
            print(i)
        

    def orders(self):
        pass
    
    def registeration(self):
        entername=input('Enter your name:'.center(175))
        enteremailId=input('Enter your EmailId:'.center(175))
        print('Your password must have at least one upper case one special case character and at least one integer value'.center(175))
        enterpass=input('Create your password'.center(175))
        if len(enterpass) >= 8:
            if any(char.isupper() for char in enterpass) and any(char.isdigit() for char in enterpass) and any(char in '!@#$%^&*()[]{};:,./<>?\|`~' for char in enterpass):
                entercontactno=input('Enter your Contact Number:'.center(175))
                #if len(entercontactno)==10 or len(entercontactno)==8 or len(entercontactno)==7:
                a=re.fullmatch('[7-9][0-9]{9}',entercontactno)
                if a!=None:
                    query='insert into reglogin1(name,email,password,contactno)values(%s,%s,%s,%s)'
                    values=(entername,enteremailId,enterpass,entercontactno)
                    self.cur.execute(query,values)
                    print('Registeration complete'.center(175))
                    self.conn.commit()
                else:
                    print('Mobile number should be 7,8 and 9 digit and Start with 7,8 and 9 digit'.center(175))
            else:
                print('password must start with capital letter and contain special character'.center(175))
        else:
            print('password should not be less than 8 digit'.center(175))
    
    def login(self):
        global count
        #global enteremailId
        self.enteremailId=input('Enter your EmailId:'.center(175))
        #for i in range(count):
        while count>0:
            print(f'You have {count} attempt'.center(175))
            count-=1
            #enteremailId=input('Enter your EmailId:'.center(175))
            enterpass=input('Enter your password'.center(175))
            query='select *from reglogin1 where email=%s and password=%s'
            values=(self.enteremailId,enterpass)
            self.cur.execute(query,values)
            data=self.cur.fetchone()
            if data:
                if data[3]==str(enterpass):
                    print('Login Successfull :)'.center(175))
                    query='select name,author,price,type from cart1 where email=%s'
                    values=(self.enteremailId,)
                    self.cur.execute(query,values)
                    data=self.cur.fetchall()
                    if data:
                        print('============================================================================='.center(175))
                        print('| Name           | Author       | Price       | type      |'.center(175))
                        print('============================================================================='.center(175))
                        for i in data:
                            name,author,price,type= i
                            print('============================================================================='.center(175))
                            print(f"| {name}    | {author}     | {price}     | {type}   |".center(175))
                            print('============================================================================='.center(175))  
                            return True  
                    else:
                        print('Cart is Empty'.center(175))   
                else:
                    count -= 1
                    print('Invalid email or password. Please try again.'.center(175))
                    return False
        else:
            print('You have reached maximum login attempt'.center(175))
                        
                        

                    
    def forgotpass(self):
        #enteremailId=input('Enter your EmailId:'.center(175))
        query='select password from reglogin1 where email=%s'
        values=(self.enteremailId,)
        self.cur.execute(query,values)
        data=self.cur.fetchone()
        if data:
            print(f'Your Password is:{data[0]}'.center(175))
        else:
            print('No password is set for user email id'.center(175))


    def reset(self):
        enterId=int(input('Enter Your Id:'.center(175)))
        #enteremailId=input('Enter your EmailId:'.center(175))
        
        enternewpass=input('Enter new password:'.center(175))

        query='select transaction_change_password from transachange_password1 where id=%s order by transaction_change_password desc limit 3'
        values=(enterId,)
        self.cur.execute(query,values)
        data=self.cur.fetchall()
        for i in data:
            if i[0]==str(enternewpass):
                print('Sorry your new password can not be same as last 3 password'.center(175))   
                break
        else:
            
            transactiontime=datetime.datetime.today()
            query='insert into transachange_password1(changing_time,transaction_change_password,id)values(%s,%s,%s)'
            values=(transactiontime,enternewpass,enterId)
            self.cur.execute(query,values)

            query='update reglogin1 set password=%s where email=%s and id=%s'
            values=(enternewpass,self.enteremailId,enterId)
            self.cur.execute(query,values)
            self.conn.commit()
            print('Password Reset Successfull :)'.center(175)) 
    
        
    def orderbook(self):
        #global enteremailId
        print('Enter name of book to place order'.center(175))
        bname=input('Enter Book name:'.center(175))
        price=int(input('Enter price:'.center(175)))
        #emailId=input('Enter Your emailId:'.center(175))
        copies=int(input('How many copies/quantity you want to order'.center(175)))
        author=input('Enter order date:'.center(175))
        type=input('Which type of book you want to order:'.center(175))
        query='insert into cart1(name,author,price,email,quantity,type)values(%s,%s,%s,%s,%s,%s)'
        values=(bname,author,price,self.enteremailId,copies,type)
        self.cur.execute(query,values)
        print('Your Books are added to cart successfully'.center(175))
        self.conn.commit()
        return True
        

    def gotocart(self):
        #global enteremailId
        #enteremailId=input('Enter email:'.center(175))
        print('Book in your cart are'.center(175))
        query='select name,author,price,email,quantity from cart1 where email=%s'
        values=(self.enteremailId,)
        self.cur.execute(query,values)
        data=self.cur.fetchall()
        if data:
            print('============================================================================='.center(175))
            print('| Name           | Author       | Price       | email       | quantity|'.center(175))
            print('============================================================================='.center(175))
            for i in data:
                name,author,price,email,quantity= i
                print(f"| {name}    | {author}      | {price}     | {email}   | {quantity}".center(175))
            print('============================================================================='.center(175))

            return True

    def removeitems(self):
        #global enteremailId
        bname=input('Enter Book name you want to remove:'.center(175))
        #emailId=input('Enter email:'.center(175))
        query='delete from cart1 where email=%s'
        values=(self.enteremailId,)
        self.cur.execute(query,values)
        self.conn.commit()
        print('Book remove from your cart are')
        query='select name from cart1 where email=%s'
        values=(self.enteremailId,)
        self.cur.execute(query,values)
        data=self.cur.fetchall()
        if data:
            for i in data:
                name,author,price,email,quantity= i
                print(f"| {name}    | {author}                | {price}           | {email} | {quantity}".center(175))
            print('============================================================================='.center(175))

        else:
            print('No data found') 
    def gotopayment(self):
        #global enteremailId
        #emailId=input('Enter email:'.center(175))
        print('Book in your cart are'.center(175))
        query='select name,author,price,type,quantity from cart1 where email=%s'
        values=(self.enteremailId,)
        self.cur.execute(query,values)
        data=self.cur.fetchall()
        if data:
            print('============================================================================='.center(175))
            print('| Name       | Author       | Price      | type      |quantity|'.center(175))
            print('============================================================================='.center(175))
            for i in data:
                name,author,price,email,quantity= i
                print(f"| {name}    | {author}                | {price}           | {email} | {quantity}".center(175))
            print('============================================================================='.center(175))
            query='select price from cart1 where email=%s'
            values=(self.enteremailId,)
            self.cur.execute(query,values)
            data=self.cur.fetchone()
            #print('total amount of your order is RS.',data[0].center(175))
            print(f'total amount of your order is RS. {data[0]}'.center(175))
            print('1.Complete Payment'.center(175))
            print('2.Exit'.center(175))
            choice=int(input('Enter Your Choice:'.center(175)))
            if choice==1:
                print('PAYMENT SUCCESSFULL'.center(175))
                sys.exit()
            elif choice==2:
                print('Exit'.center(175))
                sys.exit()
            else:
                print('Wrong Choice'.center(175))
                
    def changequantity(self):
        #global enteremailId
        #emailId=input('Enter email:'.center(175))2

        qty=int(input('Enter quantity you want'.center(175)))
        query='update cart1 set quantity=%s where email=%s'
        values=(qty,self.enteremailId)
        self.cur.execute(query,values)
        self.conn.commit()
        data=self.cur.fetchall()
        if data:
            for i in data:
                name,author,price,email,quantity= i
                print(f"| {name}    | {author}                | {price}           | {email} | {quantity}")
            print('=============================================================================')
            
    def shopmore(self):
        print('Enter name of book to place order'.center(175))
        bname=input('Enter Book name:'.center(175))
        price=int(input('Enter price:'.center(175)))
        #emailId=input('Enter Your emailId:'.center(175))
        copies=int(input('How many copies/quantity you want to order'.center(175)))
        author=input('Enter order date:'.center(175))
        type=input('Which type of book you want to order:'.center(175))
        query='insert into cart1(name,author,price,email,quantity,type)values(%s,%s,%s,%s,%s,%s)'
        values=(bname,author,price,self.enteremailId,copies,type)
        self.cur.execute(query,values)
        print('Your Books are added to cart successfully'.center(175))
        self.conn.commit()


    def placeorder(self):
        
        query='select name,author,price type from cart1 where email=%s'
        values=(self.enteremailId,)
        self.cur.execute(query,values)
        data=self.cur.fetchall()
        if data:
            print('Book In your cart are'.center(175))
            print('============================================================================='.center(175))
            print('| Name       | Author       | Price      |'.center(175))
            print('============================================================================='.center(175))
            for i in data:
                name,author,price= i
                print('============================================================================='.center(175))
                print(f"| {name}    | {author}                | {price}   |".center(175))
                print('============================================================================='.center(175)) 
                return True 

a=transaction()
while True:
    print('*******************************WELCOME TO Our Library********************************'.center(175))
    print('1.Admin'.center(175))
    print('2.Customer'.center(175))
    print('6.Exit'.center(175))
    print('*************************************************************************************'.center(175))

    choice=int(input('Enter your choice:'.center(175)))      

    if choice==1:
        a.admin()
        while True:
            print('*************************************************************************************'.center(175))
            print('1.Insert'.center(175))
            print('2.Update'.center(175))
            print('3.Delete'.center(175))
            print('4.Display'.center(175))
            print('5.show customer'.center(175))
            print('6.Orders'.center(175))
            print('7.Exit'.center(175))
            admin_choice=int(input('Enter your choice:'.center(175)))
            if admin_choice == 1:
                a.insert()
            elif admin_choice == 2:
                print('1.update entire row'.center(175))
                print('2.update specific row'.center(175))
                print('3.Exit'.center(175))
                admin_update_choice=int(input('Enter your choice:'.center(175)))
                if admin_update_choice==1:
                    a.update_entire_row()
                elif admin_update_choice==2:
                    while True:
                        print('What you want to update'.center(175))
                        print('1.Name'.center(175))
                        print('2.Author'.center(175))
                        print('3.price'.center(175))
                        print('4.Type'.center(175))
                        print('5.Exit'.center(175))
                        admin_update_specific_row=int(input('Enter your choice:'.center(175)))
                        if admin_update_specific_row==1:
                            a.name()
                        elif admin_update_specific_row==2:
                            a.Author()
                        elif admin_update_specific_row==3:
                            a.price()
                        elif admin_update_specific_row==4:
                            a.Type()
                        elif admin_update_specific_row==5:
                            print('Thank you'.center(175))
                            break
                        else:
                            print('Wrong choice'.center(175))
                elif admin_update_choice==3:
                    print('Thank you'.center(175))
                    break    
                else:
                    print('Wrong choice'.center(175))
            elif admin_choice == 3:
                a.delete()
            elif admin_choice == 4: 
                print('1.Display all record'.center(175))
                print('2.Display one record'.center(175))
                print('3.Exit'.center(175))
                admin_display_choice=int(input('Enter your choice:'.center(175)))

                if admin_display_choice==1:
                    a.display_all()
                elif admin_display_choice==2:
                    a.display_one()
                elif admin_display_choice==3:
                    print('Thank you'.center(175))
                    break
                else:
                    print('wrong choice'.center(175))

            elif admin_choice == 5:
                print('1.Show single customer'.center(175))
                print('2.Show multiple customer'.center(175))
                print('3.Exit'.center(175))
                admin_show_customer_choice=int(input('Enter your choice:'.center(175)))

                if admin_show_customer_choice==1:
                    a.show_single_customer()
                elif admin_show_customer_choice==2:
                    a.show_multiple_customer()
                elif admin_show_customer_choice==3:
                    print('Thank you'.center(175))
                    break
                else:
                    print('wrong choice'.center(175))

            elif admin_choice == 6:
                a.orders()
            elif admin_choice == 7:
                print('Exiting admin operations...'.center(175))
                break
            else:
                print('Wrong choice'.center(175))
 
    elif choice==2: 
        while True:
            print('*************************************************************************************'.center(175))
            print('1.Registeration'.center(175))
            print('2.Login'.center(175))
            print('3.Exit'.center(175))
            customer_choice=int(input('Enter your choice:'.center(175)))
            if customer_choice==1:
                a.registeration()
            elif customer_choice==2:
                log=a.login()
                if log==True:
                    while True:
                        print('1.Order book'.center(175))
                        print('2.Go To Cart'.center(175))
                        print('3.Exit'.center(175))
                        orderoption_choice=int(input('Enter your choice:'.center(175)))
                        if orderoption_choice==1:
                            ob=a.orderbook()
                            if ob==True:
                                while True:
                                    print('1.Shop More'.center(175))
                                    print('2.Place Order'.center(175))
                                    print('3.Exit'.center(175))
                                    choice=int(input('Enter your choice:'.center(175)))
                                    if choice==1:
                                        a.shopmore()
                                    elif choice==2:
                                        a.placeorder()
                                        plcodr=a.placeorder()
                                        if plcodr==True:
                                           while True:
                                                print('1.Remove Items from cart'.center(175))
                                                print('2.Go to payment page'.center(175))
                                                print('3.Change Quantity'.center(175))
                                                print('4.Exit'.center(175))
                                                gotocart_choice=int(input('Enter your choice:'.center(175)))
                                                if gotocart_choice==1:
                                                    a.removeitems()
                                                elif gotocart_choice==2:
                                                    a.gotopayment() 
                                                elif gotocart_choice==3:
                                                    a.changequantity()
                                                elif gotocart_choice==4:
                                                    print('Exit'.center(175)) 
                                                    break
                                                else:
                                                    print('Wrong Choice'.center(175)) 
                                    elif choice==3:
                                        print('Exit'.center(175))
                                    else:
                                        print('Wrong Choice'.center(175))
                        elif orderoption_choice==2:
                            gtc=a.gotocart()
                            if gtc==True:
                                while True:
                                    print('1.Remove Items from cart'.center(175))
                                    print('2.Go to payment page'.center(175))
                                    print('3.Change Quantity'.center(175))
                                    print('4.Exit'.center(175))
                                    gotocart_choice=int(input('Enter your choice:'.center(175)))
                                    if gotocart_choice==1:
                                        a.removeitems()
                                    elif gotocart_choice==2:
                                        a.gotopayment() 
                                    elif gotocart_choice==3:
                                        a.changequantity()
                                    elif gotocart_choice==4:
                                        print('Exit'.center(175)) 
                                        break
                                    else:
                                        print('Wrong Choice'.center(175))
                        elif orderoption_choice==3:
                            print('Exit'.center(175)) 
                            break
                        else:
                            print('Wrong Choice'.center(175))
                else:
                    while True:
                        print('1.Forgot password'.center(175))
                        print('2.Reset password'.center(175))
                        print('3.Exit'.center(175))
                        choice=int(input('Enter your choice:'.center(175)))
                        if choice==1:
                            a.forgotpass()
                        elif choice==2:
                            a.reset()
                        elif choice==3:
                            print('Exit'.center(175))
                            break
                        else:
                            print('Wrong Choice'.center(175))        
                           
            elif customer_choice==3:
                print('Exit'.center(175))
                break
            else:
                print('Wrong Choice'.center(175))
    elif choice==3:
        print('Exit'.center(175))
        print('Thank you'.center(175))
        a.conn_close()
        break        
    else:
        print('Wrong Choice'.center(175))





