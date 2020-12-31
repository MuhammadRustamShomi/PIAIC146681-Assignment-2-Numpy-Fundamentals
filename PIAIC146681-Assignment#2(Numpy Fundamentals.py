#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[15]:


import numpy as np
a = np.array([0,1,2,3,4,5,6,7,8,9])
b=a.reshape(2,5)
print(b.tolist())


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[31]:


import numpy as np
x=np.arange(10).reshape(2,5)
print(x)
y=np.ones(10).reshape(2,5)
print(y)


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[39]:


import numpy as np
x=np.arange(10).reshape(2,5),np.ones(10).reshape(2,5)
print(x)
x[0:4]


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[ ]:





# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[ ]:





# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[ ]:





# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[3]:


import numpy as np
x = np.random.random((5,5))
print(x,np.square(x))


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[5]:


import numpy as np
x = np.random.random((5,6))
print(x)
np.mean(x)


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[6]:


import numpy as np
x = np.random.random((5,6))
print(x)
np.std(x)


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[8]:


import numpy as np
x = np.random.random((5,6))
print(x)
np.median(x)


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[9]:


import numpy as np
x = np.random.random((5,6))
print(x)
np.transpose(x)


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[10]:


import numpy as np 
n_array = np.array([[55, 25, 15, 41], 
                    [30, 44, 2, 54], 
                    [11, 45, 77, 11], 
                    [11, 212, 4, 20]]) 
   
print(n_array) 
trace = np.trace(n_array) 
print(trace) 


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[12]:


import numpy as np 
n_array = np.array([[55, 25, 15, 41], 
                    [30, 44, 2, 54], 
                    [11, 45, 77, 11], 
                    [11, 212, 4, 20]]) 
   
print(n_array)
print(np.linalg.det(n_array))


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[14]:


import numpy as np 
arr = [20, 2, 7, 1, 34]
print(arr) 
print(np.percentile(arr, 5))
print(np.percentile(arr, 95))


# ## Question:15

# ### How to find if a given array has any null values?

# In[15]:


import numpy as np

b = np.array([[4, np.inf],[np.nan, -np.inf]])

np.isnan(b)

