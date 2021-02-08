

def edit_distance(string1,string2):

    str1_len=len(string1) 
    str2_len=len(string2) 



    if str1_len == 0 and str2_len == 0:
        return None
    if str1_len == 0:
        return str2_len

    if str2_len == 0:
        return str1_len

    matrix = [[0 for x in range(str1_len+1)] for x in range(str2_len+1)]

    

    for i in range(1,str1_len+1):
        matrix[0][i] = i

    for i in range(1,str2_len+1):
        matrix[i][0] = i


    #setting all the values to the  matrix for each test of each item.
    second_str_counter = 0

    while second_str_counter != str2_len :
        

        for index,char in enumerate(string1) :


            current_position = matrix[second_str_counter+1][index+1]
           
            
            
            left_position = matrix[second_str_counter+1][index]
            left_top_position = matrix[second_str_counter][index]
            right_top_position = matrix[second_str_counter][index+1]

            if char == string2[second_str_counter]:
                matrix[second_str_counter+1][index+1] = int(left_top_position)
                
               
            else :
                get_min_value=min(int(left_position),int(left_top_position),int(right_top_position))
                matrix[second_str_counter+1][index+1] = int(get_min_value)+1
          
        second_str_counter += 1
   

    return matrix[-1][-1]


    

print(edit_distance('saturday','sunday'))