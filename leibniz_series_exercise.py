def approximate_pi(n_terms):
    sum = o
    for i in range(n_terms):
        num = (-1)**i / (2*i + 1)
        sum += num
    return sum * 4    
    
