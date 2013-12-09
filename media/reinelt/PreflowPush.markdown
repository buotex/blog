Preflow-Push
=====

Präfluss $f : V \rightarrow R$
---
- Kapazität $f < c$
- Antisymmetrie $f(u,v) = - f(v,u)$
- Überschuss $f(V,u) \geq 0$ hier im Gegensatz zu $\sum f(u,v) = \sum f(v,u)$

Höhenfunktion h(s)
---
- h(s) = |V|
- h(t) = 0
- h(u) $\leq$ h(v) + 1 für jede Kante aus dem reduzierten Netzwerk $D_f$
