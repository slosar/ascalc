# ASCALC - a simple astropy based calculator

This is a very simply interface to the astopy units and constant engine.

It imports all units and constants (in this order, so G = gravitational constant and not Gauss) into root namespace.
It manipulates string to allow intuitive entry, i.e. 10K becomes 10*(K).

It allows calculations like:

```
> (68 km/s/Mpc)**2/(8*pi*G/3)
 =  8.685451636698969e-27 kg / m3
```

When I get less lazy I might implement some syntax for unit conversion.
