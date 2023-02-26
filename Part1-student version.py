
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.    # Any code taken from other sources is referenced within my code solution.  
  
# Student ID:20211525               # Date:  16.04.2022





k=0
j=0
i=0
l=0

credit_pass=0
credit_defer=0
credit_fail=0


progress_count=0
module_trailer_count=0
module_retriever_count=0
Exclude_count=0

while True:
     while k<1:
     
       try:
          credit_pass =int(input("please enter your credits at pass: "))      #validations
          if 0 <= credit_pass <= 120 and credit_pass % 20 == 0:
            break            
          else:
            print( "out of range")
       except:
           print("Integer required")
     k+=1
     while j<1:

           try:
                credit_defer=int(input("please enter your credits at defer: "))
                if 0 <= credit_defer  <= 120 and credit_defer  % 20 == 0:
                    break            
                else:
                   print( "out of range")
           except :
                print("Integer required")
     j+=1
     while l<1:        

           try:
                credit_fail=int(input("please enter your credits at fail: "))
                if 0 <=credit_fail  <= 120 and credit_fail % 20 == 0:
                    break            
                else:
                   print( "out of range")
           except ValueError:
                print("Integer required")
     l+=1 

     while i<1:
          
                total =credit_pass + credit_defer+ credit_fail
                if total>120 :
                     print("Total incorrect")
                     break
                elif credit_pass==120 and credit_defer==0 and credit_fail==0 :
                      print("Progress")
                      break
                elif credit_pass==100 and 0<=credit_defer<=20 and  0<=credit_fail<=20:
                    print("Progress (module trailer)")                    
                    break
                elif 0<= credit_pass<=80 and 0<=credit_defer<=120 and 0<=credit_fail<=60:
                       print("module retriever")                      
                       break
                elif 0<=credit_pass<=40 and 0<=credit_defer<=40 and 80<=credit_fail<=120:
                       print("Exclude")
                       break
     i=i+1

