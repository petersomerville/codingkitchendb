from ckds import CKDS, Person, Company, Department, State, City, League, Club, Exchange
from pprint import pprint

ckds = CKDS()

try:
    for person_id in range(1,50):
        results = ckds.get_json("http://data.coding.kitchen/api/people/{}".format(person_id))
        for per in results:
            person = Person()
            person.parse_person(per)
            thing = ckds.db.open().query(Person).filter(Person.url == person.url).all()
            if len(thing) == 0:
                ckds.db.save(person)
except:
    print('No more pages of people.')

try:
    for company_id in range(1,10):
        results = ckds.get_json("http://data.coding.kitchen/api/companies/{}".format(company_id))
        for co in results:
            company = Company()
            company.parse_company(co)
            thing = ckds.db.open().query(Company).filter(Company.url == company.url).all()
            if len(thing) == 0:
                ckds.db.save(company)
except:
    print('No more pages of companies.')

try:
    for department_id in range(1,10):
        results = ckds.get_json("http://data.coding.kitchen/api/departments/{}".format(department_id))
        for dept in results:
            department = Department()
            department.parse_department(dept)
            thing = ckds.db.open().query(Department).filter(Department.url == department.url).all()
            if len(thing) == 0:
                ckds.db.save(department)
except:
    print('No more pages of departments.')

results = ckds.get_json("http://data.coding.kitchen/api/states/")
for st in results:
    state = State()
    state.parse_state(st)
    thing = ckds.db.open().query(State).filter(State.abbreviation == state.abbreviation).all()
    if len(thing) == 0:
        ckds.db.save(state)    

try:
    for city_id in range(1,50):
        results = ckds.get_json("http://data.coding.kitchen/api/cities/{}".format(city_id))
        for ci in results:
            city = City()
            city.parse_city(ci)
            thing = ckds.db.open().query(City).filter(City.url == city.url).all()
            if len(thing) == 0:
                ckds.db.save(city)
except: 
    print('No more pages of cities.')

results = ckds.get_json("http://data.coding.kitchen/api/leagues/")
for le in results:
    league = League()
    league.parse_league(le)
    thing = ckds.db.open().query(League).filter(League.url == league.url).all()
    if len(thing) == 0:
        ckds.db.save(league)

try:
    for club_id in range(1,10):
        results = ckds.get_json("http://data.coding.kitchen/api/clubs/{}".format(club_id))
        for cl in results:
            club = Club()
            club.parse_club(cl)
            thing = ckds.db.open().query(Club).filter(Club.url == club.url).all()
            if len(thing) == 0:
                ckds.db.save(club)    
except:
    print('No more pages of clubs.')

results = ckds.get_json("http://data.coding.kitchen/api/exchanges/")
for ex in results:
    exchange = Exchange()
    exchange.parse_exchange(ex)
    thing = ckds.db.open().query(Exchange).filter(Exchange.url == exchange.url).all()
    if len(thing) == 0:
        ckds.db.save(exchange)  