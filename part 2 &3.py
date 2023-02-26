  
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.    # Any code taken from other sources is referenced within my code solution.  
  
# Student ID: 20211525        # Date: 2022.04.16
credit_pass=0
credit_defer=0
credit_fail=0


progress_count=0
module_trailer_count=0
module_retriever_count=0
exclude_count=0

progress=' ' 
trailer=' ' 
retriever=''
exclude=''


is_True=True
while True:
     while is_True:
     
       try:
          credit_pass =int(input("please enter your credits at pass: "))   #Validations
          if 0 <= credit_pass <= 120 and credit_pass % 20 == 0:
            break            
          else:
            print( "out of range")     
       except:
           print("Integer required")

     while is_True:
           try:
                credit_defer=int(input("please enter your credits at defer: "))
                if 0 <= credit_defer  <= 120 and credit_defer  % 20 == 0:
                    break            
                else:
                   print( "out of range")
           except :
                print("Integer required")
          
     while is_True:
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
         if total>120 :
             print("Total incorrect")
             break
         elif credit_pass==120 and credit_defer==0 and credit_fail==0 :                  #Displaying outcomes
             print("Progress")                      
             progress = f"progress - {credit_pass},{credit_defer},{credit_fail}"
             progress_count=progress_count+1
             break
         elif credit_pass==100 and 0<=credit_defer<=20 and  0<=credit_fail<=20:
             print("Progress (module trailer)")
             trailer = f"trailer - {credit_pass},{credit_defer},{credit_fail}"
             module_trailer_count = module_trailer_count + 1
             break
         elif 0<= credit_pass<=80 and 0<=credit_defer<=120 and 0<=credit_fail<=60:
             print("module retriever")
             retriever = f"retriever - {credit_pass},{credit_defer},{credit_fail}"          
             module_retriever_count = module_retriever_count + 1
             break
         elif 0<=credit_pass<=40 and 0<=credit_defer<=40 and 80<=credit_fail<=120:
             print("Exclude")
             exclude = f"Exclude - {credit_pass},{credit_defer},{credit_fail}"
             exclude_count = exclude_count + 1
         break
        
              
                       
     while is_True:
         print("\n")
         try:
             answer = input("Would you like to enter another set of data?\n"
                            "Enter 'y' for yes or 'q' to quit and view results: ")
             if answer == 'y':
                 break
             elif answer=='q':
                def histogram_print(progress_count,module_trailer_count,module_retriever_count,exclude_count):        #vertical histogram
                    print('vertical Histogram')
                    print("-progress-", "-module_trailer-","-module_retriever-" , "-Exclude-")

                    for i in range(max(progress_count, module_trailer_count, module_retriever_count, exclude_count)):
                        print(" {}                   {}                    {}           {}   ".format(
                            "*" if i < progress_count else ' ',
                            "*" if i < module_trailer_count else ' ',
                            "*" if i < module_retriever_count else ' ',
                            "*" if i < exclude_count else ' ' 
                              ))
                total_outcomes=progress_count+module_trailer_count+module_retriever_count+ exclude_count
                
                print('\n')
                print()
                histogram_print(progress_count,module_trailer_count,module_retriever_count,exclude_count)
                print(total_outcomes, "outcomes in total.")
                print('\n')
             progression = progress,trailer,retriever,exclude
             progression_1 = list(progression)
             print(progression_1)
             for progressions in progression_1:
                 temp = progressions.split()                     #creating a list
                 print('' .join(temp))
             exit()
         except ValueError:
                print("Please Enter 'y' or 'q'")
             

