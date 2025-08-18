This unit talks about broadcasking and vectorization given the example of the following exercise;
a = np.arange(5)
    0,1,2,3,4
a + 20
    20,21,22,23,24
a
    0,1,2,3,4


The follwing operation is vectorized:
a + 20 The following operation is broadcasted to all the values in the following and reverts to normal
The following operation is not vectorized:
a = a + 20 this opertion with be performed to all the values and they would not return to their original state