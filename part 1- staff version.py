#Main Part-01
   

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.    # Any code taken from other sources is referenced within my code solution.  
  
# Student ID:20211525               # Date:16.04,2022




credit_pass=0
credit_defer=0
credit_fail=0


progress_count=0
module_trailer_count=0
module_retriever_count=0
Exclude_count=0


while True:
     while True:
     
       try:
          credit_pass =int(input("please enter your credits at pass: "))      #validations
          if 0 <= credit_pass <= 120 and credit_pass % 20 == 0:
            break            
          else:
            print( "out of range")
       except:
           print("Integer required")
           

     while True:
           try:
                credit_defer=int(input("please enter your credits at defer: "))
                if 0 <= credit_defer  <= 120 and credit_defer  % 20 == 0:
                    break            
                else:
                   print( "out of range")
           except :
                print("Integer required")
               
          
     while True:
           try:
                credit_fail=int(input("please enter your credits at fail: "))
                if 0 <=credit_fail  <= 120 and credit_fail % 20 == 0:
                    break            
                else:
                   print( "out of range")
           except ValueError:
                print("Integer required")
               
     while True:
          
                total =credit_pass + credit_defer+ credit_fail
                if total>120  :
                     print("Total incorrect")
                     break
                elif credit_pass==120 and credit_defer==0 and credit_fail==0 :
                      print("Progress")
                      progress_count=progress_count+1
                      break
                elif credit_pass==100 and 0<=credit_defer<=20 and  0<=credit_fail<=20:
                    print("Progress (module trailer)")
                    module_trailer_count+=1
                    break
                elif 0<= credit_pass<=80 and 0<=credit_defer<=120 and 0<=credit_fail<=60:
                       print("module retriever")
                       module_retriever_count+=1
                       break
                elif 0<=credit_pass<=40 and 0<=credit_defer<=40 and 80<=credit_fail<=120:
                       print("Exclude")
                       Exclude_count+=1
                       break
                      
     def histogram_print():
         
            print("\n")
          
            print("Horizontal Histogram\n")                         #printing the horizontal histogram
            print("Progress_count",  " :", "*" * progress_count)
            print("module_trailer_count",  "  :", "*" * module_trailer_count)
            print("module_retriever_count",  ":", "*" *module_retriever_count)
            print("Exclude_count", " :", "*" *Exclude_count)
            total_outcomes =(progress_count) +(module_trailer_count) +(module_retriever_count) + (Exclude_count)
            print("\n")
            print(total_outcomes, "outcomes in total.")
            exit()
        


         

     while True:
        print("\n")
        try:   
           answer= input("Would you like to enter another set of data?\n"                #checking the option
                          "Enter 'y' for yes or 'q' to quit and view results: ")
        except ValueError:
            print("Please Enter 'y' or 'q'")
            
        else:
            if answer == "q":
               
                histogram_print()
                break

            elif answer== "y":
                pass
                break

            else:
                print("Please Enter 'y' or 'q'")
                
             
                 
                    
