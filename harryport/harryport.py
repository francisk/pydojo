from functools import partial

DISCOUNT={5:0.75,
          4:0.8,
          3:0.85,
          2:0.9,
          1:1}
BOOK_PRICE=8

def get_all_prices(book_price,discount_mapping,buying_strategy):
    return reduce(lambda x,y:x+y,
                  map(partial(get_stratege_price,
                              book_price,
                              discount_mapping),buying_strategy))

def get_stratege_price(book_price,discount,combination):
    return book_price*discount[combination]*combination
        
def get_min_price(book_count,book_combinations,price,discount):
    strategies=get_buying_strategies(book_count,book_combinations)
    prices= map(partial(get_all_prices,price,discount),strategies)
    return reduce(lambda x,y:x>=y and y or x,prices)

def get_buying_strategies(book_count,book_combinations):
    for choice in range(1,book_combinations+1):
        if book_count/choice > 0:
            if (book_count-choice)>0:
                for result in get_buying_strategies(book_count-choice,
                                                      book_combinations):
                    yield (choice,)+ result
            else:
                yield (choice,)
        else:
            continue
def smoke():
    print get_min_price(9,5,BOOK_PRICE,DISCOUNT)

if __name__ == '__main__':
    smoke()

