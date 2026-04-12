using Statistics, PyPlot, DelimitedFiles, StatsBase

# #=
# EXERCICE 1 ################################################################
# Exercise 1.1
x1 = readdlm("meteostat-sion-1988-1993.csv",',')	# Load data
ndays = 2192
for j in 2:4
	for i in 2:(ndays+1)
		if x1[i,j] == ""
			if i == 1
				x1[i,j] = x1[i+1,j]
			else
				x1[i,j] = x1[i-1,j]
			end
		end
	end
end
Ta1 = Float64.(x1[2:end,2])	# Daily average temp.
Tm1 = Float64.(x1[2:end,3])	# Daily min temp.
TM1 = Float64.(x1[2:end,4])	# Daily max temp.

dates = x1[2:end,1]

figure("Sion 1988-1993 (ex 1.1)")
PyPlot.plot(1:ndays,Ta1)
xlabel("day")
ylabel("T [°C]")

# Exercice 1.2
T = Dict{Int64,Vector{Float64}}(i => Float64[] for i in 1:12)
for i in 1:ndays
	date = dates[i]
	month = parse(Int64,date[6:7])
	push!(T[month],Ta1[i])
end
a1 = [mean(T[i]) for i in 1:12]
m1 = [minimum(T[i]) for i in 1:12]
M1 = [maximum(T[i]) for i in 1:12]

figure("Sion 1988-1993 (ex 1.2)")
PyPlot.plot(1:12,a1,"-o",color="gray")
PyPlot.plot(1:12,m1,"-o",color="C0")
PyPlot.plot(1:12,M1,"-o",color="C3")
xlabel("month")
ylabel("T [°C]")

# Exercise 1.3
sy = std(Ta1)
sm = [std(T[i]) for i in 1:12]

figure("Sion 1988-1993 (ex 1.3)")
PyPlot.plot([1,12],[sy,sy],"--",color="C7",label="year")
PyPlot.plot(1:12,sm,"-o",color="C7",label="month")
xlabel("month")
ylabel("standard deviation")
legend()

# Exercise 1.4
figure("Sion 1988-1993 (ex 1.4)")
Tmi = floor(minimum(Ta1)-.51) + .5
Tma = maximum(Ta1)+.99
bins = Tmi:1:Tma
h = PyPlot.hist(Ta1,bins=bins)
xlabel("T [°C]")
ylabel("probability")

# Exercise 1.5
p = [sum(bins[i] .< Ta1 .<= bins[i+1]) for i in 1:length(bins)-1]./ndays .+ 1e-10
H = -sum(log.(2,p).*p)
@info "H = $H"

# EXERCICE 2 ################################################################
# Exercice 2.1, 2.2
x2 = readdlm("meteostat-miami-1988-1993.csv",',')	# Load data
Ta2 = Float64.(x2[2:end,2])	# Daily average temp.
Tm2 = Float64.(x2[2:end,3])	# Daily min temp.
TM2 = Float64.(x2[2:end,4])	# Daily max temp.

r12 = cor(Ta1,Ta2)
@info "Correlation of avg temp. between Sion and Miami between 1988 and 1993: $(round(r12,digits=2))"

# Exercice 2.3
a1 = autocor(Ta1,0:600)
a2 = autocor(Ta2,0:600)

figure("Autocorrelation (ex 2.3)")
PyPlot.plot(0:600,a1,label="Sion, 1988-1993")
PyPlot.plot(0:600,a2,label="Miami, 1988-1993")
xlabel("Lag [days]")
ylabel("Autocorrelation")
legend()

# EXERCICE 3 ################################################################
# Exercice 3.1
months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
month2temp1 = Dict{String,Vector{Float64}}(m => Float64[] for m in months)
month2temp2 = Dict{String,Vector{Float64}}(m => Float64[] for m in months)
for d in 1:ndays
	date = dates[d]
	T1 = Ta1[d]
	T2 = Ta2[d]
	push!(month2temp1[date[6:7]],T1)
	push!(month2temp2[date[6:7]],T2)
end

# =#
figure("Boxplots (ex 3.1)",figsize=(15,5))
subplot(2,1,1)
PyPlot.boxplot([month2temp1[m] for m in months],vert=true,positions=(1:12),widths=.2)
ylabel("T [°C]")
title("Sion")
subplot(2,1,2)
PyPlot.boxplot([month2temp2[m] for m in months],vert=true,positions=(1:12),widths=.2)
xlabel("month")
ylabel("T [°C]")
title("Miami")

# =#
Z1 = zscore.([month2temp1[m] for m in months])
for m in 1:12
	for d in 1:length(Z1[m])
		if Z1[m][d] >= 2.
			@info "Sion: Outlier on $d.$m."
		end
	end
end
Z2 = zscore.([month2temp2[m] for m in months])
for m in 1:12
	for d in 1:length(Z2[m])
		if Z2[m][d] >= 2
			@info "Miami: Outlier on $d.$m."
		end
	end
end







