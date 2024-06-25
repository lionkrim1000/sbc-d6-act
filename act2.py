height = 5  # height 
width = 5   # width 
    
row = 1
while row <= height:
        col = 1
        while col <= width:
            if row == 1 or row == height or col == 1 or col == width:
                print('*', end='')
            else:
                print(' ', end='')
            col += 1
        print()  
        row += 1


