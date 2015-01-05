L <- matrix(0, 4, 4)
L[1, 2] = 1
L[1, 3] = 1
L[2, 1] = 1
L[3, 4] = 1
L[4, 3] = 1

h = c(1,1,1,1)

for(i in 1: 2) {
	a = t(L) %*% h
	a = a / max(a)
	h = L %*% a
	h = h / max(h)
}

h
a
