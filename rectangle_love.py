

def rect_love(rect1,rect2):
    #print(rect1['left_x'])
    
    if (rect1['x1'] > rect2['x2']) or (rect2['x1'] > rect1['x2']) :
        return False
    if (rect1['y1'] < rect2['y2']) or (rect2['y1'] < rect1['y2']) :
        return False

    return True

rect1={'x1':'10','y1':'5','x2':'10','y2':'5'}
rect2={'x1':'10','y1':'5','x2':'10','y2':'5'}
print("same coordinates: ",rect_love(rect1,rect2))


r1={'x1':'0','y1':'10','x2':'0','y2':'10'}
r2={'x1':'5','y1':'5','x2':'15','y2':'0'}

  #my_rectangle1 = {'left_x': '3','bottom_y': '7','width': '10','height': '4'}
  #my_rectangle2 = {'left_x': 1,'bottom_y': 5,'width': 10,'height': 4}

print("different coordinates: ",rect_love(r1,r2))

