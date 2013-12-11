{
  "title": "Master Theorem",
  "date": "2013-12-11",
  "categories": [
    
  ],
  "tags": [
    
  ]
}

[Wiki](http://en.wikipedia.org/wiki/Master_theorem)

###Main recursion formula
$$T(n) = aT(n / b) + f(n)$$

If 
$$f(n) = \Theta\left( n^{c} \right)$$ where $$c < \log_b a $$(using Big O notation)
then:
$$T(n) = \Theta\left( n^{\log_b a} \right)$$

If it is true, for some constant k ≥ 0, that:
$$f(n) = \Theta\left( n^{c} \log^{k} n \right)$$ where $$c = \log_b a$$
then:
$$T(n) = \Theta\left( n^{c} \log^{k+1} n \right)$$

Generic form
If it is true that:
$$f(n) = \Theta\left( n^{c} \right)$$ where $$c > \log_b a$$
then:
$$T\left(n \right) = \Theta\left(f(n) \right)$$
