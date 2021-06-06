def incomodam(n):

    if n <= 0:
        return str('')
    return 'incomodam ' + incomodam(n-1)
        
    
def elefantes(n, max = None) -> str:

    if not max: # apenas inverto na primeira rodada. Nas demais eu informo o parametro...
        max, n = n, 2

    if n <= max:
        if n == 2:
            verso = 'Um elefante incomoda muita gente\n'
            verso += '{} elefantes {}muito mais\n'.format(n, incomodam(n))

        else:
            verso = '{} elefantes {}muito mais\n'.format(n, incomodam(n))

        if n < max:
            verso += '{} elefantes incomodam muita gente\n'.format(n)

        return verso + elefantes(n+1, max)
        
    return ''
