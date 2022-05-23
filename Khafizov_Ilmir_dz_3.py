def thesaurus(*args):
    out_dict = {}
    for name in args:
        out_dict.setdefault(name[0], [])
        out_dict[name[0]].append(name)
    return out_dict
print(thesaurus('Иван', 'Мария', 'Петр', 'Илья', 'Федор'))