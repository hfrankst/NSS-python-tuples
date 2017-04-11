# NSS-python-tuples

# Python Tuples

Tuples are like lists, but are immutable. They can't be modified once defined. However, finding values in a tuple is faster than in a list.

## Setup

```mkdir -p ~/workspace/python/exercises/tuples && cd $_
touch zoo.py
subl .
```
## References

*[Python tuples](https://docs.python.org/3.6/tutorial/datastructures.html#tuples-and-sequences)
*[Introducing Tuples](http://www.diveintopython.net/native_data_types/tuples.html)

## Instructions

1. Create a tuple named ```zoo``` that contains your favorite animals.

2. Find one of your animals using the ```.index(value)``` method on the tuple.

3. Determine if an animal is in your tuple by using ```for value in tuple.```

4. Create a variable for each of the animals in your tuple with this cool feature of Python.
```
# example
(lizard, fox, mammoth) = zoo
print(lizard)
```

5.Convert your tuple into a list.

6. Use ```extend()``` to add three more animals to your zoo.

7. Convert the list back into a tuple.