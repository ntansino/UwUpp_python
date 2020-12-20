# UwU++
## Python 3 Implementation
### Name: Danny Noe and Nick Tansino

# Introduction

We have implemented a modified version of the UwUpp language (also known as UwU++) in Python. UwU++ is an esoteric programming language based around unconventional, meme-related slang. As described by its creator, UwU++ aims to compete with Brainf*ck to be the most painful programming language to read and write in. The reason being that the entire programming language is written in what is known as UwU-speak, an English dialect that is phonetically spelled and pronounced as if spoken/written by an infant.
Based on this GitHub repo: https://github.com/deltaphish/uwupp
Our GitHub: https://github.com/ntansino001/UwUpp_python

# Implementation


# Challenges
Surprisingly, the most challenging piece of implementing UwU++ was the lexer. The lexer was so challenging because UwU++ uses phrases like "pwus" rather than '+' for addition and "gweatew_twan" for '>'. It took us some time to figure out how to get Yacc and Ply to recognize "pwus" as an operator. Yacc and Ply did not allow for tokens to be more than one word, so we had to include underscores in the comparison operators' names. In the original UwUpp, assignment statements used the phrase "iws" instead of the '=' sign. Ply did not allow us to use the word 'iws', so we had to stick with the equals sign.
If we could implement UwU++ again, we would like to recreate it closer to the original UwU++. For example, we would like to find a way to support 'iws" for the assignment operator. We would also like to support multi-line comments.
If we had more time, we would add support for strings and arrays. The original UwU++ supports strings. We originally wanted to support strings but ran out of time. Similarly, UwU++ supports arrays. We want to support arrays but did not have enough time to figure out the implementation. If we had more time, we would also like to implement the comment character properly. In our implementation comments begin with '/UwU'. The '/' is required for our lexer to recognize comments. When we tried to just use 'UwU' the parse would not ignore comments properly.

# Examples

```
assign = \
    """
    /UwU Basic Variable assignment and print
    decwawe x = 5
    nuzzels(x)
    """
interp(assign)
```

```
add = \
    """
    /UwU Function
    decwawe *add(a)* {
        decwawe x = 1
        decwawe y = x pwus a
        wetuwn y
    }
    nuzzels(add(5))
    """
interp(add)
```

```
test_wisten = \
    """
    /UwU Input
    decwawe input
    input = wisten()
    nuzzels(input)
    """
interp(test_wisten)
```

```
notices_no_ewse = \
    """
    /UwU If
    decwawe x = 1000
    decwawe y = 54321
    * notices x wess_twan y *
        nuzzels(x)
        stawp
    """
interp(notices_no_ewse)
```

```
notices = \
    /UwU If else
    """
    decwawe x = 100000
    decwawe y = 54321
    * notices x wess_twan y *
        nuzzels(x)
    ewse
        nuzzels(y)
        stawp
    """
interp(notices)
```

```
binop = \
    """
    decwawe x = 10
    decwawe y = 122
    decwawe z = x pwus y
    nuzzels(z)

    decwawe a = 150
    decwawe b = 50
    decwawe c = a minwus b
    nuzzels(c)

    decwawe d = 10
    decwawe e = 5
    decwawe f = d twimes e
    nuzzels(f)

    decwawe m = 1000
    decwawe n = 20
    decwawe o = m diwide n
    nuzzels(o)
    """
interp(binop)
```

```
negative = \
        """
        decwawe x = 200
        decwawe y = minwus 200
        nuzzels(y)
        nuzzels(x minwus y)
        nuzzels(x minwus minwus 20)
        """
interp(negative)
```

```
OwO = \
    """
    /UwU While loop
    decwawe x = 1000
    decwawe y = 54321

    owo * x wess_twan y *{
        nuzzels(x)
        x = x twimes 2
        nuzzels(y)}
        stawp
    """
interp(OwO)
```