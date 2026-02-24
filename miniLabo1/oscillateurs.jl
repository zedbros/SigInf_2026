import Pkg
Pkg.activate(@__DIR__)
Pkg.add("Plots")

using Plots

begin
    global x = []
    global y = []
    function complexe_osc(t)
        local a = 2
        local ω = 1
        local ϕ = π/4
        local Re = a*cos(ω*t+ϕ)
        local Im = a*sin(ω*t+ϕ)
        return Re, Im
    end

    @gif for i in 1:0.1:10
        yarrr = complexe_osc(i)
        push!(x, yarrr[1])
        push!(y, yarrr[2])

        Plots.plot(x, y, xlims=[-3,3], ylims=[-3,3])
    end
end
