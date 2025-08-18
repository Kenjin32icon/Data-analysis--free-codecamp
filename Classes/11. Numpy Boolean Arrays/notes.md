In python there are multiple operation that could be performed for example +,- and boolean operators also called masks
The boolean array is created by matcing a specific listt of conditions that should be matched by selective filtering which can be seen as a query method.
The concept of broadcatsing is also defined for boolean operators which return boolean arrays which can be used in filtering 
You can also query the operation you want by using the or[|], and[&] operators

Question

What will the following code print out?

a = np.arange(5)

print(a <= 3)

    [False, False, False, False, True]

    [5]

    [0, 1, 2, 3]

    [True, True, True, True, False] Correct!