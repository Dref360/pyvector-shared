# pyvector-shared
Implementation of a sharable vector-like structure. This can be used to speedup consumer-producers architecture where pickling is a bottleneck.

## Vector methods
```python
x = np.arange(10, dtype=np.int)
vec = Vector(x) # Initialize a vector of ints.
vec.assign(np.arange(15, dtype=np.int) # Assign the values of a new vector. (Resize the vector if needed)
y = vec.get() # Get a numpy array representation.
```
We can then share `vec` to other processes and they share a common Array.


## Notes
* Only some numpy types are accepted.
* The array type is not dynamic
* 
