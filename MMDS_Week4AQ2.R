alpha <- 0
A = c(1,0,1,0,1,2*alpha)
B = c(1,1,0,0,1,6*alpha)
C = c(0,1,0,1,0,2*alpha)
A_len = sqrt(sum(A^2))
B_len = sqrt(sum(B^2))
C_len = sqrt(sum(C^2))
AB = A %*% B / (A_len * B_len)
AC = A %*% C / (A_len * C_len)
BC = B %*% C / (B_len * C_len)
