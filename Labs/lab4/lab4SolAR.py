############################################################
# Name: Anthony Rizzuto
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. Anthony Rizzuto
# CS115 Lab 4
#
############################################################

def knapsack(capacity, itemList):
    '''
    -function takes an integer capacity, which represents the maximum 'weight' possible
    and itemList, which is multiple lists in a list that and they represent items that can be taken
    -the lists in itemList represent [itemWeight, itemValue]
    -after receiving a max capacity and possible items in itemList, this function displays the maximum item 
    value that can be obtained from the provided itemList 
    '''
    if len(itemList) == 0 or capacity <= 0:   #BASE CASE
        return [0, []]
    elif itemList[0][0] > capacity:         #assuming itemList = [maxval, [[item1weight, item1val], 
                                            #[item2weight, item2val], [item3weight, item3val]]]
                                            #ths statement says if item1weight > capacity, then go to the next item
        return knapsack(capacity, itemList[1:])
    else:
        use_it = knapsack(capacity - itemList[0][0], itemList[1:])  #otherwise, (while using same itemList assumption),
                                                                    #the use_it recursively calls knapsack and subtracts item1weight from
                                                                    #capacity and then moves on to item2... and so on
                                                                    
        use_it[0] += itemList[0][1]         #use_it then returns a list with the first element 
                                            #being the item values added together.
        
        use_it[1].insert(0, itemList[0])    #the second element in the use_it list inserts (as a itemWeight, itemValue list)
                                            #which items are being used to contirbute to the total item value (1st element in use_it list)
        lose_it = knapsack(capacity, itemList[1:])  #lose_it recursively calls the function again just skipping the 1st item in itemList
        return max(use_it, lose_it)     
