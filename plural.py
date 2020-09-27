import re


def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return (matches_rule, apply_rule)


patterns = \
  (
    ('[sxz]$',           '$',  'es'),
    ('[^aeioudgkprt]h$', '$',  'es'),
    ('(qu|[^aeiou])y$',  'y$', 'ies'),
    ('$',                '$',  's')
)

rules = [
    build_match_and_apply_functions(pattern, search, replace)
    for (pattern, search, replace) in patterns
]


def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)


if __name__ == '__main__':
    print(plural('dog'))
    print(plural('cat'))
    print(plural('coach'))
    print(plural('rash'))
    print(plural('bass'))
    print(plural('fax'))
    print(plural('vacancy'))
    print(plural('day'))
    print(plural('knife'))
    print(plural('house'))
