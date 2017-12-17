""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might 
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    max_val = max(arr)
    min_val = min(arr)
    
    if max_val == min_val:
        return None
    else:
        Scale_lst = [ 1.0*(i - min_val) / (max_val - min_val) for i in arr]

        
    return Scale_lst

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)