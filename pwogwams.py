assign = \
    """
    UwUBasic Variable assignment and print
    decwawe x = 5
    nuzzels(x)
    """

add = \
    """
    decwawe *add(a)* {
        decwawe x = 1
        decwawe y = x pwus a
        wetuwn y
    }
    nuzzels(add(5))
    """

test_wisten = \
    """
    decwawe input
    input = wisten
    nuzzels(input)
    """

notices = \
    """
    decwawe x = 100000
    decwawe y = 54321
    * notices x wess_twan y *
        nuzzels(x)
    ewse
        nuzzels(y)
        stawp
    """

notices_no_ewse = \
    """
    decwawe x = 1000
    decwawe y = 54321
    * notices x wess_twan y *
        nuzzels(x)
        stawp
    """

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

OwO = \
    """
    decwawe x = 1000
    decwawe y = 54321

    owo * x wess_twan y *{
        nuzzels(x)
        x = x twimes 2
        nuzzels(y)}
        stawp
    """

negative = \
        """
        decwawe x = 200
        decwawe y = minwus 200
        nuzzels(y)
        nuzzels(x minwus y)
        nuzzels(x minwus minwus 20)
        """

test_all = \
    """
    decwawe input = wisten
    decwawe *math(a)* {
        decwawe x = 10
        decwawe y = 122
        decwawe z = x pwus y
        nuzzels(z)

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
        wetuwn o
    }
    math(input)
    decwawe y = 122
    * notices input wess_twan y *
        nuzzels(input)
    ewse
        nuzzels(y)
    stawp

    decwawe x = 200
    owo * x gweatew_twan y *{
        nuzzels(x)
        x = x diwide 2
        nuzzels(y)
        }
        stawp
    
    * notices 10 eqwall_twoo 10 *
        nuzzels(10)
        stawp
    
    * notices 20 eqwall_twoo 10 *
        nuzzels(10)
    ewse
        nuzzels(20)
        stawp
    """