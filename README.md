# Linq.py

## About Linq

The well-known EDSL in C#, `Language Integrated Query`, in my opinion, is one of the best design in .NET environment.  
Here is an example of C# Linq.
```C#
// Calculate MSE loss.
/// <param name="Prediction"> the prediction of the neuron network</param>
/// <param name="Expected"> the expected target of the neuron network</param>

Prediction.Zip(Expected, (pred, expected)=> Math.Square(pred-expected)).Average()
```
It's so human readable and it doesn't cost much.

- Reference:

    - Microsoft .NET Genrral introduction => [LINQ: .NET Language-Integrated Query](https://msdn.microsoft.com/en-us/library/bb308959.aspx).
    - Wikipedia => [Language Integrated Query](https://en.wikipedia.org/wiki/Language_Integrated_Query).

And there are so many scenes very awkward to Python programmer, using `Linq` might help a lot.

## Awkward Scenes in Python

```python
seq1 = range(100)
seq2 = range(100, 200)
zipped = zip(seq1, seq2)
mapped = map(lambda ab: ab[0] / ab[1], zipped)
grouped = dict();
group_fn = lambda x: x // 0.2
for e in mapped:
    group_id = group_fn(e)
    if group_id not in grouped:
        grouped[group_id] = [e]
        continue
    grouped[group_id].append(e)
for e in grouped.items():
    print(e)
```
The codes seems to be too long...  
Now we extract the function `group_by`:
```python
def group_by(f, container):
    grouped = dict()
    for e in container:
        group_id = f(e)
        if group_id not in grouped:
            grouped[group_id] = [e]
            continue
        grouped[group_id].append(e)
    return grouped
res = group_by(lambda x: x//0.2, map(lambda ab[0]/ab[1], zip(seq1, seq2)))
```
Okay, it's not at fault, however, it makes me upset —— why do I have to write these ugly codes?  
Now, let us try Linq!
```Python
from linq import Flow, extension_std
seq = Flow(range(100))
res = seq.Zip(range(100, 200)).Map(lambda fst, snd : fst/snd).GroupBy(lambda num: num//0.2).Unboxed()
```

To be continue.
