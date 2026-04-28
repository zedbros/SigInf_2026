function myLZ_encode(text::String)
	O = ["",]
	C = Dict{Int64,Tuple{Int64,String}}(0 => (0,""))
	code = ""

	t = ""
	k = 0
	for c in text
		t *= c
		if !(t in O)
			i = maximum(collect(1:length(O)).*(t[1:end-1] .== O))
			push!(O,t)
			k += 1
			C[k] = (i-1,"$c")
			code *= "$(i-1)"*c
			t = ""
		end
	end
	i = maximum(collect(1:length(O)).*(t .== O))
	code *= "$(i-1)"

	return code,C
end

function myLZ_decode(code::String)
	O = ["",]
	T = Dict{Int64,String}(0 => "")
	text = ""

	t = ""
	k = 0
	nums = ['0','1','2','3','4','5','6','7','8','9']
	for c in code
		if c in nums
			t *= c
		else
			k += 1
			n = parse(Int64,t)
			T[k] = T[n]*c
			text *= T[k]
			t = ""
		end
	end
	T[k+1] = T[parse(Int64,t)]
	text *= T[k+1]

	return text, T
end

text = lowercase(read("8-Code-Prefix/sols/lab08-solution-myLoremIpsum.txt",String)[1:end-1])
code = myLZ_encode(text)
write("8-Code-Prefix/sols/myCode.txt",code[1])
txet = myLZ_decode(code[1])
