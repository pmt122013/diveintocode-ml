import time
import matplotlib.pyplot as plt

THICKNESS = 0.00008                             #meters

def folded_43times():                           #PROBLEM 1
    folded_thickness = THICKNESS*(2**43)
    print("Thickness: {} meters".format(folded_thickness))

def folded_43times_in_kilometer():              #PROBLEM 2
    folded_thickness = THICKNESS*(2**43)
    print("Thickness: {:.2f} kilometers".format(folded_thickness/1000))  

def folded_43times_using_for():                 #PROBLEM 3
    time = 1
    for i in range(43):
        time *= 2
        if i == 43:
            break
    folded_thickness = THICKNESS*time
    print("Thickness: {} meters".format(folded_thickness))    

def time_comparison():                          #PROBLEM 4
    start_function1 = time.time()
    folded_43times()
    elapsed_time_function1 = time.time() - start_function1
    print("time for function 1 : {}[s]".format(elapsed_time_function1)) 

    start_function3 = time.time()
    folded_43times_using_for()
    elapsed_time_function3 = time.time() - start_function3
    print("time for function 2 : {}[s]".format(elapsed_time_function3)) 
    if elapsed_time_function1 < elapsed_time_function3:
        print("\nTime executing loop is longer.")
    elif elapsed_time_function1 > elapsed_time_function3:
        print("\nTime executing loop is shorter.")  
    else:
        print("\nTime executing for both functions is the same.")           

def list_of_folded():                           #PROBLEM 5
    value_list = []
    value_list += [THICKNESS]
    for i in range(1,44):
        folded_thickness = THICKNESS* (2**i)
        value_list += [folded_thickness]
    print("There are {} elements in this list.".format(len(value_list)))

def unmodified_plot_list():                     #PROBLEM 6
    value_list = []
    value_list += [THICKNESS]

    for i in range(1,44):
        folded_thickness = THICKNESS* (2**i)
        value_list += [folded_thickness]    

    plt.title("thickness of folded paper")
    plt.xlabel("number of folds")
    plt.ylabel("thickness[m]")
    plt.plot(value_list)
    plt.show()

def modified_plot_list():                       #PROBLEM 7
    value_list = []
    value_list += [THICKNESS]

    for i in range(1,44):
        folded_thickness = THICKNESS* (2**i)
        value_list += [folded_thickness] 

    plt.title("thickness of folded paper",color='green',fontsize=20)
    plt.xlabel("number of folds",color='green',fontsize=16)
    plt.ylabel("thickness[m]",color='green',fontsize=16)
    plt.plot(value_list,color='green' ,linestyle='dotted',linewidth=4)
    plt.show()      

print("-------ANSWER PROBLEM 1-------")
folded_43times()
print("\n-------ANSWER PROBLEM 2-------")
folded_43times_in_kilometer() 
print("\n-------ANSWER PROBLEM 3-------")
folded_43times_using_for() 
print("\n-------ANSWER PROBLEM 4-------")
time_comparison()
print("\n-------ANSWER PROBLEM 5-------")
list_of_folded()

print("\n-------ANSWER PROBLEM 6-------")
unmodified_plot_list() 
print("\n-------ANSWER PROBLEM 7-------")
modified_plot_list() 
