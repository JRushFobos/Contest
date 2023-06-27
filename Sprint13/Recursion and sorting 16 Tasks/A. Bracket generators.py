def generate(count_psp, etalon, prefix, open, close):
    if count_psp == 0:
        print(prefix)
    else:
        if prefix == '':
            generate(count_psp - 1, etalon, prefix + '(', open + 1, close)

        else:
            if open == etalon:
                generate(count_psp - 1, etalon, prefix + ')', open, close + 1)

            elif open == close:
                generate(count_psp - 1, etalon, prefix + '(', open + 1, close)

            else:
                generate(count_psp - 1, etalon, prefix + '(', open + 1, close)
                generate(count_psp - 1, etalon, prefix + ')', open, close + 1)


number_pairs_brackets = int(input())
prefix = ''
open_bracket = 0
close_bracket = 0

generate(
    number_pairs_brackets * 2,
    number_pairs_brackets,
    prefix,
    open_bracket,
    close_bracket,
)
