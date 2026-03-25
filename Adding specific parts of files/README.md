# Adding files is the beginning

As I work with git I find myself adding files `git add filename.txt`. When I have several files to commit `git add .` adds them all. That is all well and good for clean sanitary perfect conditions. I don't usually have that occur.

Often I find myself working on a section of code when I see an issue in another piece of code. My past-self would say "Well. Since I'm here I can add this little cleanup." My current-self usually adds a `TODO:` note with enough information to correct it. After doing that I move on. The issue with that is those edits accumulate. When it comes time to add and commit the changes I intended to make `git add .` adds everything.

Now those edits are unwanted noise. They don't belong to what I worked on. I want atomic self containing commits. I also don't want to discard the edits though. ¿What to do? [git add -e](https://git-scm.com/docs/git-add#Documentation/git-add.txt--e) is the tool for the job. `-e` is a synonym/alias for `--edit`. You get to decide what you want to add.

To illustrate this point I start with a contrived math example in python.

```python
# Code Above

def adding_two_numbers_together(augend, addend):
    return augend + addend

def subtracting_two_numbers(minuend, subtrahend):
    return minuend - subtrahend

def multiplying_two_numbers(multiplier, multiplicand):
    return multiplier * multiplicand

def dividing_two_numbers(numerator, denominator):
    return numerator / denominator

# Plenty of code in between


# Code you're working in
def Foo(bar, bazz):
    match bar:
        case 1:
            return adding_two_numbers_together(1, 3)
        case 2:
            return subtracting_two_numbers(2, 2)
        case 3:
            return multiplying_two_numbers(3, 1)
        case 4:
            return dividing_two_numbers(4, 0)

    return bazz
```

Assume valid numerical data will only ever be used. Do you see it? The issue. It comes from division. If you have a zero in the denominator you end up with a `ZeroDivisionError`.