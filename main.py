#the first assignment of the bootcamp
#create a simple function and push to your github
#it's a Hamming Distance (two count the difference of the two strings)
def hamming_distance(str1,str2):
       counter =0
       indexer_list= []
       #check the type of input
       if type(str1) !=str or type(str2) !=str :
              raise ValueError("the type must be string")
       #check the equality of two strings
       elif len(str1) != len(str2):
              raise ValueError("the strings must be at the same length")
       #counting the difference
       else:
              for i in range(0,len(str1)):
                     if str1[i] !=str2[i] :
                            counter +=1
                            indexer_list.append(counter-1)
                     else:
                            pass
       return indexer_list

       
f1=hamming_distance('this is a string', 'thix ix a xtring')
print(' the number of differences are ', len(f1))