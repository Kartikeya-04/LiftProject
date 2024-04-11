from django.shortcuts import render
from django.http import HttpResponse
from .models import LiftSystem
import time,random
# Create your views here.

def Home(request):
    return render(request,'index.html')
def Compute(request):
    l=LiftSystem()
    time_consumed1=0
    is_open=False
    
    l.lift_name1='L1'
    l.lift_name2='L2'
    listed_lifts=[l.lift_name1,l.lift_name2]

    
    if request.method == 'POST':
        input1=request.POST['Trigger1']
        input2=request.POST['Trigger2']
        if input1>input2:
            a=random.choice(listed_lifts)
            print(f'lift name is {a}')
            

            for i in range(int(input1),int(input2)-1,-1):
                if i==int(input1):
                    print('Lift is Opening')

                    is_open=True
                    time.sleep(1)
                    time_consumed1+=1
                    print('Lift is Closing')

                    is_open=False
                    time.sleep(1)

                    time_consumed1+=1
                time_consumed1+=1
                l.floor_no=i
                time.sleep(1)

                if i==int(input2):
                    print('Lift is Opening')

                    is_open=True
                    time.sleep(1)

                    time_consumed1+=1
                    print('Lift is Closing')

                    is_open=False
                    time.sleep(1)

                    

                
                
                
                
                print(f'Floor number is {l.floor_no}')
                print(f"Time consumed is {time_consumed1}")
            print(f'Total time consumed is {time_consumed1}')
            return HttpResponse('Passenger has been reached Successfully !')
        



        
        a=random.choice(listed_lifts)
        b=LiftSystem()
        print(f'lift name is {a}')
        if input2>input1:
            for i in range(int(input1),int(input2)+1):
                 
                 if i==int(input1):
                    print('Lift is Opening')
                    is_open=True
                    time.sleep(1)
                    time_consumed1+=1
                    print('Lift is Closing')

                    is_open=False
                    time.sleep(1)

                    time_consumed1+=1
                    print(f'Floor number is {i}')
                 b.floor_no=i+1
                 time.sleep(1)
                 time_consumed1 += 1
                 
                
                 if i==int(input2):
                     print('Lift is Opening')
                     
                     is_open=True
                     time.sleep(1)

                     time_consumed1+=1
                     print('Lift is Closing')

                     is_open=False
                     time.sleep(1)

                    #  time_consumed1+=1

                     
                
                     print(f'Floor number is {b.floor_no}')
                 print(f'Time consumed is {time_consumed1}')
        
        l.trigger1=input1
        l.trigger2=input2

        
            
            
        




        print(f'Start - {input1}')
        print(f'End - {input2}')
        return HttpResponse('Passenger has been reached successfully !')
    print('the end')
    return HttpResponse('Ended successfully ')
