s = 'ocean'
k = 10


def caesarCipher(s, k):
    abc_l = 'abcdefghijklmnopqrstuvwxyz'
    # abc_u = 'ABCDEFGHUJKLMNOPQRSTUVWXYZ'
    s_abc_l = abc_l[k:] + abc_l[:k]  # defghijklmnopqrstuvwxyzabc

    # each letter has it's position in regular abs
    # print('regular')
    # index = 0
    # for each in s:
    # index = index + 1
    # print(each, index)
    new_s = ''
    for i, each in enumerate(abc_l):
        # print('i, each', i, each)
        if each in s:
            # print(each, s_abc_l[i])
            print(s_abc_l[i])
            new_s = s.replace(each, s_abc_l[i])
            print('new_s', new_s)
    # print(new_s)
    # for each in s_abc:
    #     if each in s:
    #         print(ord(each), each)

        # if each in s:
            # pos.append(i)
            # print(pos, each)

    # current posiiton of letters in string
    # 4 e
    # 18 s
    # 19 t
    # use the same numbers for shifted_abc

    # for each in s:
        # get the position of the letter in a normal abc
        # print(ord(each))
        # print()
        # if each in pos:
            # print(pos)
        # shift abc to k times
        # select letter with the same number position
        # how to get position number of a letter in both abcs?

        # get letter position in a normal abc

        # select same position number in a shifted abc
        # shifted_abc[]

        # replace this letter in replace
        # print(s.replace('t', 'O'))

        # return the string

    # s
    # 2 e
    # 16 s
    # 17 t

    # print('string')
    # for each in s:
    #     print(each)

    # print('shifted')
    # for each in shifted_abc:
    #     if each in s:
    #         print(each)


caesarCipher(s, k)
