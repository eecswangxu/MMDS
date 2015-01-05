m <- matrix(c(0,1/2,1/2,0,0,1,1,0,0), nrow=3, ncol=3)
r0 <- rbind(1,1,1)
r1 <- m %*% r0
r2 <- m %*% r1
r3 <- m %*% r2
r4 <- m %*% r3
r5 <- m %*% r4


