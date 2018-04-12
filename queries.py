from ckds import CKDS, Person, Company, Department, State, City, League, Club, Exchange
from pprint import pprint

ckds = CKDS()

# City for each exchange

exchanges_list = ckds.db.open().query(Exchange).all()
for exchange in exchanges_list:
    exchange_cities = exchange.city
    results = ckds.get_json("http://data.coding.kitchen/api/city/{}".format(exchange_cities))
    print(results)
    print(results.name)




# high_rev_cos = ckds.db.open().query(Company).filter(Company.revenue > 1000).all()
# for high_rev_co in high_rev_cos:
#     pprint(high_rev_co.name)

# state_capitals = ckds.db.open().query(City).filter(City.is_capital == 1).all()
# for state_capital in state_capitals:
#     pprint(state_capital.name)