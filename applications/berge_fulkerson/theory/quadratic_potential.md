# Quadratic Potential

For coordinate `i`, define

`w_i(e)=2d(e)+1-2*1[e in M_i]`.

Then replacing `M_i` by `N` changes the potential by

`Q(M-M_i+N)-Q(M)=w_i(N)-w_i(M_i)`.

Thus the optimal coordinate update is a minimum-weight perfect matching.  At a coordinate local minimum, comparison with the fractional perfect matching `1/3` gives `S_i=sum_{e in M_i}d(e)<=n/3`; summation gives `Q<=2n`.
