def extraction_decimale():

    cobaye = 424242.8412
    split_cobaye = str(cobaye).split('.')
    partie_entiere = int(split_cobaye[0])
    partie_decimale = int(split_cobaye[1]) * 10 ** -len(split_cobaye[1])
    print("partie entière :", partie_entiere)
    print("partie decimale :", partie_decimale)


extraction_decimale()