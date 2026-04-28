# SinInf: solutions to lab08
# Apr 21, 2026

using DelimitedFiles

refPath = "/home/robindelabays/kDrive/00-teaching/2425-sp/siginf/lab02/" # Indicate the path to the lab directory.

include(refPath*"../myLibrary.jl")
include(refPath*"../myTools.jl")

#################################################
# Partie 0
@info "========================="
@info "Partie 0"
@info "========================="

# 1.
A = sort(union(['A','D','E','I','M','N','P','R','U','Y']))
@info "A = $A"

# 2.
p = [7.11,3.67,12.1,6.59,2.62,6.39,2.49,6.07,4.49,.46]
p ./= sum(p)
@info "1. p = $(round.(p,digits=2))"

A2p = Dict{Char,Float64}(A[i] => p[i] for i in 1:length(A))

# 3.
H = myEntropy(p)
@info "H(X) = $H"


#################################################
# Partie 1
@info "========================="
@info "Partie 1"
@info "========================="

# 2.
C1 = Dict{Char,String}('A' => "0000",
		       'D' => "0001",
		       'E' => "0010",
		       'I' => "0011",
		       'M' => "0100",
		       'N' => "0101",
		       'P' => "0110",
		       'R' => "0111",
		       'U' => "1000",
		       'Y' => "1001")


# 3.
E1 = sum([length(C1[k])*A2p[k] for k in keys(C1)])
@info "3. \tLongueur moyenne (naïf): \tE(l(C1(X))) = $E1, \n\t\tborne de Shannon: \tH(X) = $H"


#################################################
# Partie 2
@info "========================="
@info "Partie 2"
@info "========================="

# 1.
C2 = Dict{Char,String}('A' => "010",
		       'D' => "0110",
		       'E' => "000",
		       'I' => "110",
		       'M' => "0111",
		       'N' => "111",
		       'P' => "1000",
		       'R' => "101",
		       'U' => "1001",
		       'Y' => "001")


# 2. 
E2 = sum([length(C2[k])*A2p[k] for k in keys(C2)])
@info "2. \tLongueur moyenne (Fano) : \tE(l(C2(X))) = $E2, \n\t\tlongueur moyenne (naïf) : \tE(l(C1(X))) = $E1, \n\t\tborne de Shannon : \t\tH(X) = $H."



#################################################
# Partie 3
@info "========================="
@info "Partie 3"
@info "========================="

# 1.
pA = sortslices([p A],dims=1,rev=true)
p = Float64.(pA[:,1])
A = pA[:,2]
n = ceil.(Int64,-log.(2,p))
c = [sum(p[1:i]) for i in 0:length(p)-1]
b = ten2two(c)
C = floor.(Int64,b.*(10.).^n)./((10.).^n)
#C = roundBin(b,n)

C3 = Dict{Char,String}(A[i] => "$(b[i] + 1. + 1e-15)"[3:n[i]+2] for i in 1:length(A))
#C3 = Dict{Char,String}(A[i] => C[i] for i in 1:length(A))

# 2.
E3 = sum([length(C3[k])*A2p[k] for k in keys(C3)])
@info "2. \tLongueur moyenne (Shannon) : \tE(l(C3(X))) = $E3, \n\t\tlongeur moyenne (Fano) : \tE(L(C2(X))) = $E2, \n\t\tlongueur moyenne (naïf) : \tE(l(C1(X))) = $E1, \n\t\tborne de Shannon : \t\tH(x) = $H."

