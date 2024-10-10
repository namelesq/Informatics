print('Добро пожаловать в пиццерию!')
print('Наше меню:\nпиццы: \nМаргарита -8 долларов, пеперони -6 долларов, мясная - 7 долларов, сырная - 7 долларов.\n напитки: \n вода - 3 доллара, sprite - 3 доллара, fanta - 3 доллара')
print('Если хотите выбрать маргариту, нажмите 1')
print('Если хотите выбрать пеперони, нажмите 2')
print('Если хотите выбрать мясную, нажмите 3')
print('Если хотите выбрать сырную, нажмите 4')
print('Если хотите выбрать воду, нажмите 5')
print('Если хотите выбрать sprite, нажмите 6')
print('Если хотите выбрать fanta, нажмите 7')
print('У нас есть скидки!\n Если сумма заказа свыше 50 долларов,то скидка 20 процентов \n Каждая пицца в подарок\n если напитков более трех, то скидка на них 15 процентов')
work=True
allsum=0
basket=[]
allsumpizza=0
allsumdrinks=0
while work:
    choise = input('Какой товар хотите добавить в корзину? Нажмите код этого продукта')
    if choise == '1':
        allsumpizza += 8
        basket.append(' пицца маргарита')
        add = input('Хотите еще добавить эту пиццу?')
        if add == 'да':
            allsumpizza += 8
            basket.append('пицца маргарита')
        else:
            print('Выберите что нибудь другое!')
    if choise == '2':
        allsumpizza += 6
        basket.append('пицца пеперони')

        add = input('Хотите еще добавить эту пиццу?')
        if add == 'да':
            allsumpizza += 8
            basket.append('пицца пеперони')
        else:
            print('выберите что нибудь другое!')
    if choise == '3':
        allsumpizza += 7
        basket.append('пицца мясная')
        add = input('Хотите еще добавить эту пиццу?')
        if add == 'да':
            allsumpizza += 7
            basket.append('пицца мясная')
        else:
            print('Выберите что нибудь другое!')
    if choise == '4':
        allsumpizza += 7
        basket.append('пицца сырная')
        add = input('Хотите еще добавить эту пиццу?')
        if add == 'да':
            allsumpizza += 7
            basket.append('пицца сырная')
        else:
            print('Выберите что нибудь другое!')
    if choise == '5':
        allsumdrinks += 3
        basket.append('вода')
        add1 = input('Хотите еще добавить этот напиток?')
        if add1 == 'да':
            allsumdrinks += 3
            basket.append('вода')
        else:
            print('Выберите что нибудь другое!')
    if choise == '6':
        allsumdrinks += 3
        basket.append('sprite')
        add1 = input('Хотите еще добавить этот напиток?')
        if add1 == 'да':
            allsumdrinks += 3
            basket.append('sprite')
        else:
            print('выберите что нибудь другое!')
    if choise == '7':
        allsumdrinks += 3
        basket.append('fanta')
        add1 = input('Хотите еще добавить этот напиток?')
        if add1 == 'да':
            allsumdrinks += 3
            basket.append('fanta')
        else:
            print('Выберите что нибудь другое!')
            break
if basket[4]=='пицца маргарита':
    allsumpizza-=8
    print('У вас действует скидка-каждая пятая пицца в подарок')
elif basket[4]=='пицца пеперони':
    allsumpizza-=6
    print('У вас действует скидка-каждая пятая пицца в подарок')

elif basket[4]=='пицца мясная':
    allsumpizza-=7
    print('У вас действует скидка-каждая пятая пицца в подарок')
elif basket[4]=='пицца сырная':
    allsumpizza-=7
    print('У вас действует скидка-каждая пятая пицца в подарок')
else:
    print('У вас не будет скидки - каждая пятая пицца в подарок')

if basket[9]=='пицца маргарита':
    allsumpizza-=8
    print('У вас действует скидка-каждая пятая пицца в подарок')
elif basket[9]=='пицца пеперони':
    allsumpizza-=6
    print('У вас действует скидка-каждая пятая пицца в подарок')

elif basket[9]=='пицца мясная':
    allsumpizza-=7
    print('У вас действует скидка-каждая пятая пицца в подарок')
elif basket[9]=='пицца сырная':
    allsumpizza-=7
    print('У вас действует скидка-каждая пятая пицца в подарок')
else:
    print('У вас не будет скидки - каждая пятая пицца в подарок')
if basket[14]=='пицца маргарита':
    allsumpizza-=8
    print('У вас действует скидка-каждая пятая пицца в подарок')
elif basket[14]=='пицца пеперони':
    allsumpizza-=6
    print('У вас действует скидка-каждая пятая пицца в подарок')

elif basket[14]=='пицца мясная':
    allsumpizza-=7
    print('У вас действует скидка-каждая пятая пицца в подарок')
elif basket[14]=='пицца сырная':
    allsumpizza-=7
    print('У вас действует скидка-каждая пятая пицца в подарок')
else:
    print('У вас не будет скидки - каждая пятая пицца в подарок')
if allsumdrinks > 9:
    print('Вы выбрали больше трех напитков, у вас будет скидка на напитки 15 процентов. Цена ваших напитков:',allsumdrinks - (allsumdrinks / 100 * 15), 'долларов')
else:
    print('Скидки на напитки не будет')
allsum = allsumpizza + allsumdrinks
if allsum > 50:
    print('Ваша цена покупки свыше 50 долларов, у вас действует скидка 20 процентов.', allsum - (allsum / 100 * 20),'долларов')
else:
    print('У вас не будет скидки на покупку')
print('Ваш чек:')
print('Корзина:', basket)
print('Итого к оплате:', allsum, 'Долларов')
print('спасибо, что выбрали нас, ждем Вас снова!')
