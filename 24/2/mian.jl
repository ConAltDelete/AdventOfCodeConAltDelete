

open(".\\2\\input","r") do f
    valids = 0
    while ! eof(f)
        s = [parse(Int, ss) for ss in split(readline(f))]
        previus_number = s[1]
        sign_of_values = 0
        found_valid = true
        for values in s[2:length(s)]
            diff = values - previus_number
            if abs(diff) < 1 || abs(diff) > 3
                found_valid = false
                break
            end
            if sign_of_values == 0
                sign_of_values = sign(diff)
            elseif sign(diff) != sign_of_values 
                found_valid = false
                break
            end
            previus_number = values
        end
        if found_valid
            valids += 1
        end
    end
    println(valids)
end