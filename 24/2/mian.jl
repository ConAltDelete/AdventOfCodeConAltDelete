
function ValidateSequence(seq)
    diff_test = diff(seq)
    sign_test = [sign(x) for x in diff_test]
    if any(x -> x != sign_test[1],sign_test)
        return false
    end
    if any(x -> abs(x) > 3 || abs(x) < 1,diff_test)
        return false
    end

    return true
end

function RemoveInvalid(seq)
    for i in 1:length(seq)
        if ValidateSequence(vcat(seq[1:i-1],seq[i+1:end]))
            return true
        end
    end
    return false
end

open(".\\2\\input","r") do f
    valids = 0
    dampend_valids = 0
    while ! eof(f)
        s = [parse(Int, ss) for ss in split(readline(f))]
        if ValidateSequence(s)
            valids += 1
        elseif RemoveInvalid(s)
            dampend_valids += 1
        end
    end
    println("Part 1:" * string(valids))
    println("Part 2:" * string(dampend_valids + valids))

end