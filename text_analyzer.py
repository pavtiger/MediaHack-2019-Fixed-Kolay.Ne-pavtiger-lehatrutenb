import pymorphy2
morph = pymorphy2.MorphAnalyzer()

def toKind(Name):
    return morph.parse(Name)[0].normal_form

def compile(string):
    return string.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('/', '')

def check_text(txt, tags):
    """ Takes text and tags to search.
    Returns True if text has tags in it, and False if not """
    txt = compile(txt).split(' ')
    summ = 0
    for tagWord in tags:
        tagWord = toKind(compile(tagWord))
        tagLen = tagWord.count(' ')
        for i in range(len(txt) - (tagLen + 1)):
            summ += [0, 1][tagWord == toKind(' '.join(txt[i:i + tagLen + 1]))]
    return summ >= 1

if __name__ == "__main__":
    strr = "В последнее время редактор XDA Developers, Мишал Рахман, проделал большую работу, выискивая кодовые имена и краткие спецификации предполагаемых смартфонов и планшетов. Недавно он натолкнулся на несколько новых устройств Huawei, и теперь у него есть пара из"
    print(check_text(strr, []))
