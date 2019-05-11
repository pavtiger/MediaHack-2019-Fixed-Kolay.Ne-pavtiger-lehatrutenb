import pymorphy2
morph = pymorphy2.MorphAnalyzer()

def toKind(Name):
    return morph.parse(Name)[0].normal_form

def compile(string):
    return string.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('/', '')

def check_text(txt, tags):
    txt = compile(txt).split(' ')
    summ = 0
    for tagWord in tags:
        tagWord = toKind(compile(tagWord))
        tagLen = tagWord.count(' ')
        for i in range(len(txt) - (tagLen + 1)):
            summ += [0, 1][tagWord == toKind(' '.join(txt[i:i + tagLen + 1]))]
    print(summ)

if __name__ == "__main__":
    strr = "В последнее время редактор XDA Developers, Мишал Рахмана, проделал большую работу, выискивая кодовые имена и краткие спецификации предполагаемых смартфонов и планшетов. Недавно он натолкнулся на несколько новых устро//йств Huawei, и теперь у него есть пара из"
    check_text(strr, ['XDA Developers', 'Мишал Рахмана'])
